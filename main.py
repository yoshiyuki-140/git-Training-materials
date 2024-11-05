from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")  # ルーティングの設定
def root():
    return {"":""}

@app.get("/{hello}")
def root():
    return {"hello":"world"}

@app.get("/{name}")
def root(name: str):
    return JSONResponse(content={"Hello": name})
