def waving_to(name:str):
    print("Hello " + name + "!")

def run():
    name:str = str(input("Type your name: "))
    waving_to(name)

if __name__ == "__main__":
    run()