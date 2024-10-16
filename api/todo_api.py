from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from databases import get_db_session
from schemas.todo_schema import TodoBase, TodoUpdate
import crud

todo_router = APIRouter()


def not_found(id):
    return HTTPException(status_code=404, detail=f"Todos with id {id} not found")


@todo_router.get("/")
async def read_all_todo(db: Session = Depends(get_db_session)):
    return crud.get_all_todos(db)


@todo_router.get("/{todo_id}")
async def read_todo_by_id(todo_id: int, db: Session = Depends(get_db_session)):
    todo = crud.get_todo_by_id(db, todo_id)
    if not todo:
        raise not_found(todo_id)
    return todo


@todo_router.post("/")
async def create_todo(todo: TodoBase, db: Session = Depends(get_db_session)):
    return crud.create_todo(db, todo), {"message": "Todo created successfully"}


@todo_router.put("/{todo_id}")
async def update_todo(
    todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db_session)
):
    updated_todo = crud.update_todo(db, todo_id, todo)
    if not updated_todo:
        raise not_found(todo_id)
    return updated_todo, {"message": "Todo updated successfully"}


@todo_router.delete("/{todo_id}")
async def delete_todo_by_id(todo_id: int, db: Session = Depends(get_db_session)):
    todo = crud.get_todo_by_id(db, todo_id)
    if not todo:
        raise not_found(todo_id)
    return crud.delete_todo_by_id(db, todo_id)
