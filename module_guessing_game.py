import random
print("Guessing Game: ")
magic_number = random.randint(1, 50)
guess = None
attempts = 0

while guess != magic_number:
    guess = int(input("Enter a number between [1, 50]"))
    attempts += 1
    
    if guess < magic_number:
        print("Try Higgher")
    
    elif guess > magic_number:
        print("Try Lower")

    else:
        print(f"You got correct ans i.e. {magic_number} in {attempts} attemps")