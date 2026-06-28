# import os
# import time
# from dotenv import load_dotenv
# from openai import OpenAI

# # 1. Load secure environment variables
# load_dotenv()
# api_key = os.getenv("QWEN_API_KEY")

# if not api_key:
#     raise ValueError("Error: QWEN_API_KEY not found in your .env file!")

# # 2. Initialize the OpenRouter Client
# client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=api_key,
# )

# def get_advanced_emotion(user_text):
#     # System prompt explicitly trained to handle raw emoji tokens natively
#     system_prompt = (
#         "You are Lucy's core emotion classification engine.\n"
#         "Analyze the input text which can be English, Roman Hindi, heavy Hinglish slang, or RAW EMOJIS.\n"
#         "Identify the true emotional undertone by evaluating cultural context, expressions, sarcasm, or symbolic emoji meanings.\n\n"
#         "CRITICAL RULES:\n"
#         "- If the user inputs ONLY emojis (e.g., '😁😁', '😭', '🤬'), analyze their emotional meaning and map them directly to a word from our allowed list.\n"
#         "- Sentences involving open challenges/threats are 'angry'.\n"
#         "- Sentences expressing exhaustion/burnout are 'sad'.\n"
#         "- Passive-aggressive guilt trips are 'sarcastic'.\n\n"
#         "Output EXACTLY ONE lowercase descriptive emotional word from this list:\n"
#         "[happy, sad, angry, anxious, sarcastic, passive-aggressive, relieved, neutral].\n"
#         "Do not use capitalization, punctuation, markdown, or extra words. Just output the raw lowercase descriptor."
#     )
    
#     retries = 3
#     delay = 0.5  
    
#     for attempt in range(retries):
#         try:
#             completion = client.chat.completions.create(
#                 model="openai/gpt-oss-120b:free",
#                 messages=[
#                     {"role": "system", "content": system_prompt},
#                     {"role": "user", "content": user_text}
#                 ],
#                 temperature=0.0  
#             )
#             return completion.choices[0].message.content.strip().lower()
            
#         except Exception as e:
#             if "429" in str(e) and attempt < retries - 1:
#                 print(f"[Traffic Spike] gpt-oss-120b busy. Retrying in {delay}s...")
#                 time.sleep(delay)
#                 delay *= 2  
#                 continue
                
#             print(f"API Error occurred: {e}")
#             return "error"
            
#     return "error"

# # --- THE RAW EMOJI & SLANG STRESS TEST SUITE ---
# if __name__ == "__main__":
#     test_cases = [
#         # --- PURE EMOJI INPUTS ---
#         "😁😁",                                                  # Expected: happy
#         "😭😭😭😭",                                              # Expected: sad
#         "🤬",                                                    # Expected: angry
#         "😰😰",                                                  # Expected: anxious
        
#         # --- MIXED TEXT + EMOJI ---
#         "bhai result aa gaya pass ho gaya main! 🥳🎉",           # Expected: happy
#         "arre yaar kya chal raha hai ye... 😮‍💨",                  # Expected: sad / neutral
#         "Haan thik hai, tum busy ho jao. Mai hi faltu hu. 🙃",   # Expected: sarcastic
#     ]
    
#     print("--- Lucy Advanced Emotion Core (Native Emoji Capabilities) ---")
#     for text in test_cases:
#         emotion = get_advanced_emotion(text)
#         print(f"Input: '{text}' \n   -> Emotion Detected: {emotion}\n")














import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Fetch your securely saved key
load_dotenv()
nvidia_key = os.getenv("NVIDIA_API_KEY")

if not nvidia_key:
    raise ValueError("Error: NVIDIA_API_KEY not found in your environment variables or .env file!")

# 2. Point to NVIDIA's cloud infrastructure endpoint
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=nvidia_key
)

def test_nvidia_emotion_core(user_text):
    system_prompt = (
        "You are Lucy's core emotion classification engine.\n"
        "Analyze the input text which can be English, Roman Hindi, heavy Hinglish slang, or RAW EMOJIS.\n\n"
        "Output EXACTLY ONE lowercase descriptive emotional word from this list:\n"
        "[happy, sad, angry, anxious, sarcastic, passive-aggressive, relieved, neutral].\n"
        "Do not use capitalization, punctuation, markdown, or extra words. Just output the raw lowercase descriptor."
    )

    try:
        completion = client.chat.completions.create(
            model="qwen/qwen3-next-80b-a3b-instruct",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text}
            ],
            temperature=0.0,  # Dropped to 0.0 for highly consistent classification tasks
            top_p=0.7,
            max_tokens=10     # Low token roof since we only expect exactly 1 word back
        )
        
        return completion.choices[0].message.content.strip().lower()
    except Exception as e:
        return f"NVIDIA API Error: {e}"

# --- THE SPEED AND ACCURACY TESTING SUITE ---
if __name__ == "__main__":
    print("--- Testing Qwen3-Next on NVIDIA Build Cluster ---")
    
    test_cases = [
    # Complex/Mixed Emotions
        
        "mst h yr"   ,
                   # Disappointed
]
    
    for phrase in test_cases:
        result = test_nvidia_emotion_core(phrase)
        print(f"Input: '{phrase}'\n  -> Output: {result}\n")