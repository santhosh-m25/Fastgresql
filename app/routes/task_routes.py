from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..schema import TaskCreate, TaskRead
from ..crud import create_task, get_user_tasks
from ..auth import get_current_user
from ..db import get_session
from ..models import User
from typing import List

router = APIRouter()

@router.post("/tasks", response_model=TaskRead)
def create(task: TaskCreate, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    return create_task(session, task.title, task.description, task.due_date, user.id)

@router.get("/tasks", response_model=List[TaskRead])
def read(session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    return get_user_tasks(session, user.id)
