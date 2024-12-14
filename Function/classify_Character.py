def classify_character(char):

    if char.lower() in 'aeiou':
        return "Vowel"
    
    elif char.isalpha(): 
        return "Consonant"
    
    elif char.isdigit():
        return "Digit"
    
    else:
        return "Special Character"

char = input("Enter a character: ")

if len(char) == 1:
    result = classify_character(char)
    print(f"The character '{char}' is a {result}.")
else:
    print("Please enter exactly one character.")
