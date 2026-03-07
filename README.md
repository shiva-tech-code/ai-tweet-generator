# AI-Powered Tweet Generator

An intelligent social media strategy tool that analyzes brand voice and generates authentic, engaging tweets.

## Project Overview

This application uses AI to:
1. Analyze brand personality and communication style
2. Generate a brand voice summary
3. Create 10 unique, on-brand tweets following specific guidelines

## Project Structure

```
├── backend/              # Express.js server
│   ├── server.js        # Main server file
│   ├── routes/          # API routes
│   └── controllers/     # Business logic
├── frontend/            # Frontend application
│   ├── index.html       # Main HTML
│   ├── css/            # Stylesheets
│   └── js/             # JavaScript files
├── database/           # Database setup
│   └── setup.js        # Database initialization
├── config/             # Configuration files
│   └── .env.example    # Environment variables template
├── prompts/            # AI Prompts
│   └── system_prompt.txt # Main system prompt
└── package.json        # Project dependencies
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```
   npm install
   ```

3. Set up environment variables:
   ```
   cp config/.env.example config/.env
   ```

4. Update `.env` with your API keys and database credentials

5. Set up database:
   ```
   npm run setup-db
   ```

6. Start the development server:
   ```
   npm run dev
   ```

## API Endpoints

### POST /api/generate-tweets
Generate tweets based on brand details.

**Request Body:**
```json
{
  "brand_name": "Nike",
  "industry": "Sportswear",
  "campaign_objective": "Product promotion",
  "product_description": "Running shoes designed for speed and comfort",
  "target_audience": "Young athletes and runners",
  "additional_notes": "Motivational and energetic brand personality"
}
```

**Response:**
```json
{
  "success": true,
  "brand_voice_summary": {...},
  "tweets": [...]
}
```

## Technologies Used

- **Backend:** Node.js, Express.js
- **Database:** MySQL
- **API:** OpenRouter (AI API)
- **Frontend:** HTML, CSS, JavaScript

## Features

✅ Brand voice analysis
✅ AI-powered tweet generation
✅ Tweet variety (engaging, promotional, witty, informative)
✅ Character limit compliance (280 chars)
✅ Database storage
✅ Responsive web interface

## License

MIT
