import joblib


model = joblib.load("models/lucy_model_v0_02.pkl")
vectorizer = joblib.load("models/lucy_vectorizer_v0_02.pkl")


def predict_emotion (text) :
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)

    return prediction[0]



if __name__ == "__main__":
    
    user_input = input("You: ")
    
    emotion = predict_emotion(user_input)

    print("Detected Emotion : ", emotion)