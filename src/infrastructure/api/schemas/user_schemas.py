from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
    phone: str

class UserUpdateSchema(BaseModel):
    name: str
    email: EmailStr
    phone: str

class UserResponseSchema(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    phone: str
