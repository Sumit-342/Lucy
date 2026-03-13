# Lucy – Personal Emotion Detection AI

Lucy is a personal AI assistant project built using Python and Machine Learning.
The goal of Lucy is to understand human emotions from text and eventually evolve into an intelligent emotional AI assistant.

This project is being developed step-by-step, with each version improving Lucy’s ability to understand emotions and interact with users.

---

## Version v0.01

This was the first working version of Lucy.

Features

- Detects basic emotions from text:
  - Happy
  - Sad
  - Angry

Model

- TF-IDF Vectorizer
- Logistic Regression

Execution

- Terminal-based emotion prediction

---

## Version v0.02

This version improved Lucy’s emotion detection pipeline.

Improvements

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

Final Model

- TF-IDF Vectorizer
- Logistic Regression (selected based on performance)

Accuracy

- ~79%

Execution

- Terminal-based emotion detection

Example:

User Input:

"Finally I built the second small version of Lucy"

Lucy Output:

Detected Emotion: Surprise

---

## Version v0.03

This version introduces a more structured machine learning pipeline and improves Lucy’s prediction system.

New Improvements

- Implemented Scikit-learn Pipeline
- Used GridSearchCV for hyperparameter tuning
- Combined TF-IDF vectorizer and model into a single pipeline
- Added confidence score for predictions
- Improved project structure

Supported Emotions

Lucy can now detect 7 emotions:

- Angry
- Happy
- Sad
- Love
- Surprise
- Hate
- Enthusiasm

Model Architecture

- TF-IDF Vectorizer
- Logistic Regression
- Scikit-learn Pipeline
- GridSearchCV for parameter optimization

Accuracy

- ~79%

Execution

Lucy runs in the terminal and continuously accepts user input.

Example:

User Input:

"I am extremely excited to start this amazing project tomorrow!"

Lucy Output:

Detected Emotion: Enthusiasm
Confidence: 0.98

---

## Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## Project Structure

Lucy/
│
├── models/
│   └── lucy_pipeline_v0_03.pkl
│
├── src/
│   └── lucy_core.py
│
└── README.md

---

## Future Versions

Lucy will gradually evolve into a more intelligent emotional AI assistant.

Planned improvements include:

- Emoji emotion detection
- Text + Emoji emotion fusion
- Emotion-based responses
- Voice interaction
- Emotion-aware UI with calming visuals (rain, nature, etc.)
- More advanced machine learning / deep learning models

---

## Project Goal

Lucy is designed as a long-term learning project to explore how artificial intelligence can understand and respond to human emotions.

This project focuses on gradually building an AI assistant that can detect emotions, respond empathetically, and eventually interact with users in a more human-like way.