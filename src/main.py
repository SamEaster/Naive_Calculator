def my_name(s: str):
    return f"My name is {s}"
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from core import my_name
import pathlib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get('/')
# async def root():
#     return {"message": "Programe is running!!"}

class User_name(BaseModel):
    name: str

@app.post('/name')
async def print_name(user: User_name):
    t = my_name(user.name)
    # print(t)
    return t

current_dir = pathlib.Path(__file__).parent.parent
current_dir = current_dir / "frontend"

app.mount("/", StaticFiles(directory=current_dir, html=True), name="static")
