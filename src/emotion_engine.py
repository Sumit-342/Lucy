import os

from dotenv import load_dotenv
from openai import OpenAI

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()

api_key = os.getenv("NVIDIA_API_KEY")

if not api_key:
    raise ValueError("NVIDIA_API_KEY not found in .env file.")

# --------------------------------------------------
# NVIDIA Client
# --------------------------------------------------

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)

# --------------------------------------------------
# Emotion Classification Prompt
# --------------------------------------------------

SYSTEM_PROMPT = """
You are Lucy's emotion classification engine.

Your only task is to identify the single dominant emotion expressed by the user.

The input may contain:
- English
- Roman Hindi
- Hinglish
- Internet slang
- Emojis
- Typos
- Repeated letters (e.g. "masttttt")

Guidelines:
- Focus on the user's underlying emotion.
- Consider emojis as part of the emotional meaning.
- Do not assume sarcasm unless there are clear sarcastic cues.
- If multiple emotions exist, return the dominant one.
- Return "neutral" only when no clear emotion is present.
- Never explain your reasoning.

Return EXACTLY ONE lowercase word from this list:

happy
sad
angry
anxious
sarcastic
passive-aggressive
relieved
neutral

Return nothing except that single word.
"""

# --------------------------------------------------
# Emotion Detection
# --------------------------------------------------

def detect_emotion(text: str) -> str:
    try:
        completion = client.chat.completions.create(
            model="qwen/qwen3-next-80b-a3b-instruct",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text}
            ],
            temperature=0.0,
            top_p=0.7,
            max_tokens=5
        )

        emotion = (
            completion.choices[0]
            .message.content
            .strip()
            .lower()
        )

        return emotion.split()[0]

    except Exception as e:
        print(f"Emotion Engine Error: {e}")
        return "neutral"