from secret_number import generate_secret_number
from secret_number import seed_secret_numbers
contador=0

# print(numero_secreto)
while True:
    guess=int(input("What is your guess:"))
    if guess<secret_numbre:
        print("Too low! Try a higher number.")
        contador+=1
    elif guess>numero_secreto:
        print("Too high! Try a lower number.")
        contador+=1
    elif guess==numero_secreto:
        print("Correct! You guessed the number!")
        break

print(f"It took you {contador} tries!")
   