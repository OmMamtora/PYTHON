# Readlines read all the lines from file..

f = open("F:/Python/File Hadling/file_Read.txt")

lines = f.readlines()

print(lines , type(lines))

f.close()


# Readline read data line by line

f = open("F:/Python/File Hadling/file_Read.txt")

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))


file_line = f.readline()
while file_line != "":
    print(file_line,end="")
    file_line = f.readline()

f.close()