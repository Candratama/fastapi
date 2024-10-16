from datetime import datetime

from sqlalchemy.orm import Session
from models import Todos
from schemas import TodoBase, TodoUpdate


def get_all_todos(db: Session):
    return db.query(Todos).all()


def get_todo_by_id(db: Session, todo_id: int):
    return db.query(Todos).filter(todo_id == Todos.id).first()


def create_todo(db: Session, todo: TodoBase):
    new_todo = Todos(**todo.dict())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def update_todo(db: Session, todo_id: int, todo: TodoUpdate):
    update_data = todo.dict(exclude_unset=True)
    update_data["updated_at"] = datetime.now()
    db.query(Todos).filter(todo_id == Todos.id).update(update_data)
    db.commit()
    return db.query(Todos).filter(todo_id == Todos.id).first()


def delete_todo_by_id(db: Session, todo_id: int):
    db.query(Todos).filter(todo_id == Todos.id).delete()
    db.commit()
    return {"message": "Todo deleted successfully"}
