#Problema 10 funciones
#Parte 1
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

# Parte 2
def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

# Parte 3: Exponenciación y Módulo
def exponent(base, exp):
    return base ** exp

def modulo(num1, num2):
    if num2 == 0:
        return "Error: Modulo by zero is not allowed."
    return num1 % num2

# Parte 4: División Entera y Valor Absoluto
def floor_divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 // num2

def absolute(num):
    return abs(num)

