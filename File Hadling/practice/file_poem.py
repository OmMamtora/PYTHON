# Write a program to read the text from a given file 'poems.txt' and find out whether 
# it contains the word twinkle

found_twinkle = False
with open("F:/Python/File Hadling/practice/poem.txt") as f:
    lines = f.readlines()
    print(f.read())

    for line in lines:
        if "twinkle" in line:
            found_twinkle = True
            print(f"Twinkle word found in line :{line.strip()}")   
    print("Twinkle word occure in poem for",line.lower().count("twinkle"),"times")

if not found_twinkle:
    print("Twinkle word not in poem..")


