from sqlmodel import Session, select
from .models import User, Task
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(session: Session, username: str, password: str):
    hashed_password = pwd_context.hash(password)
    user = User(username=username, hashed_password=hashed_password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def create_task(session: Session, title: str, description: str, due_date, owner_id: int):
    task = Task(title=title, description=description, due_date=due_date, owner_id=owner_id)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def get_user_tasks(session: Session, user_id: int):
    return session.exec(select(Task).where(Task.owner_id == user_id)).all()
