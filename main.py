
from fastapi import FastAPI
from models import ServerStatusResponse, Server
from models import read_server_list, add_new_server

app = FastAPI()

# returns server details if exists, and a message if it doesn't
@app.get("/server")
def get_server(server_name: str) -> ServerStatusResponse:
    "Check Server Status. Please enter Server name you'd like to get details on"
    servers = read_server_list()
    for server in servers:
        if server.name == server_name:
            server_status = server.online
            return ServerStatusResponse(server_name=server_name, server_status=server_status)
    return ServerStatusResponse(server_name=server_name, server_status="Didn't find this server")


# adds new server to the list if valid.
@app.post("/server")
def create_server(server_name: str, online_status: bool, CPUs, RAM) -> ServerStatusResponse:
    "Add Server to Servers List. Please enter Server name, online status, number of CPUs and RAM"
    new_server = Server(name=server_name, online=online_status, cpus=CPUs, ram=RAM)
    add_new_server(new_server)
    return ServerStatusResponse(server_name=server_name, server_status="Created")