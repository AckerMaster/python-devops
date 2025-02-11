
from dataclasses import dataclass
from fastapi import FastAPI
import httpx

app = FastAPI()


@dataclass
class User:
    name: str
    email: str


@app.get("/")
def hello_world():
    "This is our main function"
    return "Hello World!"

@app.get("/users")
def get_users() -> list[User]:
    response = httpx.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()
    return users

@app.post("/users")
def create_user(new_user: User) -> bool:
    return new_user