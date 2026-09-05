# 🎥 TubeBrief AI

### AI-Powered YouTube Video Summarizer

TubeBrief AI is an AI-powered web application that converts long YouTube video transcripts into concise, structured, and easy-to-understand English summaries.

The application uses **Streamlit** for the web interface, **YouTube Transcript API** for transcript extraction, and **Groq AI** for intelligent summarization.

LIVE URL LINK:https://tubebrief-ai.streamlit.app/



---
<img width="1906" height="1013" alt="Screenshot 2026-09-04 222340" src="https://github.com/user-attachments/assets/cdf94da7-6fd2-42f3-a129-b728bc35fdb4" />
<img width="1904" height="1013" alt="Screenshot 2026-09-04 222354" src="https://github.com/user-attachments/assets/1c9df4d6-b189-4303-aa53-56b0ebe29f13" />



## 🚀 Features

- 🔗 Extract transcripts from YouTube videos
- 📝 Paste transcripts manually when YouTube extraction is unavailable
- 🤖 AI-powered summarization using Groq
- 🇬🇧 Converts Hindi or other language transcripts into English summaries
- 📌 Structured summary points
- ⭐ Important points extraction
- 📚 Main topics identification
- 💡 Key takeaways
- 📊 Transcript statistics
- 📈 Summary visualization
- 📥 Download generated summaries
- 🖥️ Simple and beginner-friendly Streamlit interface
- 🔐 Environment-variable based API key management
- ⚙️ GitHub Actions CI workflow

---

## 🖼️ Project Overview

TubeBrief AI follows a simple pipeline:

```text
YouTube Video
      │
      ▼
Transcript Extraction
      │
      ▼
Transcript Processing
      │
      ▼
Groq AI
      │
      ▼
AI Analysis
      │
      ├── 📌 Summary
      ├── ⭐ Important Points
      ├── 📚 Main Topics
      └── 💡 Key Takeaways
      │
      ▼
Visualization + Download
Download
🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
Streamlit	Web application interface
Groq API	AI-powered summarization
Qwen 3.6 27B	Large language model
YouTube Transcript API	YouTube transcript retrieval
python-dotenv	Environment variable management
GitHub Actions	Continuous Integration
📁 Project Structure
TubeBrief-AI/
│
├── app.py
│
├── utils/
│   ├── __init__.py
│   ├── youtube.py
│   └── summarizer.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
├── .gitignore
├── .env
└── README.md
⚙️ Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/TubeBrief-AI.git

Move into the project directory:

cd TubeBrief-AI
2. Create a virtual environment
Windows
python -m venv .venv

Activate it:

.venv\Scripts\activate
macOS / Linux
python3 -m venv .venv

Activate it:

source .venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
🔑 Groq API Setup

TubeBrief AI uses the Groq API for AI summarization.

Create a Groq API key and store it in a .env file.

Create:

.env

Add:

GROQ_API_KEY=your_groq_api_key_here
Important

Never commit your .env file to GitHub.

Your .gitignore should contain:

.env
.venv/
__pycache__/
*.pyc
▶️ Run the Application

Start Streamlit:

streamlit run app.py

The application will open in your browser.

Usually:

http://localhost:8501
📌 How to Use
Method 1 — YouTube URL
Open TubeBrief AI.
Paste a YouTube video URL.
Click Get Transcript.
Wait for the transcript.
Click Generate English Summary.
View the generated results.
Method 2 — Manual Transcript

If YouTube temporarily blocks or rate-limits transcript requests:

Open the YouTube video.
Open Show Transcript.
Copy the transcript.
Paste it into TubeBrief AI.
Click Use This Transcript.
Click Generate English Summary.

This provides a fallback when automatic transcript extraction is unavailable.

🤖 AI Summary Output

TubeBrief AI generates a structured result containing:

📌 Summary

A concise overview of the video.

⭐ Important Points

The most important information discussed in the video.

📚 Main Topics

The major topics covered by the video.

💡 Key Takeaways

Useful conclusions and lessons from the video.

📊 Transcript Statistics

TubeBrief AI also displays basic transcript statistics such as:

📝 Word count
🔤 Character count

These statistics help users understand the size of the processed content.

📈 Visualization

The application provides a simple visualization of the generated summary sections.

This helps make the results easier to understand and gives the application a more interactive dashboard-style experience.

📥 Download Summary

Users can download the generated AI summary as a text file.

Example:

TubeBrief_AI_Summary.txt
🌐 Supported Languages

TubeBrief AI can process transcripts in different languages depending on transcript availability.

The AI output is configured to be generated in:

English

For example:

Hindi Transcript
       ↓
Groq AI
       ↓
English Summary
🔐 Environment Variables

The application requires:

GROQ_API_KEY=your_api_key

Never hard-code API keys directly inside Python files.

⚠️ Known Limitations
YouTube Transcript Availability

Some YouTube videos may not have transcripts available.

Automatic transcript retrieval can also be temporarily rate-limited or blocked by YouTube depending on the network or IP address.

In such cases, users can use the manual transcript input option.

Long Transcripts

Very long transcripts are processed in smaller chunks before generating the final summary.

This helps reduce large API requests.

API Limits

Groq API usage is subject to the limits of the selected account and model.

🧪 Testing

Before running the application, make sure the environment is configured correctly.

Run:

python -m pip install -r requirements.txt

Then:

streamlit run app.py
⚙️ GitHub Actions

TubeBrief AI includes a GitHub Actions workflow for basic automated checks.

The workflow runs when code is pushed to GitHub or a pull request is created.

Workflow location:

.github/workflows/ci.yml

The CI workflow checks that the Python project can be compiled successfully.

🚀 Deployment

TubeBrief AI can be deployed using Streamlit Community Cloud.

General deployment process:

Push the project to GitHub.
Open Streamlit Community Cloud.
Connect your GitHub account.
Select the TubeBrief AI repository.

Select:

app.py

Add the required secret:

GROQ_API_KEY
Deploy the application.
Important

Do not upload .env to GitHub.

For cloud deployment, configure the API key using the platform's secret management system.

🔒 Security

TubeBrief AI follows basic API key security practices:

API keys are stored using environment variables.
.env is excluded from Git.
API keys should never be written directly in source code.
API keys should never be shared publicly.
🎯 Future Improvements

Future versions of TubeBrief AI may include:

🎬 Automatic video title and thumbnail extraction
⏱️ Video duration detection
🧠 Better topic extraction
📊 Advanced topic visualization
📄 PDF summary download
📑 DOCX summary download
🌍 Multi-language output
🎙️ Audio transcription
🔍 Keyword extraction
📚 Study notes generation
❓ AI-generated questions and answers
📝 Quiz generation
💬 Interactive video Q&A
👤 User accounts and saved summaries
🎓 Academic Project

TubeBrief AI is designed as a practical AI-based application demonstrating the integration of:

Natural Language Processing
Large Language Models
API integration
Web application development
Text summarization
Data visualization
Software version control
Continuous Integration

It can be used as a university/FYP project demonstrating a real-world application of Generative AI.
