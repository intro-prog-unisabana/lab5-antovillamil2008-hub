from utils import *

mensaje=input("Please type your message\n")
mensaje_reverseado=flip(mensaje)
a=count_letters(mensaje, 'a')
mensaje_codificado=mensaje_reverseado + str(a)
print(f"Your encoded message is: {mensaje_codificado}")