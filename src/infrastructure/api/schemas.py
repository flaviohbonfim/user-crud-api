from pydantic import BaseModel, EmailStr, Field

class UserCreateSchema(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    phone: str = Field(..., min_length=5)

class UserUpdateSchema(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None

class UserResponseSchema(BaseModel):
    id: str
    name: str
    email: str
    phone: str

    class Config:
        from_attributes = True
