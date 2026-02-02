# simple-backend-api
FastAPI × SQLite × SQLAlchemy

Web から title / description を受け取り、SQLite に保存して
CRUD（作成・取得・更新・削除）を行う最小構成のバックエンド API です。

--------------------------------------------------
構成
--------------------------------------------------

.
├── main.py
├── database.py
├── models.py
└── requirements.txt

--------------------------------------------------
セットアップ（Windows / PowerShell）
--------------------------------------------------

1. リポジトリをクローン

git clone https://github.com/<your-name>/<repo-name>.git
cd <repo-name>

2. 仮想環境を作成・有効化

python -m venv venv
.\venv\Scripts\activate

3. 依存関係をインストール

pip install -r requirements.txt

4. サーバー起動

uvicorn main:app --reload

Swagger UI:
http://127.0.0.1:8000/docs

--------------------------------------------------
セットアップ（Linux / macOS）
--------------------------------------------------

git clone https://github.com/<your-name>/<repo-name>.git
cd <repo-name>

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn main:app --reload

--------------------------------------------------
API 仕様
--------------------------------------------------

POST /tasks
title, description をクエリで送信

例:
curl -X POST "http://127.0.0.1:8000/tasks?title=study&description=fastapi"

GET /tasks
登録されているタスク一覧を取得

PUT /tasks/{task_id}
タスクを更新

DELETE /tasks/{task_id}
タスクを削除

--------------------------------------------------
データベース
--------------------------------------------------

SQLite を使用
test.db がプロジェクト直下に作成されます

--------------------------------------------------
.gitignore（推奨）
--------------------------------------------------

__pycache__/
*.pyc
venv/
test.db
