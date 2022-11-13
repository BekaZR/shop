from pydantic import BaseModel


class UserRegistration(BaseModel):
    username: str
    password: str
    
    class Config:
        orm_mode = True

