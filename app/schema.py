from typing import Optional
from sqlmodel import SQLModel
from datetime import date

class UserCreate(SQLModel):
    username: str
    password: str

class TaskCreate(SQLModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None

class TaskRead(SQLModel):
    id: int
    title: str
    description: Optional[str]
    due_date: Optional[date]
    status: str
    owner_id: int
