print("Let's find out if a number is odd or even.")
nr = int(input("Tell me some number: "))
rem1 = nr % 2

if rem1 is 0:
    print("This number is even.")
else:
    print("This number is odd.")

print("Now let's find out if one number is divisible by another one with or without remainder.")
first = int(input("Tell me the first number: "))
second = int(input("Tell me the second number: "))
rem2 = first % second

if rem2 is 0:
    print("The first number is divisible by the second number without remainder.")
else:
    print("The first number is divisible by the second number with remainder: " + str(rem2) + ".")