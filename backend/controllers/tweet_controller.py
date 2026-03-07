import os
import json
import requests
from flask import jsonify
from dotenv import load_dotenv

# Load environment variables from the project root
env_path = os.path.join(os.path.dirname(__file__), '../../.env')
load_dotenv(env_path)

from utils.prompt_helper import PromptHelper
from utils.tweet_parser import TweetParser

class TweetController:
    def __init__(self):
        self.prompt_helper = PromptHelper()
        self.parser = TweetParser()
        self.api_key = os.getenv('OPENROUTER_API_KEY')
        self.model = os.getenv('OPENROUTER_MODEL', 'openai/gpt-4-turbo')
        self.campaigns = {}
        self.campaign_counter = 0
        print("✅ TweetController initialized (no database)")

    def generate_tweets(self, data):
        try:
            required_fields = ['brand_name', 'industry', 'campaign_objective']
            for field in required_fields:
                if field not in data or not data[field]:
                    return jsonify({"success": False, "error": f"Missing required field: {field}"}), 400

            system_prompt = self.prompt_helper.get_system_prompt()
            user_prompt = self.prompt_helper.create_user_prompt(**data)

            response = self._call_openrouter_api(system_prompt, user_prompt)
            
            if not response or 'error' in response:
                error_msg = response.get('error', 'API error') if response else 'API call failed'
                return jsonify({"success": False, "error": error_msg}), 500

            raw_response = response.get('choices', [{}])[0].get('message', {}).get('content', '')
            
            if not raw_response:
                return jsonify({"success": False, "error": "No response from API"}), 500

            brand_voice_summary = self._extract_brand_voice(raw_response)
            tweets = self.parser.parse_tweets(raw_response)

            self.campaign_counter += 1
            campaign_id = self.campaign_counter
            self.campaigns[campaign_id] = {
                "brand_name": data.get('brand_name'),
                "response": raw_response,
                "input_data": data
            }

            result = {
                "success": True,
                "campaign_id": campaign_id,
                "brand_voice_summary": brand_voice_summary,
                "tweets": tweets
            }

            return jsonify(result), 200

        except Exception as e:
            print(f"Error in generate_tweets: {e}")
            return jsonify({"success": False, "error": str(e)}), 500

    def _call_openrouter_api(self, system_prompt, user_prompt):
        try:
            if not self.api_key:
                print("No API key found!")
                return {"error": "API key not configured"}
            
            print(f"Calling OpenRouter API with model: {self.model}")
            
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:8888",
                "X-Title": "AI Tweet Generator"
            }

            payload = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature": 0.7,
                "max_tokens": 500
            }

            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=60
            )

            print(f"API Response Status: {response.status_code}")

            if response.status_code == 200:
                return response.json()
            else:
                error_text = response.text[:200]
                print(f"API error: {response.status_code} - {error_text}")
                return {"error": f"API returned status {response.status_code}: {error_text}"}

        except requests.exceptions.Timeout:
            print("API request timed out")
            return {"error": "API request timed out. Please try again."}
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return {"error": f"Request failed: {str(e)}"}
        except Exception as e:
            print(f"Error calling API: {e}")
            return {"error": str(e)}

    def _extract_brand_voice(self, response_text):
        summary = {
            "tone": "Professional and engaging",
            "target_audience": "Brand audience",
            "communication_style": "Social media focused",
            "key_themes": "Brand promotion and engagement"
        }

        lines = response_text.split('\n')

        for line in lines:
            line = line.strip()
            if 'Tone:' in line:
                summary["tone"] = line.split('Tone:')[-1].strip().strip('•-')
            elif 'Target Audience:' in line:
                summary["target_audience"] = line.split('Target Audience:')[-1].strip().strip('•-')
            elif 'Communication Style:' in line or 'Style:' in line:
                key = 'Communication Style:' if 'Communication Style:' in line else 'Style:'
                summary["communication_style"] = line.split(key)[-1].strip().strip('•-')
            elif 'Key' in line and 'Theme' in line:
                if 'Key Content Themes:' in line:
                    summary["key_themes"] = line.split('Key Content Themes:')[-1].strip().strip('•-')
                elif 'Key Themes:' in line:
                    summary["key_themes"] = line.split('Key Themes:')[-1].strip().strip('•-')

        return summary

    def get_tweets(self, id):
        try:
            campaign = self.campaigns.get(int(id))
            if not campaign:
                return jsonify({"success": False, "error": "Campaign not found"}), 404

            tweets = self.parser.parse_tweets(campaign['response'])
            brand_voice = self._extract_brand_voice(campaign['response'])

            return jsonify({
                "success": True,
                "campaign_id": id,
                "brand_voice_summary": brand_voice,
                "tweets": tweets
            }), 200

        except Exception as e:
            print(f"Error in get_tweets: {e}")
            return jsonify({"success": False, "error": str(e)}), 500

    def get_campaigns(self):
        try:
            campaigns_list = []
            for cid, data in self.campaigns.items():
                campaigns_list.append({
                    "id": cid,
                    "brand_name": data.get("brand_name", "Unknown")
                })
            return jsonify({"success": True, "campaigns": campaigns_list}), 200

        except Exception as e:
            print(f"Error in get_campaigns: {e}")
            return jsonify({"success": False, "error": str(e)}), 500
