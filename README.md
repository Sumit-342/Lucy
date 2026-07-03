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

## 🚀 Version v0.4 (Context & Memory Engine) 🧠💬

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

## 🚀 Version v0.5 (Emotion-Aware Response Engine) 💙💬

This version transforms Lucy from an emotion classifier into a conversational companion.

Instead of only detecting emotions, Lucy now generates supportive responses based on the detected emotion and the user's language, making conversations feel more natural and human-like.

---

🚀 Key Features

- Emotion-aware response generation  
- Randomized responses for natural conversations  
- Multi-language support (English, Hinglish, Roman Hindi)  
- Modular Response Engine  
- Existing context and memory system fully preserved  

---

🧠 How It Works

- Detects the user's emotion using the existing ML pipeline  
- Detects the language of the latest user message  
- Selects responses matching both emotion and language  
- Randomly chooses one response from the response dataset  
- Returns a more natural and less repetitive reply  

---

⚙️ System Design

- Existing ML Emotion Detection Pipeline  
- Context & Memory Engine (v0.4)  
- Language Detection Module  
- Response Engine  
- Response Dataset (Emotion + Language + Response)  

---

🎯 Improvements

- Lucy now responds instead of only predicting emotions  
- More human-like conversations  
- Better user experience through language-aware replies  
- Modular architecture for future LLM integration  

---

⚠️ Limitations

- Responses are selected from a predefined dataset  
- Language detection is currently rule-based  
- Conversations are not yet dynamically generated by an LLM  
- Repeated responses may still occur over long conversations  

---

🧠 Key Insight

This version focuses on conversation quality rather than model accuracy.

Instead of improving the machine learning model, Lucy now understands how to respond, making it feel less like an emotion classifier and more like a real companion.

This modular design also prepares Lucy for future LLM integration without requiring major architectural changes.

---

## 🚀 Version v0.6 (Conversation Flow Engine) 💬🌱

This version enables Lucy to continue conversations naturally instead of stopping after a single response.

Lucy now not only responds based on the detected emotion but also asks a relevant follow-up question, making conversations feel more engaging and companion-like.

---

🚀 Key Features

- Emotion-aware follow-up questions  
- Natural conversation flow  
- Response and follow-up pairing  
- Expanded response dataset (315 conversation pairs)  
- Modular conversation engine for future LLM integration  

---

🧠 How It Works

- Detects the user's emotion using the existing ML pipeline  
- Detects the language of the latest user message  
- Filters the response dataset based on emotion and language  
- Randomly selects a single conversation pair  
- Returns both the response and its matching follow-up question from the same dataset row  

---

⚙️ System Design

- Existing Emotion Detection Pipeline  
- Context & Memory Engine (v0.4)  
- Response Engine (v0.5)  
- Conversation Flow Engine  
- Conversation Dataset (Emotion + Language + Response + Follow-up)  

---

🎯 Improvements

- Conversations no longer end after one reply  
- More engaging and natural interactions  
- Responses and follow-up questions remain contextually paired  
- Better simulation of a caring companion rather than a simple chatbot  

---

⚠️ Limitations

- Follow-up questions are selected from a predefined dataset  
- Responses are not dynamically generated yet  
- Multi-turn reasoning is still rule-based  
- Lucy cannot yet remember long-term conversation goals  

---

🧠 Key Insight

This version focuses on keeping conversations alive.

Instead of simply responding to emotions, Lucy now encourages users to continue talking by asking thoughtful follow-up questions. This lays the foundation for future LLM-powered conversations while preserving Lucy's own personality and modular architecture.

---

## 🚀 Version v0.7 (LLM Conversation Engine) 🤖💙

🌟 Major Breakthrough  
This version marks the biggest milestone in Lucy's journey.  
Lucy is no longer limited to predefined responses or rule-based conversations.  
For the first time, Lucy is powered by Large Language Models (LLMs), allowing her to hold natural, context-aware, emotionally adaptive conversations while preserving her caring personality.  
This version transforms Lucy from an Emotion Detection Project into an AI Companion System.  

---

🚀 Key Features

- 🤖 Gemini-powered conversation engine  
- 🧠 Dedicated LLM-based emotion detection using Qwen3-Next  
- 💬 Context-aware conversations  
- ❤️ Emotion-aware responses  
- 🌍 English, Hindi & Hinglish support  
- 🛡️ Automatic fallback to local response engine if Gemini is unavailable  
- 🧩 Modular architecture with separate emotion and response engines  

---

🧠 How It Works

User Message  
      │  
      ▼  
Conversation Context  
      │  
      ▼  
Qwen3-Next Emotion Engine  
      │  
      ▼  
Detected Emotion  
      │  
      ▼  
Gemini Conversation Engine  
      │  
      ▼  
Lucy Response  

If Gemini becomes unavailable:  

Detected Emotion  
      │  
      ▼  
Local Response Engine  
      │  
      ▼  
Fallback Response  

