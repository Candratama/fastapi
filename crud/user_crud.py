from datetime import datetime

from sqlalchemy.orm import Session
from models import user_model
from schemas import UsersBase, UsersUpdate


def get_all_users(db: Session):
    return db.query(user_model.Users).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(user_model.Users).filter(user_id == user_model.Users.id).first()


def create_user(db: Session, user: UsersBase):
    new_user = user_model.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, user_id: int, user: UsersUpdate):
    update_data = user.dict(exclude_unset=True)
    update_data["updated_at"] = datetime.now()
    db.query(user_model.Users).filter(user_id == user_model.Users.id).update(
        update_data
    )
    db.commit()
    return db.query(user_model.Users).filter(user_id == user_model.Users.id).first()


def delete_user_by_id(db: Session, user_id: int):
    db.query(user_model.Users).filter(user_id == user_model.Users.id).delete()
    db.commit()
    return {"message": "User deleted successfully"}
