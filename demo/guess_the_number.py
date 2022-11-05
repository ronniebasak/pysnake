from random import randint

number = randint(1, 100)
MAX_TRIES = 7

def check_condition():
    if guess == number:
        print("Unbeatable! You won!!")
        return True
    elif guess < number:
        print("Try a higher number")
        return False
    else:
        print("Try a lower number")
        return False

is_win = False
for tries in range(MAX_TRIES):
    guess = int(input("Enter your guess: "))
    is_win = check_condition()
    if is_win:
        break
    else:
        print(f"You have {MAX_TRIES-tries-1} tries left")

if not is_win:
    print("You are out of tries, better luck next game!!")