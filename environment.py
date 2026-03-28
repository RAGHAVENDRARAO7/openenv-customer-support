import random
from .tasks import load_tasks
from .rewards import compute_reward
from .models import Action

class CustomerSupportEnv:
    def __init__(self):
        self.tasks = load_tasks()
        self.current_task = None
        self.state_data = {}
   def reset(self):
      self.current_task = random.choice(self.tasks)
      self.state_data = {"steps": 0}

    obs = self.current_task.initial_observation()
    return Observation(**obs).dict()

    def step(self, action_dict):
        action = Action(**action_dict)
        self.state_data["steps"] += 1
        reward = compute_reward(self.current_task, action)
        done = self._is_done(action)
        obs = self.current_task.next_observation(action_dict)
        return obs, reward.dict(), done, {"state": self.state_data}

    def state(self):
        return self.state_data

    def _is_done(self, action):
        if self.state_data["steps"] >= 5:
            return True
        if action.action_type == "reply" and action.content:
            if "resolved" in action.content.lower():
                return True
        return False
