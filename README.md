# Diary App

カレンダー形式でイベントを管理するFlaskアプリケーションです。

## 使用技術

- Python 3.12
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- SQLite
- HTML / CSS
- Docker

## ディレクトリ構成

```text
diary_app/
├── app.py
├── config.py
├── form.py
├── models.py
├── requirements.txt
├── Pipfile
├── Dockerfile
├── .dockerignore
├── instance/
├── static/
└── templates/
```

## リポジトリの取得

```bash
git clone https://github.com/yskhikage/diary-app-7.git
cd diary-app-7
```

## ローカル環境での起動

### 1. 仮想環境を作成する

```bash
python3 -m venv venv
```

### 2. 仮想環境を有効化する

macOS / Linux：

```bash
source venv/bin/activate
```

Windows：

```bash
venv\Scripts\activate
```

### 3. 必要なパッケージをインストールする

```bash
python -m pip install -r requirements.txt
```

### 4. 環境変数を設定する

プロジェクト直下に `.env` ファイルを作成し、必要な環境変数を記載します。

`.env` はGitの管理対象には含めません。

### 5. データベースを作成する

Pythonシェルを起動します。

```bash
python
```

以下を実行します。

```python
from app import app, db

with app.app_context():
    db.create_all()
```

Pythonシェルを終了します。

```python
exit()
```

### 6. アプリケーションを起動する

```bash
python app.py
```

起動後、以下のURLにアクセスします。

トップページ：

```text
http://127.0.0.1:5000/
```

カレンダー画面：

```text
http://127.0.0.1:5000/calendar
```

## Dockerでの起動

### 1. Dockerイメージをビルドする

```bash
docker build -t diary-app-7 .
```

### 2. コンテナを起動する

```bash
docker run --rm \
  -p 5001:5000 \
  --env-file .env \
  diary-app-7
```

起動後、以下のURLにアクセスします。

```text
http://localhost:5001/
```

カレンダー画面：

```text
http://localhost:5001/calendar
```

`-p 5001:5000` は、Mac側の5001番ポートをコンテナ側の5000番ポートへ接続する指定です。

```text
Macの5001番ポート → コンテナの5000番ポート
```

Macではシステム機能が5000番ポートを使用している場合があるため、このREADMEでは5001番ポートを使用しています。

## Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /diary_app

# requirements.txtに変更がない場合、
# pip installの結果をキャッシュとして再利用する
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "--app", "app", "run", "--host=0.0.0.0", "--port=5000", "--debug"]
```

## .dockerignore

Dockerイメージに不要なファイルを含めないようにしています。

```text
venv/
__pycache__/
*.pyc
.env
.git/
```

現在は既存のSQLiteデータベースをDockerイメージへ含めるため、`instance/`は除外していません。

なお、現在のDocker構成では、コンテナ起動後に追加・変更したデータはコンテナ終了時に失われる可能性があります。データの永続化は今後対応予定です。

## イベントモデル

| 項目 | 内容 |
| --- | --- |
| id | イベントID |
| name | イベント名 |
| date | イベントの日付 |
| created_at | 作成日時 |
| updated_at | 更新日時 |

## 主な機能

- イベントの一覧表示
- カレンダー形式でのイベント表示
- イベントの新規登録
- イベントの詳細表示
- イベントの編集
- イベントの削除
- 入力内容のバリデーション

## 今後実装予定の機能

- 日記本文の登録
- SQLiteデータベースの永続化
- 画面デザインの改善
- エラーハンドリングの追加
- 本番環境向け設定への対応

## 注意事項

このアプリケーションは現在開発中です。

`config.py` は開発環境向けの設定になっています。本番環境で使用する場合は、デバッグモード、シークレットキー、データベース設定などを変更してください。