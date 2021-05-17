from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...db.connection import get_db
from ...models.users import User
from ...operations.users import get_user_by_email, get_user_by_id, get_users
from typing import List

router = APIRouter()


@router.get("/", response_model=List[User])
def read_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.get("/user_id/{user_id}", response_model=User)
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/user_email/{user_email}", response_model=User)
def read_user_by_email(user_email: str, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
