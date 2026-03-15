import random
random.seed(123)
inicio=int(input("Enter the start value:\n"))
final=int(input("Enter the end value:\n"))
numero=random.randint(inicio, final)
print(f"Generated random number: {numero}")