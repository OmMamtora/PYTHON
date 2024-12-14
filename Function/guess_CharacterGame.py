import random

def guess(char):
    possible_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

    word = random.choice(possible_characters)

    if char == word:
        print("Correct guess!")
    else:
        print("Oops! The correct character was:", word)
    
    return word

char = input("Enter a Character: ")

guess(char)

