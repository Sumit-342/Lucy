import joblib
import emoji
from collections import Counter
import pandas as pd
from response_engine import get_response
from language_detector import detect_language
from gemini_client import generate_reply
from emotion_engine import detect_emotion
from conversation_engine import detect_mode

model = joblib.load("models/lucy_pipeline_v0_2.pkl")
df_emoji = pd.read_csv("dataset/emoji_emotions_final.csv")


def clean_emoji(e):                                 # clean emojis
    return e.replace("\ufe0f","").strip()

emoji_dict = {                                         # emoji dictonary
    clean_emoji(k): v
    for k , v in zip (df_emoji["emoji"],df_emoji["emotion"])
}

def extract_emojis(text):                                  # extracting emoji
    return [c for c in text if c in emoji.EMOJI_DATA]


def get_emoji_emotion(text):                        # emotion to emotion mapping
    emojis = extract_emojis(text)

    emotions = []

    for e in emojis:
        e = clean_emoji(e)
        if e in emoji_dict:
            emotions.append(emoji_dict[e])

    if not emotions:
        return None
    
    most_common = Counter(emotions).most_common(1)
    return most_common[0][0] if most_common else None


def get_text_emotion(text):                         # text emotion function
    prediction = model.predict([text])[0]
    probabilities = model.predict_proba([text])[0]
    confidence = max(probabilities)

    return prediction , confidence


def predict_final(text):                                        # text + emoji fusion
    text_emotion , text_confidence = get_text_emotion(text)   # emoji can dubliacte in context 
    emoji_emotion = get_emoji_emotion(history[-1])

    if emoji_emotion is None:
        return text_emotion , text_confidence , "text_only"
    
    if text_confidence >=0.85:
        if emoji_emotion and text_emotion != emoji_emotion:
            return emoji_emotion,text_confidence, "emoji_override"
        return text_emotion , text_confidence , "text_strong"
    
        
    
    elif text_confidence<=0.4:
        return emoji_emotion ,text_confidence,"emoji_strong"
    
    else:
        if text_emotion == emoji_emotion:
            return text_emotion,text_confidence,"text_emoji_agree"
        else:
            return emoji_emotion,text_confidence , "emoji_priority"

history = []
def update_history(new_msg):
    
    history.append(new_msg)

    if len(history)>3:
        history.pop(0)


def get_context():
    if len(history) == 1:
        return history[0]
    
    return " ".join(history)
    


def analyze(text):                                      # output wrapper
    emotion , confidence , mode = predict_final(text)
    

    return {
        "emotion":emotion,
        "confidence":round(float(confidence),2),
        "mode":mode
    }



# if __name__ == "__main__":
    
#     while True :
#         user_input = input("\nYou: ")
#         if user_input.lower() == "exit" :
#             print("Lucy: Goodbye 👋👋")
#             break

#         if not user_input.strip():  
#             print("Lucy: Please say something")
#             continue
        
#         update_history(user_input)
#         context_text = get_context()
#         emotion = detect_emotion(context_text)
#         mode = detect_mode(user_input)
#         language = detect_language(user_input)
        
       
#         try :
#             response = generate_reply(emotion,language,context_text)
#             follow_up = None
#         except Exception as e :
#             print(f"\n Gemini Error : {e}")
#             print("\n Gemini Unavaliable. Using local FallBack")

#             response,follow_up = get_response(emotion,language)

#         print(f"Emotion   : {emotion}")
#         print("History :",history)
#         print("Context : ",context_text)
#         print(f"Mode : {mode}")
#         print("Langauge : ",language)
#         print("Lucy : ",response)

#         if follow_up :
#              print()
#              print(follow_up)




DEBUG = True

if __name__ == "__main__":

    while True:

        user_input = input("\nYou: ").strip()

        if user_input.lower() == "exit":
            print("Lucy: Goodbye 👋👋")
            break

        # -----------------------------
        # Developer Commands
        # -----------------------------
        if user_input.lower() == "/clear":
            history.clear()
            print("✨ Conversation reset.")
            continue

        if not user_input:
            print("Lucy: Please say something.")
            continue

        # -----------------------------
        # Lucy Pipeline
        # -----------------------------
        update_history(user_input)

        context_text = get_context()
        emotion = detect_emotion(context_text)
        mode = detect_mode(user_input)
        language = detect_language(user_input)

        # -----------------------------
        # Response Generation
        # -----------------------------
        try:
            response = generate_reply(
                user_message = user_input,
                emotion=emotion,
                language=language,
                mode=mode,
                context=context_text
            )
            follow_up = None

        except Exception as e:
            print(f"\nGemini Error: {e}")
            print("Gemini unavailable. Using Local Fallback...\n")

            response, follow_up = get_response(
                emotion,
                language
            )

        # -----------------------------
        # Debug Information
        # -----------------------------
        if DEBUG:

            print("\n" + "=" * 60)
            print("                     LUCY DEBUG")
            print("=" * 60)

            print(f"Language : {language}")
            print(f"Emotion  : {emotion}")
            print(f"Mode     : {mode}")

            print("\nHistory:")
            for i, msg in enumerate(history, start=1):
                print(f"{i}. {msg}")

            print("\nContext:")
            print(context_text)

            print("=" * 60)

        # -----------------------------
        # Lucy Response
        # -----------------------------
        print("\nLucy:")
        print(response)

        if follow_up:
            print()
            print(follow_up)
            


      