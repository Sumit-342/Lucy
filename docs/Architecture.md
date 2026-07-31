# Lucy Architecture Principles

## Design Philosophy

Lucy is built incrementally.

The rule is simple:

Design first. Code second.

Before implementing any feature, the behavior and responsibility of that feature must be clearly defined.

---

# Engineering Principles

## 1. One Name. One Responsibility.

Every function, class, and component should have one clear responsibility.

Example:

create_session()
→ Only creates a session.

save_session()
→ Only saves a session.

load_session()
→ Only loads a session.

No hidden behavior.

---

## 2. Components Should Be Independent

Each component should know only what it needs to know.

Example:

SessionManager knows:
- Session data
- Session lifecycle
- Session storage

SessionManager does NOT know:
- Gemini
- Groq
- Emotions
- Memory
- Personality

---

## 3. Lucy Core Is The Orchestrator

Lucy Core decides the flow.

Individual components perform their specific tasks.

Example:

Lucy Core decides:
"Should we continue this session?"

SessionManager only provides:
"The session status is ACTIVE."

---

# Session Architecture

## Purpose

Session memory exists to continue conversations naturally.

It is NOT long-term memory.

Session memory answers:

"What were we talking about?"

Long-term memory answers:

"Who is this person?"

---

# Session Rules

## Single Active Session

Lucy maintains only one active session.

There will never be multiple active session files.

Current design:

data/
└── session.json

---

## Session Lifecycle

1. User sends a message.

2. Lucy checks if an active session exists.

3. If no session exists:
   - Create a new session.

4. If a session exists:
   - Check if it is still active.

5. If expired:
   - Remove old session.
   - Create a new session.

---

# Session States

Current session states:

NO_SESSION

ACTIVE

EXPIRED

---

# Current Session Structure

Example:

{
    "session_id": "",
    "created_at": "",
    "last_activity": "",
    "messages": []
}


---
# Lazy AI Principle

Lucy performs expensive AI operations only when they are required to answer the current user message. This minimizes latency, reduces API usage, and keeps the system efficient.

---
# 📜 Incremental Summary Principle
A summary is never regenerated from the beginning. Once a summary exists, it is only refreshed using the existing summary plus the messages that have not yet been summarized.