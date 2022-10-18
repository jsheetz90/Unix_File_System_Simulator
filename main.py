import shellcommands
root = None

def parse(commands, folder):

        cmd = commands[0]
        if cmd == "ls":
                shellcommands.ls(folder)
                return folder

        elif cmd == "mkdir" and len(commands) == 2:
                shellcommands.mkdir(commands[1], folder)
                return folder

        elif cmd == "cd" and len(commands) == 2:
                return shellcommands.cd(root, folder, commands[1])

        elif cmd == "touch" and len(commands) == 2:
                shellcommands.touch (commands[1], folder)
                return folder

        elif cmd == "quit" and len(commands) == 1:
                return None

        else:
                print("Hmm, something isn't quite right... try again.")
                return folder
                

def main():
    global root
    root = shellcommands.Folder("root", "/")
    directory = root
    run = True

    while (run):
        command = input(f"john@isveryhireable {directory} $ ")
        commands = command.split()
        directory = parse(commands, directory)

        if directory == None:
            run = False
            
        

if __name__ == "__main__":
        main()