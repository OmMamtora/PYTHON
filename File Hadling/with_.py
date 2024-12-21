f = open("F:/Python/File Hadling/file_Read.txt")

print(f.read())
f.close()
# We can also perform using WITH statement..

with open("F:/Python/File Hadling/file_Read.txt") as f:
    print(f.read())