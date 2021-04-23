def command1():
    print("This is function for command1")

def command2():
    print("This is function for command1")

prefix = "-" #idk what to do with this to be honest
commands = {
    "-command": command1,
    "-command2": command2,
}

msg = input()
if commands[msg]:
    print("command exisits")
    commands[msg]()