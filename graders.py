def grade_classification(pred, expected):
    return 1.0 if pred == expected else 0.0

def grade_response(response):
    if response is None:
        return 0.0
    text = response.lower()
    score = 0.0
    if "sorry" in text:
        score += 0.3
    if "solution" in text or "try" in text:
        score += 0.4
    if len(text) > 30:
        score += 0.3
    return min(score, 1.0)

def grade_multistep(task):
    score = 0.2 * task.steps_completed
    if task.resolved:
        score += 0.5
    return min(score, 1.0)
