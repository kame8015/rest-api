# ローカル実行の方法
## アプリケーションの起動
```
$ python --version
Python 3.8.5

$ python -m venv .venv
$ source .venv/bin/acticate
$ pip install -r requirements.txt
$ python app.py
```

## ユーザ登録
```
$ curl -X POST -d `{"user_id": "TaroYamada", "password": "PaSSwd2021"}` {ENDPOINT}:5000/signup
```

## ユーザ取得
```
$ curl {ENDPOINT}/5000/users/TaroYamada
```