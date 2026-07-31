import json
import os
from datetime import datetime


class SummaryManager:

    def __init__(self, file_path="data/session_summary.json"):
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            self.create_summary()


    def create_summary(self):
        summary_data = {
            "summary": "",
            "updated_at": "",
            "messages_summarized": 0
        }

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(summary_data, file, indent=4)


    def load_summary(self):

        if not os.path.exists(self.file_path):
            self.create_summary()

        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)


    def save_summary(self, summary_data):

        summary_data["updated_at"] = datetime.now().isoformat()

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(summary_data, file, indent=4)


    def clear_summary(self):
        self.create_summary()


    def get_summary(self):
        data = self.load_summary()
        return data["summary"]


# Testing


if __name__ == "__main__":
    
    manager = SummaryManager()

print(manager.load_summary())

print(manager.get_summary())

manager.save_summary({
    "summary": "Lucy and the user discussed SummaryWorker.",
    "messages_summarized": 10
})

print(manager.load_summary())

manager.clear_summary()

print(manager.load_summary())