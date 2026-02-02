from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from models import Task

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --------------------
# Create（POST）
# --------------------
@app.post("/tasks")
def create_task(
    title: str,
    description: str,
    db: Session = Depends(get_db)
):
    task = Task(title=title, description=description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# --------------------
# Read（GET）
# --------------------
@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

# --------------------
# Update（PUT）
# --------------------
@app.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    title: str,
    description: str,
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = title
    task.description = description
    db.commit()
    db.refresh(task)
    return task

# --------------------
# Delete（DELETE）
# --------------------
@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}

