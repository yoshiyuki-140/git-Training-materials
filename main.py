from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
app = FastAPI()

@app.get("/")  # ルーティングの設定
def root():
    return {"":""}

@app.get("/hello")
def root():
    return {"hello":"world"}

@app.get("/{name}")
def root(name: str):
    return {"Hello": name}

@app.get("/index")
def root():
    url = os.path.join("static", "index.html")
    return FileResponse(url)