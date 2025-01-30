from pydantic import BaseModel, EmailStr


class SAdminChanges(BaseModel):
    role: str

class SUsers(BaseModel):
    email: EmailStr
    password: str