from fastapi import FastAPI
from env.environment import CustomerSupportEnv

app = FastAPI()
env = CustomerSupportEnv()

@app.post("/reset")
def reset():
    return env.reset()
@app.post("/step")
def step(action: dict):
    obs, reward, done, info = env.step(action)

    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/")
def root():
    return {"status": "running"}
