number = int(input("Enter a random number: "))
if number == 0:
    print("Please enter a valid number, division by zero is impossible")
elif number % 2 == 0:
    print("The entered number is even")
else:
    print("The entered number is odd")
