# 4. A file contains a word "Donkey" multiple times. You need to write a program which 
# replace this word with "Monkey" by updating the same file.

def wordReplace():

    with open("F:/Python/File Hadling/practice/replace_word.txt","r") as f:
        lines = f.readlines()
        print(lines)

    modified_lines=[]
    for line in lines:
        modified_line = line.replace("Donkey","Monkey")
        modified_lines.append(modified_line)
    
    with open("F:/Python/File Hadling/practice/replace_word.txt","w") as f:
        f.writelines(modified_lines)

    print("Donkey has been replaced with Monkey")


wordReplace()