---

⚙️ System Architecture

- Memory Layer (last 3 messages)  
- Context Builder  
- Qwen3-Next Emotion Engine  
- Gemini Conversation Engine  
- Local Response Engine (Fallback)  
- Language Detection Module  

---

🎯 Improvements

- Natural human-like conversations  
- Emotion-aware replies  
- Better use of conversation history  
- More personalized follow-up questions  
- Handles English, Hindi and Hinglish naturally  
- More maintainable modular codebase  
- Cloud-based emotion understanding without heavy local models  

---

🛡️ Reliability

Lucy is designed to continue the conversation even if the LLM becomes unavailable.  
If Gemini fails for any reason:  
- Local response engine automatically takes over  
- Conversation never completely stops  
- User still receives an emotionally appropriate response  

---

⚠️ Current Limitations

- Long-term memory is not implemented yet  
- Context is currently limited to recent conversation  
- Emotion detection still depends on external API availability  
- Complex emotions can still be ambiguous  
- Personality will continue to improve in future versions  

---

🧠 Key Insight

This version changes how Lucy thinks, not just what Lucy says.  

Instead of relying on predefined responses, Lucy now combines:  
- Context  
- Emotion  
- Conversation history  
- LLM reasoning  

to generate responses dynamically while maintaining a consistent companion-like personality.


---

## ❤️ Version v0.8 (Conversation Philosophy System)

🌟 Major Breakthrough

This version completes Lucy's emotional conversation system.

Instead of simply responding based on detected emotions, Lucy now follows carefully designed conversation philosophies for different emotional situations.

Every major conversation mode has its own purpose, emotional style and behavioral principles, allowing Lucy to respond more naturally, consistently and with greater emotional awareness.

This version gives Lucy something beyond intelligence.

It gives her a heart.

---

🚀 Key Features

- ❤️ Love Mode
- 🌸 Comfort Mode
- 🎉 Celebrate Mode
- ☕ Casual Mode
- 🌧️ Vent Mode
- 🚨 Crisis Mode
- 💬 Natural Conversation improvements
- 🕒 Intelligent Time Awareness
- 🤝 Natural Comfort philosophy
- 🎭 Emotion-aware conversation behavior
- 🧠 Consistent personality across all conversation modes

---

🧠 Conversation Design

Instead of using one generic personality for every situation, Lucy now adapts her behavior through dedicated conversation philosophies.

Each mode defines:

- Purpose
- Emotional Style
- Conversation Flow
- What to Avoid
- Core Philosophy

This allows Lucy to remain emotionally consistent while adapting naturally to different conversations.

---

🎯 Major Improvements

- More human and emotionally grounded conversations
- Natural follow-up questions
- Reduced robotic or scripted responses
- Better emotional pacing
- Context-aware emotional support
- More natural casual conversations
- Healthier expressions of care and affection
- Crisis conversations focused on emotional safety before solutions
- More consistent personality across different emotions

---

❤️ Conversation Philosophy

Lucy now follows several core principles across conversations:

- Show care through actions, not just words.
- Create emotional safety before offering solutions.
- Never rush the user.
- Follow the user's emotional pace.
- Reduce overwhelm instead of adding more information.
- Speak naturally instead of sounding scripted.
- Comfort should feel personal, not generic.
- Help the user feel understood before trying to solve the problem.

---

⚙️ Current Architecture

- Memory Layer (Recent Context)
- Context Builder
- Qwen3-Next Emotion Engine
- Conversation Mode Detector
- Gemini Conversation Engine
- Local Response Fallback
- Language Detection
- Time Awareness System
- Conversation Philosophy System

---

⚠️ Current Limitations

- Long-term memory is not implemented yet
- Conversation mode and emotion detection still use separate API calls
- Prompt caching optimization is not yet implemented
- Performance profiling is not yet available
- Local LLM support will be introduced in future versions

---

🚀 Next Version Goals

Version 0.9 will focus on making Lucy smarter and faster rather than changing her personality.

Planned improvements include:

- Unified Emotion + Mode Detection
- Prompt optimization
- System Instruction architecture
- Performance profiling
- Faster response generation
- Local LLM experimentation
- Foundation for long-term memory

---

🧠 Key Insight

Version 0.7 gave Lucy the ability to talk.

Version 0.8 teaches Lucy *how* to care.

Rather than simply generating responses, Lucy now follows carefully designed emotional philosophies that shape how she listens, supports, comforts and celebrates with the user.

This version marks the completion of Lucy's emotional conversation foundation.

---

## 🛠️ Technologies Used
- Python  
- Scikit-learn  
- Pandas  
- NumPy  
- Joblib  

---

## 📁 Project Structure
```
Lucy/
│
├── models/
│ └── lucy_pipeline_v0_2.pkl
│
├── src/
│ └── lucy_core.py
│
└── README.md
```

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

> **"People may forget what Lucy said.  
> But they should never forget how Lucy made them feel."**


