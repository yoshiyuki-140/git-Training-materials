from openai import OpenAI
client = OpenAI()

from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
app = FastAPI()

@app.get("/GPT") 
def training():
    completion = OpenAI.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "おすすめの筋トレは？"}
        ]
    )
    return {"response": completion.choices[0].message.get("content")}