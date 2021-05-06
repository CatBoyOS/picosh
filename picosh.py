from linker import *

import usys

def term():
    print("""Welcome to PicoSH

    - a list of avaliable commands can be found using 'cbam list'

    - any and all of your daily scripting needs are provided by python, please refer to the wiki for more info\n""")
    while True:
        tasks = input("░▒▓ ~  ").split(" ")
        packages = cbam.load_path()
        if tasks[0] in packages:
            module = tasks[0]
            function = tasks[1]
            try:
                arguments = tasks[2]
                with open("lost_ship.py","w") as f:
                    f.write("")
                with open("lost_ship.py","a") as f:
                    f.write("import " + module + "\n")
                    f.write("def lost():\n")
                    f.write("   " + module + "." + function + "(\"" + arguments + "\")")
                import lost_ship
                lost_ship.lost()
            except IndexError:
                with open("lost_ship.py","w") as f:
                    f.write("")
                with open("lost_ship.py","a") as f:
                    f.write("import " + module + "\n")
                    f.write("def lost():\n")
                    f.write("   " + module + "." + function + "()")
                import lost_ship
                lost_ship.lost()
                del sys.modules["lost_ship"]
        else:
            pass

term()
