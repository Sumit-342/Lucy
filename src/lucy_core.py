import joblib
import re

model = joblib.load("models/lucy_pipeline_v0_1.pkl")



def clean_text(text):
    text = str(text)
    text = re.sub(r'[\U00010000-\U0010ffff]', '', text)  # remove emojis
    text = re.sub(r'[^\x00-\x7F]+', '', text)            # remove broken chars
    return text.lower()


def predict_emotion (text) :
    prediction = model.predict([text])
    probabilities = model.predict_proba([text])
    return prediction[0],probabilities[0]



if __name__ == "__main__":
    
    while True :
        user_input = input("You: ")
        if user_input.lower() == "exit" :
            print("Lucy: Goodbye 👋👋")
            break

        if not user_input.strip():  
            print("Lucy: Please say something")
            continue

        emotion , probs = predict_emotion(user_input)

        print("Detected Emotion : ", emotion)
        print(f"Confidence : {max(probs):.2f}")