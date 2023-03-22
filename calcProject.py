memory = 0 

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: division by zero"
    else:
        return x / y

def square_root(x):
    return x ** 0.5

def reciprocal(x):
    if x == 0:
        return "Error: division by zero"
    else:
        return 1 / x

def sign(x):
    return -x

def clear_memory():
    global memory
    memory = 0

def recall_memory():
    return memory

def store_memory(x):
    global memory
    memory = x

def add_to_memory(x):
    global memory
    memory += x

def subtract_from_memory(x):
    global memory
    memory -= x

def clear_all():
    global memory
    memory = 0
    return "0"

def clear_entry(current):
    return "0"

while True:
    print("Calculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Reciprocal")
    print("7. Sign")
    print("8. Memory Clear")
    print("9. Memory Recall")
    print("10. Add to Memory")
    print("11. Subtract from Memory")
    print("12. Clear All")
    print("13. Clear Entry")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "0":
        break

    elif choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        print("Result: ", result)

    elif choice == "5":
        num = float(input("Enter number: "))
        result = square_root(num)
        print("Result: ", result)

    elif choice == "6":
        num = float(input("Enter number: "))
        result = reciprocal(num)
        print("Result: ", result)

    elif choice == "7":
        num = float(input("Enter number: "))
        result = sign(num)
        print("Result: ", result)

    elif choice == "8":
        clear_memory()

    elif choice == "9":
        result = recall_memory()
        print("Result: ", result)

    elif choice == "10":
        num = float(input("Enter number: "))
        add_to_memory(num)

    elif choice == "11":
        num = float(input("Enter number: "))
        subtract_from_memory(num)

    elif choice == "12":
        result = clear_all()
        print("Result: ", result)

    elif choice == "13":
        result = clear_entry(result)
        print("Result: ", result)

    else:
        print("Invalid choice")

    
        