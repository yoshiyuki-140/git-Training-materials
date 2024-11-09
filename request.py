import requests
import json

# JSONファイルからイベント情報を読み込む関数
def load_event_data(file_name):
    with open(file_name, "r") as file:
        return json.load(file)

# 各JSONファイルからイベント情報を読み込み、リクエストを送信する
for file_name in ["event1.json", "event2.json"]:
    # イベント情報を読み込む
    event_data = load_event_data(file_name)
    
    # POSTリクエストの送信
    response = requests.post("http://localhost:8000/events/", json=event_data)

    # レスポンスの確認
    print(response.status_code)
    print(response.json())