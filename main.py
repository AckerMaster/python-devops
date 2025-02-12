
from fastapi import FastAPI
from models import ServerStatusResponse, Server
from models import read_server_list, add_new_server

app = FastAPI()

@app.get("/server")
def get_server(server_name: str) -> ServerStatusResponse:
    servers = read_server_list()
    for server in servers:
        if server.name == server_name:
            server_status = server.online
            return ServerStatusResponse(server_name=server_name, server_status=server_status)
    return ServerStatusResponse(server_name=server_name, server_status="Didn't find this server")

@app.post("/server")
def create_server(server_name: str, online_status: bool, CPUs, RAM) -> ServerStatusResponse:
    "Please enter server name, it's online status, number of CPUs and RAM"
    new_server = Server(name=server_name, online=online_status, cpus=CPUs, ram=RAM)
    add_new_server(new_server)
    return ServerStatusResponse(server_name=server_name, server_status="Created")