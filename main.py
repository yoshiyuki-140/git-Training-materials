from fastapi import FastAPI

app = FastAPI()


@app.get("/")  # ルーティングの設定
def root():
    return {"message": "Hello World"}