from pydantic import BaseModel
from datetime import datetime


# イベントを定義
class Event(BaseModel):
    id: int             
    title: str          #タイトル
    datetime: datetime  #日付
    location: str       #場所
    description: str    #進捗状況