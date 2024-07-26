def add(x,y):
    return x+y

def subtract(x,y):
  return x-y

def multiply(x,y):
  return x*y

def divide(x,y):
  return x/y


def calculator():
    operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
    }
    num1 = int(input("enter first number"))
    for i in operations:
        print(i)
    print("pick any operation symbol")
    operation_symbol = input()
    num2 = int(input("enter another number"))
    calculation = operations[operation_symbol]
    answer = calculation(num1, num2)
    print(f"answer is: {answer}")

calculator()