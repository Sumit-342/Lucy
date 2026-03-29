# Lucy – Personal Emotion Detection AI 🤖💙

Lucy is a personal AI assistant project built using Python and Machine Learning.
The goal of Lucy is to understand human emotions from text and gradually evolve into an intelligent, emotionally aware AI companion.

This project is being developed step-by-step, with each version improving Lucy’s ability to understand emotions, language, and human intent.

---

## 🚀 Version v0.01

The first working version of Lucy.

Features

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

This is a major milestone in Lucy’s journey.

Lucy can now understand Hinglish (Hindi + English mixed language), making it more natural and relatable for real-world conversations.

### Key Improvements

- Combined multiple datasets:
  - English dataset
  - AI-generated Hinglish dataset
  - Real Hinglish dataset (Kaggle)
- Built a unified emotion mapping system
- Cleaned and standardized multi-source data
- Handled inconsistent labels (e.g., angry vs anger, joy vs happy)
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

- ~73% (Hinglish is more complex, still improving)

## Notes

- Model may produce incorrect predictions in some cases
- Hinglish understanding is still evolving
- This version focuses on capability over perfection

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
│   └── lucy_pipeline_v0_1.pkl
│
├── src/
│   └── lucy_core.py
│
└── README.md

---

## 🌱 Future Roadmap

Lucy will continue evolving into a more human-like emotional AI.

Planned improvements:

- Emoji emotion detection
- Text + Emoji emotion fusion
- Emotion-aware responses
- Voice interaction (calm, human-like voice)
- Emotion-based UI (rain, nature, mood visuals)
- Deep learning / transformer-based models
- Context-aware conversation

---

## 🎯 Project Vision

Lucy is not just a machine learning project.

It is an attempt to build an AI that:

- Understands emotions
- Responds with empathy
- Feels natural to talk to

The long-term vision is to create a personal AI companion that understands not just words, but the emotions behind them.

---

### 💬 Final Note

Lucy is still learning.

And so is the developer. 😄