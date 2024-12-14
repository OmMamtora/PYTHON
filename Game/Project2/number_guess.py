import random

def number_guess():
    num = random.randint(0, 100)

    max_attempt = 5
    for attempt in range(1,max_attempt+1):
        guess = int(input(f"Attempt number {attempt}/{max_attempt} enter any number between 0 to 100:->"))

        if guess == num:
            print("yupp! your guess is correct..")
            break
        elif guess < num:
           print("You guess is too low, Please try again..")
        else:
            print("Your guess is too high, Please try again..")
    else:
        print(f"Sorry! You've used all {max_attempt} attempts. The correct number was {num}.")

number_guess()