print(" === CALCULATOR === ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Select the operation you want: ")
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
if operation == "add":
    print("The result is: ", add(num1, num2))
elif operation == "subtract":
    print("The result is: ",subtract(num1, num2))
elif operation == "multiply":
    print("The result is: ", multiply(num1, num2))
else:
    print("the result is: ",divide(num1, num2))
if num2 == 0:
    try:
        result = divide(num1, num2)
    except ZeroDivisionError:
        print("You can't divide by zero, pick another number!")
    
        
        