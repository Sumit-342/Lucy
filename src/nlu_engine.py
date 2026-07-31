from src.groq_client import client
import json


# # --------------------------------------------------
# # Load Environment Variables
# # --------------------------------------------------

# load_dotenv()

# api_key = os.getenv("GROQ_API_KEY")

# if not api_key:
#     raise ValueError("GROQ_API_KEY not found in .env file.")

# # --------------------------------------------------
# #  GROQ Client
# # --------------------------------------------------

# client = OpenAI(
#     base_url="https://api.groq.com/openai/v1",
#     api_key=api_key
# )

# --------------------------------------------------
# Emotion + Mode Classification Prompt
# --------------------------------------------------

SYSTEM_PROMPT = """
You are Lucy's Natural Language Understanding (NLU) engine.

Your job is to analyze the user's message and determine:

1. The dominant emotion.
2. The most appropriate conversation mode.

The input may contain:
- English
- Roman Hindi
- Hinglish
- Emojis
- Internet slang
- Typos
- Repeated letters (e.g. "sooooo", "masttttt")

Guidelines:

- Focus on the user's underlying meaning.
- Consider emojis as part of the message.
- If multiple emotions exist, return the dominant one.
- Return "neutral" only when no clear emotion is present.
- Choose the single best conversation mode.

Valid emotions:

happy
sad
angry
anxious
sarcastic
passive-aggressive
relieved
neutral

Valid conversation modes:

crisis
comfort
celebrate
vent
love
motivate
explain
casual

Return ONLY valid JSON.

Do NOT explain.

Do NOT use markdown.

Return exactly this format:

{
  "emotion": "...",
  "mode": "..."
}
"""

def analyze_message(text: str):
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text}
            ],
            temperature=0.0,
            top_p=0.7,
            max_tokens=45
        )

        raw_response = completion.choices[0].message.content.strip()

        result = json.loads(raw_response)

        return result

    except Exception as e:
        print(f"NLU Engine Error: {e}")
        return None
    

if __name__ == "__main__":

    while True:

        text = input("You: ")

        if text.lower() == "exit":
            break

        print(analyze_message(text))
        print(type(analyze_message(text)))