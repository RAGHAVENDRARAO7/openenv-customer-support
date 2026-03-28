import os
from openai import OpenAI
from env.environment import CustomerSupportEnv

client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

env = CustomerSupportEnv()

def run():
    scores = []

    for _ in range(3):
        obs = env.reset()
        done = False

        while not done:
            prompt = f"Ticket: {obs['customer_message']}"

            res = client.chat.completions.create(
                model=os.getenv("MODEL_NAME"),
                messages=[{"role": "user", "content": prompt}]
            )

            text = res.choices[0].message.content.lower()

            action = {"action_type": "reply", "content": text}

            obs, reward, done, _ = env.step(action)

        scores.append(reward["score"])

    print("Average Score:", sum(scores) / len(scores))


if __name__ == "__main__":
    run()
