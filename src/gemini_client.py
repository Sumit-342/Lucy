import os
from dotenv import load_dotenv
from google import genai
from prompts.LUCY_PERSONALITY_PROMPT import SYSTEM_PROMPT
from prompts.LUCY_PERSONALITY_PROMPT import LUCY_PERSONALITY_PROMPT
from prompts.MODE_PROMPT import get_mode_prompt

# Load .env file
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# Create client
client = genai.Client(api_key=api_key)


def generate_reply(user_message,emotion,language,mode,context):
    mode_prompt = get_mode_prompt(mode)

    full_prompt = f"""

{LUCY_PERSONALITY_PROMPT}

{SYSTEM_PROMPT}

{mode_prompt}

Detected Emotion:
{emotion}

Always make your response consistent with the detected emotion.
Trust the detected emotion while responding.

The detected emotion is for your internal guidance only.

Never mention the emotion label directly.

Instead, express it naturally in conversation.

Never say things like:
"You are sad."
"You are happy."
"You are anxious."

Instead, naturally reflect the user's feelings through empathetic conversation.

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