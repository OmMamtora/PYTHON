#Print the first 10 natural numbers.
for i in range(0,10):
    print(i)

# Calculate the sum of numbers from 1 to n (where n is provided by the user).

num = int(input("Enter Number:->"))
sum = 0

for n in range(1, num+1):
    sum += n
print(f"Sum of numbers from 1 to {num} is {sum}")


# Print the multiplication table for a given number.

number = int(input("Enter number for multiplication:->"))

for m in range(1,11):
    multi = number * m
    print(f"{number} * {m} = {multi} ")


# Count the number of vowels in a given string.

str = "Om Mamtora"
count =0
for s in str:
    print(s)
    if(s=="A" or s=="a" or s=="E" or s=="e" or s=="I" or s=="i" or s=="O" or s=="o" or s=="U" or s=="u"):
        count+=1
print("Vowels are",count)

lst = ["A","a","E","e","I","i","O","o","U","u"]
count = 0


name = input("Enter Name:->")
for char in name:
    if char in lst:
        count += 1
print(count)


# Reverse a given string using a loop.

good_name = "Om Mamtora"
reverse_name = ""

for x in good_name:
    reverse_name = x+reverse_name
print(reverse_name)

# Find the factorial of a number using a for loop.

digit = int(input("Enter Number for factorial:->"))
fact=0
for d in range(1,digit+1):
    fact*=d
print(f"Factorial of number {digit} is {fact}")

# Print all prime numbers between 1 and 100.

for num in range(2, 101):
    is_prime = True
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break 
    if is_prime:
        print(num)

# Find particular number is prime or not.

p_number = int(input("Enter number:->"))

if p_number < 1:
    print("not prime number..")
elif p_number == 2:
    print("Prime number")
else:
    is_prime = True
    for p in range(2,int(p_number**5)+1):
        if p_number % 2 == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{p_number} is a prime number.")
    else:
        print(f"{p_number} is not a prime number.")

# By giving particular range display prime number
range_limit = int(input("Give range for prime number:->"))

if range_limit < 1:
    print(f"{range_limit}Not Prime number..")
elif range_limit == 2:
    print(f"{range_limit}Prime number..")
elif range_limit > 2:
    for r_number in range(2,range_limit+1):
        is_prime = True

        for y in range(2,int(r_number**0.5)+1):
            if r_number % y == 0:
                is_prime=False
                break
        if is_prime:
            print(f"Prime numbers are: {r_number}")

# Generate a Fibonacci sequence up to n terms.

fibonacci_number = int(input("Enter number:->"))

a=0
b=1

for f in range(fibonacci_number):
    print(a,end=" ")
    a,b = b,a+b