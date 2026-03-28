from .graders import grade_classification, grade_response, grade_multistep
from .models import Reward

def compute_reward(task, action):
    if task.type == "classification":
        score = grade_classification(action.category, task.expected)
        return Reward(score=score, feedback="classification evaluated")
    elif task.type == "response":
        score = grade_response(action.content)
        return Reward(score=score, feedback="response evaluated")
    elif task.type == "multi":
        task.steps_completed += 1
        if action.action_type == "reply" and action.content:
            if "resolved" in action.content.lower():
                task.resolved = True
        score = grade_multistep(task)
        return Reward(score=score, feedback="multi-step evaluated")
    return Reward(score=0.0, feedback="invalid task")
