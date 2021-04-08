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
        print(package_name + " insalled")
    else:
        pass
def uninstall(package_name):
    if input("uninstall " + package_name + "? [y/n] ") == "y":
        path = load_path()
        path.remove(package_name)
        save_path(path)
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
