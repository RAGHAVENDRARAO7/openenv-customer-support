import json
import os

class Task:
    def __init__(self, data):
        self.id = data["id"]
        self.type = data["type"]
        self.ticket = data["ticket"]
        self.expected = data["expected"]
        self.steps_completed = 0
        self.resolved = False

    def initial_observation(self):
        return {
            "ticket_id": self.id,
            "customer_message": self.ticket,
            "history": [],
            "metadata": {"type": self.type}
        }
@app.get("/health")
def health():
    return {"status": "ok"}

def next_observation(self, action):
    return {
        "ticket_id": self.id,
        "customer_message": self.ticket,
        "history": [str(action)],  # must be string
        "metadata": {"type": self.type}
    }

def load_tasks():
    path = os.path.join("data", "tickets.json")
    with open(path) as f:
        raw = json.load(f)
    return [Task(t) for t in raw]
