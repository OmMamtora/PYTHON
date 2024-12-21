# Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13-year old.

import random

def tableGenerate():
    number = random.randint(2,20)
    table=""
    for i in range(1,11):
        table += f"{number} X {i} = {number*i}\n"
    
    with open(f"F:/Python/File Hadling/practice/tables/table_{number}.txt","w") as f:
        f.write(table)

tableGenerate()