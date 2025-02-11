
from dataclasses import dataclass
from fastapi import FastAPI
import httpx

app = FastAPI()


servers_dict = {
    
    "Nginx": "Running",
    "Docker": "Not Running",
    "Terraform": "Running",
    "Kubernetes": "Running",
    "AWS": "Not Running"
}


new_servers_dict = { key.strip().lower() : value for key, value in servers_dict.items()}


@app.get("/")
def ask_for_server(server_name: str) -> str:
    "This is our main function"
    server_name = server_name.strip().lower()
    try:
       return f"{server_name} is {new_servers_dict[server_name]}"
    except KeyError:
            return f"{server_name} is not recognized."

@app.get("/add")
def add_server(server_name: str) -> str:
    "Add server to the list"
    server_name = server_name.strip().lower()
    if server_name in new_servers_dict:
        return "Server already exist"
    else:
        new_servers_dict[server_name] = "Running"
        return f"{server_name} was added to servers list"

