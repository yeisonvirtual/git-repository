def add_2_numbers(a:int, b:int):
    result:int = a + b
    print(str(a) + " + " + str(b))
    print("Result: " + str(result))

def substract_2_numbers(a:int, b:int):
    result:int = a - b
    print(str(a) + " - " + str(b))
    print("Result: " + str(result))

def multiply_2_numbers(a:int, b:int):
    result:int = a * b
    print(str(a) + " * " + str(b))
    print("Result: " + str(result))

def divide_2_numbers(a:int, b:int):
    if b == 0:
        print("Division by zero doesn't exist")
    else:
        result:int = a / b
        print(str(a) + " / " + str(b))
        print("Result: " + str(result))

def ask_for_an_int():
    number:int = int(input("Type an interger number: "))
    return number

def waving_to(name:str):
    print("Hello " + name + "!")

def run():
    name = input("Type your name: ")
    waving_to(name)

if __name__ == "__main__":
    run()