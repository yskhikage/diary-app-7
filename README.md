# Diary App

カレンダー形式の日記・イベント管理アプリ

## 使用技術

* Python
* Flask
* HTML


## ディレクトリ構成

```text
diary_app/
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── Pipfile
├── templates/
│   ├── base.html
│   ├── calendar.html
│   └── index.html
```



## 環境構築

リポジトリをクローンします。

```bash
git clone https://github.com/yskhikage/diary-app-7.git
cd diary_app
```

仮想環境を作成します。

```bash
python3 -m venv venv
```

仮想環境を有効化します。

macOS / Linuxの場合：

```bash
source venv/bin/activate
```

Windowsの場合：

```bash
venv\Scripts\activate
```

必要なパッケージをインストールします。

```bash
python -m pip install -r requirements.txt
```

## データベースの作成

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

終了する場合は、以下を実行します。

```python
exit()
```

## アプリケーションの起動

```bash
python app.py
```

起動後、ブラウザで以下にアクセスします。

```text
http://127.0.0.1:5000/
```

カレンダー画面：

```text
http://127.0.0.1:5000/calendar
```

## イベントモデル

| 項目         | 内容      |
| ---------- | ------- |
| id         | イベントID  |
| name       | イベント名   |
| date       | イベントの日付 |
| created_at | 作成日時    |
| updated_at | 更新日時    |

## 今後実装予定の機能

* イベントの新規登録
* イベントの編集
* イベントの削除
* 日記本文の登録
* データベースに登録されたイベントのカレンダー表示
* 入力内容のバリデーション
* 画面デザインの改善

## 注意事項

このアプリケーションは現在開発中です。

`config.py` は開発環境向けの設定になっています。本番環境で使用する場合は、デバッグモードやデータベース設定を変更してください。
