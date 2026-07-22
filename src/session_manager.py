import json
from pathlib import Path
from datetime import datetime
import uuid


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

        now = datetime.now().isoformat()

        self.session = {
            "session_id" : str(uuid.uuid4()),
            "created_at" : now,
            "last_activity" : now,
            "messages" : []
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


if __name__ == "__main__":

    session = SessionManager()
    session.load_session()
    
    session.create_session()

    session.save_session()

    print("\nCurrent Session:")
    print(json.dumps(session.session, indent=4))