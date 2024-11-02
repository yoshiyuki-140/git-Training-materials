# ハッカソン用のGitの研修リポジトリ


# ゴール

- FastAPIで簡単なWeb APIを作成できる
    - ブラウザで`localhost:8000`にアクセスすると、`{"":""}`という文字列が表示されるようにする
    - ブラウザで`localhost:8000`にアクセスすると、`{"Hello":"World"}`という文字列が表示されるようにする
    - ブラウザで`localhost:8000/{自分の名前}`にアクセスすると`{"Hello":"自分の名前"}`と表示されるようにする
    - ブラウザで`localhost:8000/index`アクセスすると、プロジェクトルートにある`index.html`の中身が表示されるようにする


# ファイル説明

```
.
├── README.md           # ドキュメント
├── index.html          # テスト環境で使うダミーデータ
├── main.py             # FastAPIのメインファイル
├── makefile            # 各種コマンドのショートカット定義ファイル(今回は使わない)
└── requirements.txt    # チュートリアルに必要なPythonライブラリが書かれている
```


# 環境構築

```
python3 -m venv venv # Python仮想環境作成
venv\Scripts\activate.ps1 # Python仮想環境の起動、Linux系システムでは次の通り -> `. ./venv/bin/activate`
pip install -r requirements.txt # 必要なライブラリを仮想環境にインストール
```

> [!NOTE]
> エラーが出たらまずはそのエラーでググる(検索する)こと
> わからなければ聞く、このタスクでは5分悩んだら聞く
> 鼻であしらわても、めげないこと
> そんな事で心をやまないこと