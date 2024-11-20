from openai import OpenAI
client = OpenAI()

from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
app = FastAPI()

@app.get("/GPT")  # ルーティングの設定
def training():

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "おすすめの筋トレは？"
        }
    ]
    )

    return {completion.choices[0].message}