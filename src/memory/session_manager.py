import json
from pathlib import Path
from datetime import datetime,timedelta
import uuid


class SessionStatus:
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    NO_SESSION = "NO_SESSION"


class SessionManager:

    def __init__(self):
        self.session_file = Path("data/session.json")
        self.session = None

    def load_session(self):
        """
        Load the current session from disk.

        If no session exists, self.session remains None.
        A missing session is a valid state.
        """

        if not self.session_file.exists():
            print("📂 No previous session found.")
            self.session = None
            return

        try:
            with open(self.session_file, "r", encoding="utf-8") as file:
                self.session = json.load(file)

            print("✅ Previous session loaded.")

        except (json.JSONDecodeError, OSError):
            print("⚠️ Previous session is corrupted. Starting fresh.")
            self.session = None


    def create_session(self):
        """
        Create a brand new conversation session.
        """

        timestamp = datetime.now().isoformat()

        self.session = {
            "session_id" : str(uuid.uuid4()),
            "created_at" : timestamp,
            "last_activity" : timestamp,
            "messages" : [],
            "summary_resume_pending": False
        }

        print("✨🌟 New Session created")


    def save_session(self):
        """
        Save the current session to disk.
        """

        if self.session is None:
            print("⚠️ No active session to save.")
            return

        # Create the data folder if it doesn't exist
        self.session_file.parent.mkdir(parents=True, exist_ok=True)

        with open(self.session_file, "w", encoding="utf-8") as file:
            json.dump(
                self.session,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("💾 Session saved.")

    
    def get_session_status(self):
        """
        Check the current state of the session.
        """

        if self.session is None:
            return SessionStatus.NO_SESSION

        last_activity = datetime.fromisoformat(
            self.session["last_activity"]
        )

        current_time = datetime.now()

        time_gap = current_time - last_activity

        if time_gap > timedelta(hours=4):
            return SessionStatus.EXPIRED

        return SessionStatus.ACTIVE


    def get_inactivity_duration(self):
        """
        Return how long it has been since the last session activity.
        """

        if self.session is None:
            return None

        last_activity = datetime.fromisoformat(
            self.session["last_activity"]
        )

        return datetime.now() - last_activity


    def prepare_resume_state(self, resume_threshold):
        """
        Determine whether this startup is a resumed conversation.

        This is checked only once when Lucy starts.
        """

        if self.session is None:
            return

        inactivity = self.get_inactivity_duration()

        if (
            inactivity is not None
            and inactivity >= resume_threshold
        ):
            self.mark_summary_resume_pending()
        else:
            self.clear_summary_resume_pending()


    
    def add_message(self, role, content):
        """
        Add a new message to the current session.
        """

        if self.session is None:
            print("⚠️ No active session found.")
            return

        timestamp = datetime.now().isoformat()

        message = {
            "role": role,
            "content": content,
            "timestamp": timestamp
        }

        self.session["messages"].append(message)

        self.session["last_activity"] = timestamp

        self.save_session()

        print(f"💬 {role.capitalize()} message added to session.")


    def get_unsummarized_messages(self, messages_already_summarized):
        """
        Return only the messages that have not yet been included
        in the session summary.
        """

        if self.session is None:
            return []

        return self.session["messages"][messages_already_summarized:]


    def mark_summary_resume_pending(self):
        """
        Mark that the next message should receive the session summary.
        """

        if self.session is None:
            return

        self.session["summary_resume_pending"] = True
        self.save_session()


    def is_summary_resume_pending(self):
        """
        Check whether the next message should receive the session summary.
        """

        if self.session is None:
            return False

        return self.session.get("summary_resume_pending", False)

    def clear_summary_resume_pending(self):
        """
        Mark that the resume summary has already been sent.
        """

        if self.session is None:
            return

        self.session["summary_resume_pending"] = False
        self.save_session()



# Testing


if __name__ == "__main__":

    session = SessionManager()

    session.load_session()

    if session.get_session_status() != "active":
        session.create_session()

    session.add_message(
        role="user",
        content="Hello Lucy!"
    )

    session.add_message(
        role="assistant",
        content="Hello! How are you?"
    )

    print("\nCurrent Session:")
    print(json.dumps(session.session, indent=4))