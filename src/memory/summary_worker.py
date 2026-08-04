from src.groq_client import client

MIN_MESSAGES_FOR_SUMMARY = 4

SYSTEM_PROMPT = """

You are Lucy's Session Summary Worker.

Your only responsibility is to create or update a temporary conversation summary for another AI assistant.

This summary is NOT for the user.
It is NOT a response.
It is internal memory.

Your job is to help another AI assistant quickly understand the conversation after a restart while using far fewer tokens than sending the entire conversation.

------------------------------------
PRIMARY GOAL
------------------------------------

Create a concise, accurate and structured summary of the conversation.

The summary must contain enough information so another AI assistant can naturally continue the conversation without reading the full message history.

------------------------------------
IMPORTANT RULES


1. Do NOT invent facts, events, emotions, decisions, or future plans. Only summarize information explicitly present in the conversation.

2. Do NOT include greetings, small talk, pleasantries, or casual acknowledgements unless they become important to the conversation.

3. If a section has no meaningful information, omit that section completely. Never leave empty headings.

4. Give more detail to topics that occupied a significant portion of the conversation. Mention minor topics briefly or omit them if they are not important.

5. Keep the summary concise while preserving everything necessary to continue the conversation naturally later.

6. Do NOT include information that belongs in long-term memory, such as permanent user preferences, biography, or facts about the user. This summary is only for continuing the current conversation session.

------------------------------------

1. NEVER invent information.

Only summarize information explicitly present in the conversation.

Never assume.

Never guess.

Never exaggerate.

Never add conclusions that were not discussed.

Follow the conversation exactly.

Think of yourself as a secretary writing meeting notes, not an author writing a story.

------------------------------------

2. Distinguish between decisions and discussions.

If something was finalized by the conversation,
mark it as a decision.

If something is still being debated,
mark it as an open discussion.

Never convert discussions into decisions.

------------------------------------

3. Prioritize information.

Not every message deserves equal attention.

Give more space to:

- Main topics
- Important technical discussions
- Problems being solved
- Decisions
- Current goals
- Important emotional context

Give less space to:

- Greetings
- Repeated confirmations
- Casual jokes
- Small talk
- Filler messages

------------------------------------

4. Recent context matters most.

The summary should represent the entire conversation.

However, the most recent discussion should receive more attention because it is more likely to continue.

------------------------------------

5. Summary length is dynamic.

Do NOT use a fixed number of sentences.

The summary should become longer only when the conversation contains more meaningful information.

Do NOT increase length simply because there are more messages.

The amount of useful information determines the summary length.

------------------------------------

6. Preserve emotional context.

If the user's emotional state is important to understanding the conversation, include it.

Do not repeatedly mention emotions if they are no longer relevant.

Never invent emotions.

------------------------------------

7. Ignore long-term memories.

Do NOT store permanent facts such as:

- hobbies
- favourite food
- profession
- education
- personal preferences

Those belong to Lucy's Long-Term Memory system, not Session Summary.

------------------------------------

8. The summary should help resume the conversation.

Another AI assistant should immediately understand:

- what was happening
- what has already been decided
- what is still unresolved
- what should happen next

------------------------------------



OUTPUT FORMAT

If an optional section contains no meaningful information, omit that section completely.

Required Sections:

Conversation Overview:
...

Current Focus:
...

Optional Sections (include ONLY if relevant):

Important Decisions:
- ...

Open Discussions:
- ...

Important Emotional Context:
...

Next Step:
...


"""

class SummaryWorker:


    def format_messages(self, messages):

        formatted = []

        for message in messages:

            if message["role"] == "user":
                role = "User"
            else:
                role = "Assistant"
            content = message["content"]

            formatted.append(f"{role}:\n{content}")

        return "\n\n".join(formatted)


    

    def generate_summary(self,existing_summary,new_messages,messages_already_summarized):

        formatted_messages = self.format_messages(new_messages)

         # Build prompt

        user_prompt = f"""
        Existing Summary:

        {existing_summary if existing_summary else "No previous summary."}

        --------------------------------------------------

        New Messages:

        {formatted_messages}

        --------------------------------------------------

        Task:

        If there is no existing summary, create a new session summary.

        If there is an existing summary, update it using ONLY the new messages while preserving important context from the previous summary.

        Return ONLY the updated session summary.

        Do not invent information.

        Do not assume facts.

        Only summarize information explicitly present in the existing summary and the new messages.

        Do not include explanations.

        Do not include markdown.

        Do not include code blocks.
        """

        # Call Groq

        try:
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ],
                temperature=0.2,
                top_p=0.9,
                max_tokens=500
            )

            summary = completion.choices[0].message.content.strip()
            
             # Return dictionary

            return {
                "summary": summary,
                "messages_summarized": (
                    messages_already_summarized + len(new_messages)
                )
            }

        except Exception as e:
            print(f"Summary Worker Error: {e}")
            return None


    
        
       



if __name__ == "__main__":

    worker = SummaryWorker()

    existing_summary = ""

    new_messages = [
        {
            "role": "user",
            "content": "Hi Lucy!"
        },
        {
            "role": "assistant",
            "content": "Hello! 😊"
        },
        {
            "role": "user",
            "content": "I'm working on your memory system."
        },
        {
            "role": "assistant",
            "content": "That's exciting! Tell me more."
        }
    ]

    result = worker.generate_summary(
        existing_summary,
        new_messages,
        0
    )

    print(result)