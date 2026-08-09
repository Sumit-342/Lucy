import joblib
import emoji
import time
from datetime import datetime , timedelta
from collections import Counter
import pandas as pd

from src.response_engine import get_response
from src.language_detector import detect_language
from src.gemini_client import generate_reply
from src.nlu_engine import analyze_message

from src.memory.session_manager import SessionManager, SessionStatus
from src.memory.summary_manager import SummaryManager , SummaryStatus
from src.memory.summary_worker import SummaryWorker




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


def update_history(role, content):

    history.append({
        "role": role,
        "content": content
    })

    if len(history) > 6:
        history.pop(0)


def get_context():

    formatted_history = []

    for message in history:
        role = "User" if message["role"] == "user" else "Lucy"

        formatted_history.append(
            f"{role}: {message['content']}"
        )

    return "\n".join(formatted_history)
    


def analyze(text):                                      # output wrapper
    emotion , confidence , mode = predict_final(text)
    

    return {
        "emotion":emotion,
        "confidence":round(float(confidence),2),
        "mode":mode
    }


DEBUG = True   
MIN_MESSAGE_FOR_SUMMARY = 4
SUMMARY_RESUME_THRESHOLD = timedelta(seconds=30)

session_manager = SessionManager()
summary_worker = SummaryWorker()
summary_manager = SummaryManager()
session_manager.prepare_resume_state(
    SUMMARY_RESUME_THRESHOLD
)

session_manager.load_session()
summary_manager.load_summary()

if session_manager.get_session_status() != SessionStatus.ACTIVE:
    session_manager.create_session()

if summary_manager.get_summary_status() == SummaryStatus.EXPIRED:
    summary_manager.clear_summary()

session_manager.prepare_resume_state(
    SUMMARY_RESUME_THRESHOLD
)

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
        pipeline_start = time.perf_counter()

        update_history(
            role="user",
            content= user_input
        )

        session_manager.add_message(
            role="user",
            content=user_input
        )

        send_summary = (
            session_manager.is_summary_resume_pending()
            and summary_manager.get_summary_status() == SummaryStatus.ACTIVE
        )

        summary_for_gemini = None

        if send_summary :
            summary_for_gemini = summary_manager.get_summary()["summary"]

        print(
            f"🤓 Summary Sent to Gemini : "
            f"{'YES' if summary_for_gemini else 'NO'}"
        )

        context_start = time.perf_counter()
        context_text = get_context()
        context_time = time.perf_counter() - context_start

        # NLU Analysis
        nlu_start = time.perf_counter()
        analysis = analyze_message(context_text)
        emotion = analysis["emotion"]
        mode = analysis["mode"]
        nlu_time = time.perf_counter() - nlu_start

        # mode_start = time.perf_counter()
        # mode = detect_mode(user_input)
        # mode_time = time.perf_counter() - mode_start

        language_start = time.perf_counter()
        language = detect_language(user_input)
        language_time = time.perf_counter() - language_start

        # -----------------------------
        # Response Generation
        # -----------------------------
        try:
            reply_start = time.perf_counter()

            response = generate_reply(
                user_message = user_input,
                emotion=emotion,
                language=language,
                mode=mode,
                context=context_text,
                summary=summary_for_gemini

            )

            if summary_for_gemini is not None:
                session_manager.clear_summary_resume_pending()

            reply_time = time.perf_counter() - reply_start

            follow_up = None

        except Exception as e:
            print(f"\nGemini Error: {e}")
            print("Gemini unavailable. Using Local Fallback...\n")

            reply_time = 0.0

            response, follow_up = get_response(
                emotion,
                language
            )

        total_time = time.perf_counter() - pipeline_start
        # -----------------------------
        # Debug Information
        # -----------------------------
        if DEBUG:

            print("\n" + "=" * 60)
            print("                     LUCY DEBUG")
            

            print(f"Language : {language}")
            print(f"Emotion  : {emotion}")
            print(f"Conversation Mode     : {mode}")

            print("\nHistory:")
            for i, msg in enumerate(history, start=1):
                print(f"{i}. {msg}")

            print("\nContext:")
            print(context_text)

            print("\n" + "=" * 60)
            print("                  PERFORMANCE")
            print("=" * 60)

            print(f"Context Build      : {context_time:.2f} s")
            # print(f"Emotion Detection  : {emotion_time:.2f} s")
            # print(f"Mode Detection     : {mode_time:.2f} s")
            print(f"NLU Analysis     : {nlu_time: .2f}s")
            print(f"Language Detection : {language_time:.2f} s")
            print(f"Gemini Reply       : {reply_time:.2f} s")

            print("-" * 60)
            print(f"Total Time         : {total_time:.2f} s")
            print("=" * 60)

            print("=" * 60)

        # -----------------------------
        # Lucy Response
        # -----------------------------

        update_history(
            role="assistant",
            content=response
        )

        session_manager.add_message(
            role="assistant",
            content=response
        )

        print("\nLucy:")
        print(response)

        if follow_up:
            print()
            print(follow_up)

       # ------------------------------------
        #        Summary Trigger check
        # ------------------------------------
        summary = summary_manager.get_summary()

        new_messages = session_manager.get_unsummarized_messages(
            summary["messages_summarized"]
        )

        if len(new_messages) >= MIN_MESSAGE_FOR_SUMMARY:
            existing_summary = summary["summary"]

            updated_summary = summary_worker.generate_summary(
                existing_summary=existing_summary,
                new_messages=new_messages,
                messages_already_summarized=summary["messages_summarized"]
            )

            if updated_summary is not None:
                summary_manager.save_summary(updated_summary)
                summary_manager.load_summary()

                print("\n🧠 Session Summary Updated!")

            else:
                print("\n❌ Summary Generation Failed")
        else:
            print("\n📄 Summary Not Required")
            


      