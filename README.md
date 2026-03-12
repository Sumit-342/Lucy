# Lucy – Personal Emotion Detection AI

Lucy is a personal AI assistant project built using Python and Machine Learning.
The goal of Lucy is to understand human emotions from text and eventually become a more intelligent emotional AI assistant.

This project is being developed step-by-step, with each version improving Lucy's ability to understand emotions.

---

## Version v0.01

This was the first working version of Lucy.

Features:

- Detects basic emotions from text:
  - Happy
  - Sad
  - Angry

Model:

- TF-IDF Vectorizer
- Logistic Regression

Execution:

- Terminal-based emotion prediction

---

## Version v0.02

This version improves Lucy’s emotion detection and machine learning pipeline.

New Improvements:

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

Final Model:

- TF-IDF Vectorizer
- Logistic Regression (selected based on performance)

Accuracy:

- ~79%

Execution:

- Terminal-based emotion detection

Example:

User Input:

«"Finally I built the second small version of Lucy"»

Lucy Output:

«Detected Emotion: Surprise»

---

## Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy

---

## Future Versions

Lucy will gradually become more intelligent with upcoming features such as:

- Emoji emotion detection
- Text + Emoji emotion fusion
- Emotion-based responses
- Voice interaction
- Emotion-aware UI with calming visuals
- Deep learning models for better understanding

---

## Project Goal

Lucy is designed as a long-term learning project to explore how artificial intelligence can understand and respond to human emotions.