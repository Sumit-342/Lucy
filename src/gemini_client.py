import os
from dotenv import load_dotenv
from google import genai
from prompt import SYSTEM_PROMPT

# Load .env file
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# Create client
client = genai.Client(api_key=api_key)


def generate_reply(user_message,emotion,context):

    full_prompt = f"""
{SYSTEM_PROMPT}

Detected Emotion:
{emotion}

Always make your response consistent with the detected emotion.
Trust the detected emotion while responding.

Conversation Context:
{context}

The conversation context contains the recent messages from the user.
Use it to understand the situation better.
Do not repeat the context back to the user.

User Message:
{user_message}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )

    return response.text


if __name__ == "__main__":

    while True:

        msg = input("You: ")

        if msg.lower() == "exit":
            break

        print("\nLucy:", generate_reply(msg))