# checking if a number is negative, positive or zero
number = float(input("Enter a number to verify its sign: "))
if number >  0:
    print(f"The entered {number} is positive")
elif number == 0:
    print(f"The entered {number} is equal to zero")
else:
    print(f"The entered {number} is negative")
