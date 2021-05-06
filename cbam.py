def load_path():
    with open("path","r+") as f:
        path = f.readlines()
        for i in path:
            index = path.index(i)
            path[index] = path[index].replace("\n","")
        return(path)

def save_path(path):
    open('path', 'w').close()
    with open("path","a+") as f:
        for i in path:
            f.write(i + "\n")

def test():
    load_path()

def install(package_name):
    if input("install " + package_name + "? [y/n] ") == "y":
        path = load_path()
        path.append(package_name)
        save_path(path)
        with open("linker.py","a+") as f:
            f.write("import " + package_name)
        print(package_name + " insalled")
        print("please restart your system to apply changes")
    else:
        pass
def uninstall(package_name):
    if input("uninstall " + package_name + "? [y/n] ") == "y":
        path = load_path()
        path.remove(package_name)
        save_path(path)
        with open("linker.py","r") as f:
                linker_current = f.read()
                linker_current = linker_current.split("\n)
                for i in linker_current:
                    if package_name in linker_current:
                                index = linker_current.index(package_name)
                                linker_current.remove(index)
                    else:
                        pass
                    for i in linker_current:
                        f.write("import " + i)
        print("please restart your system to apply changes")
    else:
        pass
def help():
    print("""Welcome to CBAM: the CatBoy Application Manager
    
    usage: cbam <operation> [targets]

    OPERATIONS:
        install 
            installs a package
        uninstall
            removs a package
        list
            lists installed packages""")

def list():
    print("Packages installed:")
    path = load_path()
    for i in path:
        print(i)
