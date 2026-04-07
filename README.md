# Lucy – Personal Emotion Detection AI 🤖💙

Lucy is a personal AI assistant project built using Python and Machine Learning.

The goal of Lucy is to understand human emotions from text and gradually evolve into an intelligent, emotionally aware AI companion.

This project is being developed step-by-step, with each version improving Lucy’s ability to understand emotions, language, and human intent.

---

## 🚀 Version v0.01

The first working version of Lucy.

### Features
- Detects basic emotions from text:
  - Happy  
  - Sad  
  - Angry  

### Model
- TF-IDF Vectorizer  
- Logistic Regression  

### Execution
- Terminal-based emotion prediction  

---

## 🚀 Version v0.02

Improved emotion detection and experimentation with multiple models.

### Improvements
- Added two new emotions:
  - Love  
  - Surprise  
- Performed Exploratory Data Analysis (EDA)  
- Cleaned dataset and removed duplicates  
- Implemented Train-Test Split  
- Tested multiple models:
  - Logistic Regression  
  - Naive Bayes  
  - Support Vector Machine (SVM)  

### Final Model
- TF-IDF Vectorizer  
- Logistic Regression  

### Accuracy
- ~79%

### Execution
- Terminal-based emotion detection  

---

## 🚀 Version v0.03

Introduced a structured machine learning pipeline.

### Improvements
- Implemented Scikit-learn Pipeline  
- Used GridSearchCV for hyperparameter tuning  
- Combined TF-IDF and model into a single pipeline  
- Added confidence score for predictions  
- Improved project structure  

### Supported Emotions
- Angry  
- Happy  
- Sad  
- Love  
- Surprise  
- Hate  
- Enthusiasm  

### Model Architecture
- TF-IDF Vectorizer  
- Logistic Regression  
- Scikit-learn Pipeline  
- GridSearchCV  

### Accuracy
- ~79%

---

## 🚀 Version v0.1 (Hinglish Breakthrough) 🔥

A major milestone in Lucy’s journey.

Lucy can now understand Hinglish (Hindi + English mixed language), making it more natural and relatable for real-world conversations.

### Key Improvements
- Combined multiple datasets:
  - English dataset  
  - AI-generated Hinglish dataset  
  - Real Hinglish dataset (Kaggle)  
- Built a unified emotion mapping system  
- Cleaned and standardized multi-source data  
- Handled inconsistent labels  
- Created a custom 7-emotion classification system  

### Supported Emotions
- Happy  
- Sad  
- Angry  
- Love  
- Surprise  
- Hate  
- Enthusiasm  

### Model
- TF-IDF Vectorizer  
- Logistic Regression  
- SVM (tested)  
- Scikit-learn Pipeline  

### Accuracy
- ~73%

### Notes
- Hinglish understanding is complex and evolving  
- Accuracy dropped slightly due to real-world complexity  

---

## 🚀 Version v0.2 (Fusion Intelligence) 🧠🔥

This version introduces multi-source emotion understanding, making Lucy smarter and more reliable.

Lucy no longer depends on just text — it now understands emotions from both text and emojis and combines them intelligently.

---

### 🚀 Key Features
- Hinglish Text Emotion Detection  
- Emoji Emotion Detection 😄😢😂  
- Fusion Logic System  

---

### 🧠 Fusion Modes
- `text_only` → when no emoji present  
- `text_strong` → when text confidence is high  
- `emoji_strong` → when emoji clearly dominates  
- `text_emoji_agree` → when both agree  
- `emoji_priority` → when emoji overrides text  

---

### ⚙️ Model Architecture
- TF-IDF Vectorizer  
- Logistic Regression  
- Scikit-learn Pipeline  
- Confidence-based decision system  
- Rule-based fusion layer  

---

### 🎯 Improvements
- Better real-world emotion detection  
- Handles mixed signals (text + emoji)  
- More human-like interpretation  
- Introduced decision-level intelligence (not just prediction)  

---

### ⚠️ Limitations
- Cannot fully understand sarcasm  
- No conversation context yet  
- Emoji meaning can sometimes mislead  
- Confidence ≠ always correct  

---

🚀 Version v0.4 (Context & Memory Engine) 🧠💬

This version introduces short-term memory and context-aware emotion detection, making Lucy more conversational and closer to real human understanding.

Lucy no longer analyzes just a single message — it now considers recent conversation history to interpret emotions more accurately.

---

🚀 Key Features

- Short-term memory (last 3 messages)
- Context-based emotion analysis
- Improved real-world conversation handling
- More human-like emotional understanding

---

🧠 How It Works

- Stores last 3 user messages
- Combines them into a single context input
- Sends context to the existing ML pipeline
- Applies fusion logic on contextual input

---

⚙️ System Design

- Memory Layer → stores conversation history
- Context Builder → merges recent messages
- Existing ML Pipeline (unchanged)
- Emoji + Text Fusion System

---

🎯 Improvements

- Handles emotional transitions (sad → recovery)
- Better interpretation of mixed emotions
- Reduces wrong predictions from single messages
- More realistic behavior compared to isolated predictions

---

⚠️ Limitations

- Model not trained specifically on contextual data
- Hinglish phrases still limited
- Emoji meaning can vary based on context
- Cannot fully detect sarcasm yet

---

🧠 Key Insight

This version improves the system, not the model.

Instead of retraining, Lucy now processes smarter input — making it more effective without changing the underlying ML model.

---

## 🛠️ Technologies Used
- Python  
- Scikit-learn  
- Pandas  
- NumPy  
- Joblib  

---

## 📁 Project Structure
Lucy/
│
├── models/
│ └── lucy_pipeline_v0_2.pkl
│
├── src/
│ └── lucy_core.py
│
└── README.md

---


## 🌱 Future Roadmap

Lucy will continue evolving into a more human-like emotional AI.

### Planned Improvements
- Improved contextual understanding (long -term memory planned) 🧠  
- Emotion-aware responses  
- Voice interaction (calm, human-like voice)  
- Emotion-based UI (rain, nature, mood visuals)  
- Advanced ML / Deep Learning models  
- Personalization & memory system  

---

## 🎯 Project Vision

Lucy is not just a machine learning project.

It is an attempt to build an AI that:
- Understands emotions  
- Responds with empathy  
- Feels natural to talk to  

The long-term vision is to create a personal AI companion that understands not just words, but the emotions behind them.

---

## 💬 Final Note

Lucy is still learning.  
And so is the developer. 😄  

But with each version…  
it’s getting closer to feeling human. 🤍