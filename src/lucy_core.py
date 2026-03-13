import joblib


model = joblib.load("models/lucy_pipeline_v0_03.pkl")



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

        emotion , probs = predict_emotion(user_input)

        print("Detected Emotion : ", emotion)
        print(f"Confidence : {max(probs):.2f}")