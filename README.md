# ハッカソン用のGitの研修リポジトリ


# ゴール

- FastAPIで簡単なWeb APIを作成できる
    - ブラウザで`localhost:8000`にアクセスすると、`{"Hello":"World"}`という文字列が表示されるようにする
    - ブラウザで`localhost:8000/{自分の名前}`にアクセスすると`{"Hello":"自分の名前"}`と表示されるようにする。
    - ブラウザで`localhost:8000/index`アクセスすると、プロジェクトルートにある`index.html`の中身が表示されるようにする。



# 環境構築

```
python3 -m venv venv
venv\Scripts\activate.ps1 # Linux -> . ./venv/bin/activate
pip install -r requirements.txt
```

> [!NOTE]
> エラーが出たらまずはそのエラーでググる(検索する)こと。
> わからなければ聞くこのタスクでは5分悩んだら聞く
> 鼻であしらわても、めげないこと。
> そんな事で心の平穏を乱すな。
