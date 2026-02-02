# simple-backend-api
**FastAPI × SQLite × SQLAlchemy**

Web から `title` / `description` を受け取り、SQLite に保存して  
CRUD（作成・取得・更新・削除）を行う **最小構成のバックエンド API** です。

> Web → API → DB の流れを理解するための学習用サンプル

---

## 使用技術

- **FastAPI**：API サーバー
- **SQLAlchemy**：ORM（Python ↔ DB）
- **SQLite**：ローカル DB

---

## ディレクトリ構成

```
.
├── main.py
├── database.py
├── models.py
└── requirements.txt
```

---

## セットアップ（Windows / PowerShell）

### 1. リポジトリをクローン
```
git clone https://github.com/boyswillbeboys77/simple-backend-api.git
cd simple-backend-api
```

### 2. 仮想環境を作成・有効化
```
python -m venv venv
.\venv\Scripts\activate
```

### 3. 依存関係をインストール
```
pip install -r requirements.txt
```

### 4. サーバー起動
```
uvicorn main:app --reload
```

Swagger UI: http://127.0.0.1:8000/docs

---

## セットアップ（Linux / macOS）

```
git clone https://github.com/boyswillbeboys77/simple-backend-api.git
cd simple-backend-api

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn main:app --reload
```

---

## API 仕様

### Create（POST） `/tasks`
```
curl -X POST "http://127.0.0.1:8000/tasks?title=study&description=fastapi"
```

### Read（GET） `/tasks`
```
curl -X GET "http://127.0.0.1:8000/tasks"
```

### Update（PUT） `/tasks/{task_id}`
```
curl -X PUT "http://127.0.0.1:8000/tasks/1?title=study2&description=sqlalchemy"
```

### Delete（DELETE） `/tasks/{task_id}`
```
curl -X DELETE "http://127.0.0.1:8000/tasks/1"
```

---

## データベース

- SQLite を使用
- `test.db` がプロジェクト直下に作成される
- 起動時にテーブル自動生成

```python
Base.metadata.create_all(bind=engine)
```

---

## 実装のポイント

- `Depends(get_db)` により DB セッションを自動注入
- リクエスト単位で Session を生成・終了
- ORM による安全な DB 操作

---

## .gitignore（推奨）

```
__pycache__/
*.pyc
venv/
test.db
```

## Qiitaで自分なりの深堀り理解
APIをつくるとはどういうことか、自分なりに整理しています。

👉 https://qiita.com/boyswillbeboys/items/f69ee7b743992e0df9ce


