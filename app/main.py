from fastapi import FastAPI
from .db import engine
from .models import SQLModel
from .routes import user_routes, task_routes

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(user_routes.router)
app.include_router(task_routes.router)
