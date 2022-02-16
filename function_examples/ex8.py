x = int(input("num:"))
y = int(input("num:"))
user = input("math: ")


def add(num1, num2):
    sonuc = num1 + num2
    return sonuc


def subtract(num1, num2):
    sonuc = num1 - num2
    return sonuc


def multiply(num1, num2):
    sonuc = num1 * num2
    return sonuc


def divide(num1, num2):
    sonuc = num1 / num2
    return sonuc


def calculator(userInput, num1, num2):
    if userInput == "+":
        return add(num1, num2)
    elif userInput == "-":
        return subtract(num1, num2)
    elif userInput == "*":
        return multiply(num1, num2)
    elif userInput == "/":
        return divide(num1, num2)
print(calculator(user, x, y))


