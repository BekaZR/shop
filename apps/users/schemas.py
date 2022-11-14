from pydantic import BaseModel


class UserRegistration(BaseModel):
    username: str
    password: str
    
    class Config:
        orm_mode = True

class UserGet(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
