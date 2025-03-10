import logging

logger = logging.getLogger("myapp")
servers = {"Nginx": True, "Docker": False}

def get_server_status(server_name: str) -> bool:
    lowercase_servers = {key.strip().lower(): value for key, value in servers.items()}
    try:
        return lowercase_servers[server_name]
    except KeyError:
        logger.error(f"The server name {server_name} does not exist")
        return False
        


def check_servers_from_terminal():
    while True:
        server_name = input("Enter server name: ").strip().lower()
        status = get_server_status(server_name)
        logger.info(f"Server {server_name} status is: {status}")