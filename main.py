from utils import *

def main():
    while True:
        operacion = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):\n").lower()
        if operacion == 'exit':
            break
        operaciones_validas = ['add', 'subtract', 'multiply', 'divide', 'exponent', 'modulo', 'floor_divide', 'absolute']
        if operacion not in operaciones_validas:
            print("Invalid option!")
            continue
        if operacion == 'absolute':
            num = float(input("Enter the number:\n"))
            result = absolute(num)
            print(f"The result is: {result}")
        else:
            n1 = float(input("Enter the first number:\n"))
            n2 = float(input("Enter the second number:\n"))
            
            if operacion == 'add': result = add(n1, n2)
            elif operacion == 'subtract': result = sub(n1, n2)
            elif operacion == 'multiply': result = multiply(n1, n2)
            elif operacion == 'divide': result = divide(n1, n2)
            elif operacion == 'exponent': result = exponent(n1, n2)
            elif operacion == 'modulo': result = modulo(n1, n2)
            elif operacion == 'floor_divide': result = floor_divide(n1, n2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"The result is: {result}")

if __name__ == "__main__":
    main()