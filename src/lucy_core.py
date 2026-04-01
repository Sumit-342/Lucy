import joblib
import emoji
from collections import Counter
import pandas as pd

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
    
    return Counter(emotions).most_common(1)[0][0]


def get_text_emotion(text):                         # text emotion function
    prediction = model.predict([text])[0]
    probabilities = model.predict_proba([text])[0]
    confidence = max(probabilities)

    return prediction , confidence


def predict_final(text):                                        # text + emoji fusion
    text_emotion , text_confidence = get_text_emotion(text)
    emoji_emotion = get_emoji_emotion(text)

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

def analyze(text):                                      # output wrapper
    emotion , confidence , mode = predict_final(text)

    return {
        "emotion":emotion,
        "confidence":round(float(confidence),2),
        "mode":mode
    }

# def clean_text(text):
#     text = str(text)
#     text = re.sub(r'[\U00010000-\U0010ffff]', '', text)  # remove emojis
#     text = re.sub(r'[^\x00-\x7F]+', '', text)            # remove broken chars
#     return text.lower()


# def predict_emotion (text) :
#     prediction = model.predict([text])
#     probabilities = model.predict_proba([text])
#     return prediction[0],probabilities[0]



if __name__ == "__main__":
    
    while True :
        user_input = input("You: ")
        if user_input.lower() == "exit" :
            print("Lucy: Goodbye 👋👋")
            break

        if not user_input.strip():  
            print("Lucy: Please say something")
            continue

        result = analyze(user_input)

        print(f"\nLucy: ")
        print(f"Emotion   : {result['emotion']}")
        print(f"Confidence: {result['confidence']}")
        print(f"Mode      : {result['mode']}")

      