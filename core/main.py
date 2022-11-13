from fastapi import FastAPI
from apps.users.views import router
from core.database import SessionLocal

from core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(router)