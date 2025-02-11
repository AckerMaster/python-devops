
from fastapi import FastAPI
from models import ServerStatusResponse, Server

app = FastAPI()


@app.get("/server")
def get_server(server_name: str) -> ServerStatusResponse:
    server_status = servers.get(server_name, "Does not exist")
    return ServerStatusResponse(server_name, server_status)


@app.post("/server")
def create_server(server_name: str) -> ServerStatusResponse:
    if server_name in servers:
        return ServerStatusResponse(server_name, "Name already exists")
    else:
        servers[server_name] = True
        return ServerStatusResponse(server_name, "Created")