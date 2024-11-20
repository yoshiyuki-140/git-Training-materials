import openai
from fastapi import FastAPI

# OpenAI APIキーを設定
openai.api_key = "your_openai_api_key"

app = FastAPI()

@app.get("/GPT")
async def training():
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "おすすめの筋トレは？"}
        ]
    )
    return {"response": completion['choices'][0]['message']['content']}
