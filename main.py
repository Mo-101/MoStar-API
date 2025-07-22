from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
OPENAI_KEY = os.getenv("OPENAI_KEY")

class ChatRequest(BaseModel):
    message: str = "Hello!"

@app.post("/chat")
def chat(req: ChatRequest):
    headers = {
        "Authorization": f"Bearer {OPENAI_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": req.message}],
    }
    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=data
    )
    return response.json()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
