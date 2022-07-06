from pydantic import BaseModel


class UserRequest(BaseModel):
    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True
