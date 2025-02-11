
from dataclasses import dataclass
from fastapi import FastAPI
import httpx

app = FastAPI()


@app.get("/")
def hello_world():
    "This is our main function"
    return "Hello World!"

@app.get("/error")
def error():
    raise ValueError("oops")

@app.get("/users")
def get_users() -> list[User]:
    response = httpx.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()
    return users

@app.post("/users")
def create_user(new_user: User) -> bool:
    return True