from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import models
from databases import engine
from api import todo_router, user_router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(todo_router, prefix="/todos", tags=["todos"])
app.include_router(user_router, prefix="/users", tags=["users"])
