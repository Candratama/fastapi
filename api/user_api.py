from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from databases import get_db_session
from schemas.user_schema import UsersBase, UsersUpdate
import crud


user_router = APIRouter()


def not_found(id):
    return HTTPException(status_code=404, detail=f"Users with id {id} not found")


@user_router.get("/")
async def read_all_users(db: Session = Depends(get_db_session)):
    return crud.get_all_users(db)


@user_router.get("/{user_id}")
async def read_user_by_id(user_id: int, db: Session = Depends(get_db_session)):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise not_found(user_id)
    return user


@user_router.post("/")
async def create_user(user: UsersBase, db: Session = Depends(get_db_session)):
    return crud.create_user(db, user), {"message": "User created successfully"}


@user_router.put("/{user_id}")
async def update_user(
    user_id: int, user: UsersUpdate, db: Session = Depends(get_db_session)
):
    updated_user = crud.update_user(db, user_id, user)
    if not updated_user:
        raise not_found(user_id)
    return updated_user, {"message": "User updated successfully"}


@user_router.delete("/{user_id}")
async def delete_user_by_id(user_id: int, db: Session = Depends(get_db_session)):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise not_found(user_id)
    return crud.delete_user_by_id(db, user_id)
