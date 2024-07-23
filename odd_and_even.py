number = int(input("Enter a random number: "))
if number % 2 == 0:
    print("The entered number is even")
elif number == 0:
    print("Please enter a valid number, division by zero is impossible")
else:
    print("The entered number is odd")
