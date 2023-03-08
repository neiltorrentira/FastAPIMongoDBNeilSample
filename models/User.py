from pydantic import BaseModel


class User(BaseModel):
    name: str
    address: str
    email: str
    password: str
