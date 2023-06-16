from typing import Optional, List, Dict
from pydantic import BaseModel


class UserToRegister(BaseModel):
    #    first_name: str
    last_name: str
    email: str
    password: str
    createdAt: str


class User(UserToRegister):
    extra_info: str  # Atributo adicional para corregir el error


class UserToUpdate(User):
    first_name: Optional[str]
    last_name: Optional[str]
