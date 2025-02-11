from log import setup_logging

# logger
logger = setup_logging()

# servers list and status
servers_dict = {
    
    "Nginx": "Running",
    "Docker": "Not Running",
    "Terraform": "Running",
    "Kubernetes": "Running",
    "AWS": "Not Running"
}

# converting servers name to lower case
new_servers_dict = { key.strip().lower() : value for key, value in servers_dict.items()}



# asking for user input until completion

server_name = input("Please Enter server name: ")

def check_server(server_name):
    server_name = server_name.strip().lower()
    logger.info(f"The user chose: {server_name}")
    try:
        print(f"{server_name} is {new_servers_dict[server_name]}")

    except KeyError:
            print("Server is not recognized.")
            logger.error("Invalid Input from user")

            
            
            
#---------------------------------------------------------------------#
#----------------------- Another main function -----------------------#
#---------------------------------------------------------------------#

# servers = {"nginx": True, "docker" : False}

# def get_server_status(server_name: str) -> bool:
    
#     try:
#         return servers[server_name]
#     except KeyError:
#         logger.error("This server does not exist")
#     return False 
        
# while True:
#     server_name = input("Please Enter server name: ")
#     server_name = server_name.lower()
#     status = get_server_status(server_name)
#     logger.info(f"Server status is {str(status)}")
