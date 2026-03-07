# 🚀 Quick Start Guide - AI Tweet Generator

## In 3 Steps:

### 1️⃣ Ensure Server is Running
The Flask server should be running on port 8888. If not, start it with:
```bash
cd /Users/macos/Desktop/ALL\ files\ and\ folder/Assignment\ /AI\ project
python3 backend/app.py
```

### 2️⃣ Open the Web Interface
Navigate to: **http://localhost:8888**

### 3️⃣ Generate Tweets!
Fill in the form:
- **Brand Name**: e.g., "Nike"
- **Industry**: e.g., "Sportswear"  
- **Campaign Objective**: e.g., "Product promotion"
- Click "Generate Tweets ✨"

---

## 📝 Example Brand Information

**Nike Example:**
```
Brand Name: Nike
Industry: Sportswear
Campaign Objective: Product promotion
Product Description: Performance running shoes with advanced cushioning
Target Audience: Young athletes and fitness enthusiasts
Additional Notes: Bold, motivational, and inspiring brand voice
```

**Starbucks Example:**
```
Brand Name: Starbucks
Industry: Food & Beverage
Campaign Objective: New seasonal drink launch
Product Description: Limited edition pumpkin spice beverages
Target Audience: Coffee lovers and seasonal product enthusiasts
Additional Notes: Warm, inviting, community-focused brand
```

**Tesla Example:**
```
Brand Name: Tesla
Industry: Electric Vehicles
Campaign Objective: EV adoption awareness
Product Description: Sustainable, innovative electric vehicles
Target Audience: Tech-savvy environmental advocates
Additional Notes: Futuristic, innovative, eco-conscious brand
```

---

## 🎯 What You'll Get

For each brand submission, you'll receive:

### Brand Voice Summary
- **Tone**: The communication style (e.g., professional, witty, casual)
- **Target Audience**: Who the brand appeals to
- **Communication Style**: How the brand speaks
- **Key Content Themes**: Main message topics

### 10 Generated Tweets
Each with:
- Tweet text (under 280 characters)
- Character count
- Optimized for engagement and brand consistency

### Export Options
- Download results as JSON
- Generate another set of tweets
- Copy-paste individual tweets

---

## 🔌 API Usage (Advanced)

### Generate Tweets via cURL
```bash
curl -X POST http://localhost:8888/api/generate-tweets \
  -H "Content-Type: application/json" \
  -d '{
    "brand_name": "Nike",
    "industry": "Sportswear",
    "campaign_objective": "Product promotion",
    "product_description": "Running shoes",
    "target_audience": "Athletes",
    "additional_notes": "Energetic and motivational"
  }'
```

### Generate Tweets via Python
```python
import requests
import json

url = "http://localhost:8888/api/generate-tweets"
payload = {
    "brand_name": "Nike",
    "industry": "Sportswear",
    "campaign_objective": "Product promotion",
    "product_description": "Running shoes",
    "target_audience": "Athletes",
    "additional_notes": "Energetic"
}

response = requests.post(url, json=payload)
result = response.json()

for i, tweet in enumerate(result['tweets'], 1):
    print(f"Tweet {i}: {tweet['text']}")
```

### Generate Tweets via JavaScript/Fetch
```javascript
fetch('http://localhost:8888/api/generate-tweets', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        brand_name: 'Nike',
        industry: 'Sportswear',
        campaign_objective: 'Product promotion',
        product_description: 'Running shoes',
        target_audience: 'Athletes',
        additional_notes: 'Energetic'
    })
})
.then(response => response.json())
.then(data => console.log(data.tweets));
```

---

## 🐛 Troubleshooting

### "Cannot connect to localhost:8888"
- Check if server is running
- Verify port 8888 is available
- Try: `ps aux | grep python3`

### "API key not found"
- Verify `.env` file contains `OPENROUTER_API_KEY`
- Check file is in project root directory
- Restart server after changing .env

### "Connection refused"
- Server might not be running
- Check firewall settings
- Try a different port if 8888 is in use

### Server crashes after request
- Check internet connection for OpenRouter API
- Verify API key is valid
- Check server logs for errors
- API might be rate limited

---

## 📊 Response Format

**Successful Response:**
```json
{
  "success": true,
  "campaign_id": 1,
  "brand_voice_summary": {
    "tone": "Bold and inspirational",
    "target_audience": "Young athletes",
    "communication_style": "Motivational and energetic",
    "key_themes": "Performance, innovation, achievement"
  },
  "tweets": [
    {
      "text": "Push your limits. Achieve your dreams. #JustDoIt",
      "char_count": 56
    },
    ...
  ]
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Error message describing what went wrong"
}
```

---

## ⚡ Performance Tips

1. **Faster Generation**: Simpler brand information = faster response
2. **Better Results**: More detailed product description = better tweets
3. **Caching**: Results are automatically saved if database is available
4. **Batch Requests**: Generate multiple brands sequentially

---

## 📞 Support

For issues or questions:
1. Check `EXECUTION_SUMMARY.md` for detailed documentation
2. Review `PROJECT_SETUP_COMPLETE.md` for configuration help
3. Verify `.env` file has correct settings
4. Check server logs: `tail /tmp/server.log`

---

## ✅ You're All Set!

Your AI Tweet Generator is ready to create amazing, on-brand tweets! 

**Start now**: http://localhost:8888

Happy tweeting! 🐦✨

