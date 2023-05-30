def add_2_numbers(a:int, b:int):
    result:int = a + b
    print(str(a) + " + " + str(b))
    print("Result: " + str(result) + "\n")

def substract_2_numbers(a:int, b:int):
    result:int = a - b
    print(str(a) + " - " + str(b))
    print("Result: " + str(result) + "\n")

def multiply_2_numbers(a:int, b:int):
    result:int = a * b
    print(str(a) + " * " + str(b))
    print("Result: " + str(result) + "\n")

def divide_2_numbers(a:int, b:int):
    if b == 0:
        print("Division by zero doesn't exist")
    else:
        result:int = a / b
        print(str(a) + " / " + str(b))
        print("Result: " + str(result) + "\n")

def perform_all_operations(a:int, b:int):
    add_2_numbers(a, b)
    substract_2_numbers(a, b)
    multiply_2_numbers(a, b)
    divide_2_numbers(a, b)

def ask_for_an_int(message:str):
    my_number:int = int(input(message))
    return my_number

def ask_for_an_str(message:str):
    my_str:str = str(input(message))
    return my_str

def waving_to(name:str):
    print("Hello " + name + "!")

def run():
    #Asking the name
    name:str = ask_for_an_str("Please, type your name: ")
    waving_to(name)

    #Performing basic math operations
    operand_a:int = ask_for_an_int("Type the operand 'a': ")
    operand_b:int = ask_for_an_int("Type the operand 'b': ")
    perform_all_operations(operand_a, operand_b)

    #Farewell
    print("All basic operations done! \n Bye " + name)

if __name__ == "__main__":
    run()