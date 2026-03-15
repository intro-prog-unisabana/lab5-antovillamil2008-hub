from secret_number import seed_secret_numbers, generate_secret_number
from response import input_response
contador=0
aciertos=False


semilla=int(input("Enter a seed number:\n"))
seed_secret_numbers(semilla)
    
secreto=generate_secret_number()

while not aciertos:
    guess=int(input("What is your guess:"))
    contador+=1
    message, guessed_correctly = input_response(secreto , guess)
    if guess<secreto:
        print("Too low! Try a higher number.")
    elif guess>secreto:
        print("Too high! Try a lower number.")
    else:
        print("Correct! You guessed the number!")
        break

print(f"It took you {contador} tries!")

