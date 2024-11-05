from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/{name}")  # ルーティングの設定
def root(name: str):
    return JSONResponse(content={"Hello": name})
