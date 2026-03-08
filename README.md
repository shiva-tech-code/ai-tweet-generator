<div align="center">

# 🐦 AI-Powered Tweet Generator

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Visit_Now-brightgreen?style=for-the-badge)](https://ai-tweet-generator-0dgo.onrender.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github)](https://github.com/shiva-tech-code/ai-tweet-generator)
[![Python](https://img.shields.io/badge/Python-3.9+-yellow?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-red?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

<p align="center">
  <strong>🚀 An intelligent social media strategy tool that analyzes brand voice and generates authentic, engaging tweets using AI</strong>
</p>

[**🌐 Live Demo**](https://ai-tweet-generator-0dgo.onrender.com/) • [**📖 Documentation**](#-features) • [**🛠️ Installation**](#-installation) • [**📧 Contact**](#-contact)

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎯 **Brand Voice Analysis** | AI analyzes your brand personality and communication style |
| 🐦 **Smart Tweet Generation** | Generates 10 unique, on-brand tweets following best practices |
| 📊 **Multiple Tweet Types** | Engaging, promotional, witty, and informative tweets |
| ✅ **Character Compliance** | All tweets stay within Twitter's 280 character limit |
| 🎨 **Beautiful UI** | Modern, responsive web interface |
| ⚡ **Fast & Reliable** | Powered by Groq's lightning-fast AI inference |

---

## 🎬 Live Demo

<div align="center">

### 🌐 **[Try it Now → ai-tweet-generator-0dgo.onrender.com](https://ai-tweet-generator-0dgo.onrender.com/)**

</div>

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           AI TWEET GENERATOR                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌──────────────┐         ┌──────────────┐         ┌──────────────┐        │
│   │   FRONTEND   │         │   BACKEND    │         │   GROQ AI    │        │
│   │              │  HTTP   │              │   API   │              │        │
│   │  HTML/CSS/JS │ ──────► │  Flask API   │ ──────► │  LLaMA 3.3   │        │
│   │              │         │              │         │  70B Model   │        │
│   └──────────────┘         └──────────────┘         └──────────────┘        │
│         │                        │                                           │
│         │                        │                                           │
│         ▼                        ▼                                           │
│   ┌──────────────┐         ┌──────────────┐                                 │
│   │   Browser    │         │   Prompts    │                                 │
│   │   Display    │         │   Engine     │                                 │
│   └──────────────┘         └──────────────┘                                 │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 How It Works - Workflow

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Step 1    │    │   Step 2    │    │   Step 3    │    │   Step 4    │
│             │    │             │    │             │    │             │
│ Enter Brand │───►│  AI Analyzes│───►│  Generate   │───►│   Display   │
│   Details   │    │ Brand Voice │    │   Tweets    │    │   Results   │
│             │    │             │    │             │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
      │                  │                  │                  │
      ▼                  ▼                  ▼                  ▼
 ┌─────────┐       ┌─────────┐       ┌─────────┐       ┌─────────┐
 │• Brand  │       │• Tone   │       │• 10     │       │• Copy   │
 │  Name   │       │• Style  │       │  Unique │       │• Share  │
 │• Industry│      │• Voice  │       │  Tweets │       │• Export │
 │• Goals  │       │• Summary│       │• Types  │       │         │
 └─────────┘       └─────────┘       └─────────┘       └─────────┘
```

### 📋 Detailed Workflow:

1. **📝 Input Brand Details** - User enters brand name, industry, campaign objective, and target audience
2. **🤖 AI Processing** - Groq's LLaMA 3.3 70B model analyzes the brand information
3. **🎨 Brand Voice Analysis** - AI creates a comprehensive brand voice summary
4. **🐦 Tweet Generation** - 10 unique tweets are generated with different styles
5. **📤 Output Display** - Tweets are displayed with copy functionality

---

## 📁 Project Structure

```
AI-Tweet-Generator/
├── 📂 backend/
│   ├── 📄 app.py                 # Main Flask application
│   ├── 📂 config/
│   │   └── 📄 database.py        # Database configuration
│   ├── 📂 controllers/
│   │   └── 📄 tweet_controller.py # Business logic & AI integration
│   ├── 📂 routes/
│   │   └── 📄 tweets_routes.py   # API endpoints
│   └── 📂 utils/
│       ├── 📄 prompt_helper.py   # AI prompt management
│       └── 📄 tweet_parser.py    # Tweet parsing utilities
│
├── 📂 frontend/
│   ├── 📄 index.html             # Landing page
│   ├── 📄 generator.html         # Tweet generator page
│   ├── 📂 css/
│   │   └── 📄 styles.css         # Stylesheet
│   ├── 📂 js/
│   │   └── 📄 main.js            # Frontend JavaScript
│   └── 📂 images/                # Image assets
│
├── 📂 prompts/
│   └── 📄 system_prompt.txt      # AI system prompt
│
├── 📄 .env                       # Environment variables
├── 📄 requirements.txt           # Python dependencies
├── 📄 Procfile                   # Deployment config
└── 📄 README.md                  # Documentation
```

---

## 🛠️ Installation

### Prerequisites

- Python 3.9+
- Groq API Key ([Get it free](https://console.groq.com/keys))

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/shiva-tech-code/ai-tweet-generator.git
cd ai-tweet-generator

# 2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
cat > .env << EOF
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
SERVER_PORT=8888
EOF

# 5. Run the application
python3 backend/app.py
```

### 🌐 Open in Browser

```
http://localhost:8888
```

---

## 📡 API Endpoints

### `POST /api/generate-tweets`

Generate AI-powered tweets based on brand details.

**Request:**
```json
{
  "brand_name": "Nike",
  "industry": "Sportswear",
  "campaign_objective": "Product promotion",
  "product_description": "Running shoes with advanced cushioning",
  "target_audience": "Young athletes and fitness enthusiasts",
  "additional_notes": "Bold, motivational brand voice"
}
```

**Response:**
```json
{
  "success": true,
  "campaign_id": 1,
  "brand_voice_summary": "Energetic, motivational, athlete-focused...",
  "tweets": [
    {
      "type": "engaging",
      "content": "Every step counts. Every mile matters. 🏃‍♂️ #JustDoIt",
      "hashtags": ["JustDoIt", "Running"]
    }
  ]
}
```

---

## 🛠️ Technologies Used

<div align="center">

| Technology | Purpose |
|:----------:|:-------:|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | Backend Language |
| ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) | Web Framework |
| ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) | Frontend Structure |
| ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) | Styling |
| ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) | Frontend Logic |
| ![Groq](https://img.shields.io/badge/Groq_AI-FF6B6B?style=for-the-badge) | AI Engine |

</div>

---

## 🚀 Deployment

### Deploy on Render

1. Fork this repository
2. Create a new Web Service on [Render](https://render.com)
3. Connect your GitHub repository
4. Set environment variables:
   - `GROQ_API_KEY`: Your Groq API key
   - `GROQ_MODEL`: llama-3.3-70b-versatile
5. Deploy!

---

## 👨‍💻 Author & Contact

<div align="center">

### 🙋‍♂️ **Shiva**

[![GitHub](https://img.shields.io/badge/GitHub-shiva--tech--code-181717?style=for-the-badge&logo=github)](https://github.com/shiva-tech-code)
[![Email](https://img.shields.io/badge/Email-Contact_Me-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:shiva.tech.code@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/)

</div>

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. 🍴 Fork the repository
2. 🔧 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit changes (`git commit -m 'Add AmazingFeature'`)
4. 📤 Push to branch (`git push origin feature/AmazingFeature`)
5. 🔃 Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### ⭐ Star this repository if you found it helpful!

<br>

**Made with ❤️ using AI**

[![GitHub stars](https://img.shields.io/github/stars/shiva-tech-code/ai-tweet-generator?style=social)](https://github.com/shiva-tech-code/ai-tweet-generator/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/shiva-tech-code/ai-tweet-generator?style=social)](https://github.com/shiva-tech-code/ai-tweet-generator/network/members)

</div>
