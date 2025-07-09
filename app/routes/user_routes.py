from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from ..schema import UserCreate
from ..crud import create_user
from ..db import get_session

router = APIRouter()

@router.post("/signup")
def signup(user: UserCreate, session: Session = Depends(get_session)):
    return create_user(session, user.username, user.password)
