import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
model_name = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")


def split_text(text, chunk_size=1800):
    words = text.split()
    return [
        " ".join(words[i:i + chunk_size])
        for i in range(0, len(words), chunk_size)
    ]


def summarize_text(text):

    chunks = split_text(text)
    summaries = []

    for chunk in chunks:

        prompt = f"""
You are an expert YouTube video summarizer.

The transcript may be in Hindi or another language.

IMPORTANT:
Write your response in ENGLISH ONLY.

Analyze this transcript section.

Return no more than 120 words. Include only the most important facts.

Transcript:
{chunk}
"""

        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=220,
        )

        summaries.append(
            response.choices[0].message.content
        )

    combined = "\n\n".join(summaries)
    combined = combined[:20000]

    final_prompt = f"""
Create a final YouTube video summary.

IMPORTANT:
WRITE EVERYTHING IN ENGLISH ONLY.

Use exactly this format:

## 📌 Summary

- 5 important summary points

## ⭐ Important Points

- 5 most important points from the video

## 📚 Main Topics

- 3 main topics

## 💡 Key Takeaways

- 3 practical takeaways

Keep the answer concise.
Do not mention transcript sections.

Content:
{combined}
"""

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ],
        temperature=0.3,
        max_tokens=600,
    )

    return response.choices[0].message.content