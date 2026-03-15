import os
import math 

#Parte 1
directorio_actual = os.getcwd()
print(f"Current working directory: {directorio_actual}")

#Parte 2
entero=int(input("Enter an integer:"))
logaritmo=math.log2(entero)
print(f"Log base 2 of {entero} is: {logaritmo}")

#Parte 3
techo=math.ceil(logaritmo)
floor=math.floor(logaritmo)
print(f"Floor: {floor}")
print(f"Ceiling: {techo}")

