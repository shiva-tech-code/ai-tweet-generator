import os
from dotenv import load_dotenv

load_dotenv()

class PromptHelper:
    @staticmethod
    def get_system_prompt():
        try:
            prompt_path = os.path.join(os.path.dirname(__file__), '../../prompts/system_prompt.txt')
            with open(prompt_path, 'r') as f:
                return f.read()
        except:
            return """You are an expert social media marketer specializing in creating engaging tweets.
Analyze the brand information provided and generate exactly 10 engaging tweets that are:
- Under 280 characters each
- Aligned with the brand voice
- Suitable for the target audience
- Promoting the campaign objective

Format each tweet as: 1. [tweet content], 2. [tweet content], etc."""

    @staticmethod
    def create_user_prompt(**kwargs):
        return f"""
Brand Name: {kwargs.get('brand_name', '')}
Industry: {kwargs.get('industry', '')}
Campaign Objective: {kwargs.get('campaign_objective', '')}
Product Description: {kwargs.get('product_description', '')}
Target Audience: {kwargs.get('target_audience', '')}
Additional Notes: {kwargs.get('additional_notes', '')}

Please analyze this brand and generate 10 engaging tweets suitable for social media.
"""
