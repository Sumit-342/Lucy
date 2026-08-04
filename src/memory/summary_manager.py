import json
import os
from datetime import datetime,timedelta


class SummaryStatus:
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    EMPTY = "EMPTY"


class SummaryManager:

    def __init__(self, file_path="data/session_summary.json"):
        self.file_path = file_path
        self.summary = None

        if not os.path.exists(self.file_path):
            self.create_summary()


    def create_summary(self):
        summary_data = {
            "summary": "",
            "updated_at": "",
            "expires_at":"",
            "messages_summarized": 0
        }

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(summary_data, file, indent=4)


    def load_summary(self):

        if not os.path.exists(self.file_path):
            self.create_summary()

        with open(self.file_path, "r", encoding="utf-8") as file:
            self.summary = json.load(file)


    def get_summary(self):
        """
        Return the currently loaded summary.
        """

        return self.summary

    
    def save_summary(self, summary_data):

        current_time = datetime.now()

        summary_data["updated_at"] = current_time.isoformat()

        summary_data["expires_at"] = (
            current_time + timedelta(hours=8)
        ).isoformat()

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(summary_data, file, indent=4)

        self.summary = summary_data


    def clear_summary(self):
        self.create_summary()
        self.load_summary()


    def get_summary_status(self):
        """
        Check the current state of the summary.
        """

        if self.summary is None:
            return SummaryStatus.EMPTY

        # If no summary exists yet
        if not self.summary["summary"]:
            return SummaryStatus.EMPTY

        expires_at = self.summary.get("expires_at")

        # Older summaries won't have expires_at
        if not expires_at:
            return SummaryStatus.EXPIRED

        expires_at = datetime.fromisoformat(expires_at)
        current_time = datetime.now()

        if current_time > expires_at:
            return SummaryStatus.EXPIRED

        return SummaryStatus.ACTIVE


  


# Testing


# if __name__ == "__main__":
    
#     manager = SummaryManager()

# print(manager.load_summary())

# print(manager.get_summary())

# manager.save_summary({
#     "summary": "Lucy and the user discussed SummaryWorker.",
#     "messages_summarized": 10
# })

# print(manager.load_summary())

# manager.clear_summary()

# print(manager.load_summary())