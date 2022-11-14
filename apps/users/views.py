from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from core.database import get_db

from apps.users.schemas import UserGet, UserRegistration
from apps.users.crud import create_user, get_user

router = APIRouter()


@router.post("/users/", response_model=UserRegistration)
def create_user_(user: UserRegistration, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)
