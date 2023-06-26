from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from routers import words


app = FastAPI()

app.include_router(words.router)

