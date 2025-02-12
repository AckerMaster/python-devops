import subprocess as sbp

command = "systemctl status nginx | grep Active"
p = sbp.run(command.split(), stdout=sbp.PIPE , stderr=sbp.PIPE)

output_bytes = p.stdout
output_str = output_bytes.decode()

status = "(running)" in output_str

print(status)

if status == 1:
    user_input = input("server is running. Do you want to stop it? [y/n]: ").lower()
    if user_input == "y" or user_input == "yes":
        command = "sudo systemctl stop nginx"
        p = sbp.run(command.split(), stdout=sbp.PIPE , stderr=sbp.PIPE)
    elif user_input == "n" or user_input == "no":
        print("Okay. Bye")
    else:
        print("Invalid Choise")
else:
    user_input = input("server is NOT running. Do you want to start it? [y/n]: ").lower()
    if user_input == "y" or user_input == "yes":
        command = "sudo systemctl start nginx"
        p = sbp.run(command.split(), stdout=sbp.PIPE , stderr=sbp.PIPE)
    elif user_input == "n" or user_input == "no":
        print("Okay. Bye")
    else:
        print("Invalid Choise")

# print(p.returncode)

# if p.returncode == 0:
#     output_bytes = p.stdout
#     output_str = output_bytes.decode()
#     print(output_str)
# else:
#     err_bytes = p.stderr
#     err_str = err_bytes.decode()
#     print(f"ERROR: {err_str}")
