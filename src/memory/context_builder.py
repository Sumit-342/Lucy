import json

class ContextBuilder:

    def build_context(
        self,
        session_summary,
        conversation_history,
        current_message
    ):
        """
        Build the conversation context that will be
        sent to the LLM.
        """

        return {
            "session_summary": session_summary,
            "conversation_history": conversation_history,
            "current_message": current_message
        }



# Testing

if __name__ == "__main__":

    builder = ContextBuilder()

    context = builder.build_context(
        session_summary="User was working on Lucy memory.",
        conversation_history=[
            {
                "role": "user",
                "content": "Let's continue."
            },
            {
                "role": "assistant",
                "content": "Sure!"
            }
        ],
        current_message="Where were we?"
    )

    print(json.dumps(context,indent = 4))