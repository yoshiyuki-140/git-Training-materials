from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from event import Event

app = FastAPI()

# イベントデータを格納するリスト
events_db = []
event_id_counter = 0

#イベントを作成する
@app.post("/events/")
def create_event(event: Event): #リストに追加する前にイベントごとにidを更新して、idからデータを取ってこれるように処理を行う
    global event_id_counter
    event_id_counter += 1
    event.id = event_id_counter
    events_db.append(event)
    return {"message": "イベント作成", "event": event}

#rootパスへのGETリクエストが実行されたら"/events/"に転送する
@app.get("/")
def root():
    return RedirectResponse(url="/events/")

#すべてのイベントを取得する
@app.get("/events/")
def get_all_events():
    return events_db

#特定のイベントを取得する
@app.get("/events/{event_id}")  #パスのidに紐づいたイベントをリストから検索し、当てはまったイベント情報を返す
def get_event(event_id: int):
    for event in events_db:
        if event.id == event_id:
            return event
    raise HTTPException(status_code=404, detail="イベントはありませんでした")#当てはまらない場合は
#FastAPIの”HTTPException“を使用して、HTTPエラーとして404を返す