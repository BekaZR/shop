from sqlalchemy.orm import Session

from passlib.hash import pbkdf2_sha256

from apps.users.schemas import UserRegistration
from apps.users.models import User


def create_user(db: Session, user: UserRegistration):
    password = pbkdf2_sha256.hash(user.password)
    user = User(username=user.username, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session):
    return db.query(User).all()
