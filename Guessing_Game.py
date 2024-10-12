import random
secret_num = random.randint(1, 100)
guess_num = None
attempts = 0

print("Welcome To The Guessing Game ")
while guess_num != secret_num:
    guess_num = int(input("Enter Your Guess: "))  
    attempts += 1
    if guess_num > secret_num:
        print("Too High")
    elif guess_num < secret_num:
        print("Too Low")
    elif guess_num == secret_num:
        print(f"Your Guess is Correct! You found the number in {attempts} attempts.")
    else:
        print("Invalid Input")

