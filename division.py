number_1 = float(input("Enter the dividend for the division: "))
number_2 = float(input("Enter the divisor for the division: "))
if number_2 == 0:
    print(f"Error, Division by 0 is not allowed.")
else:
    division_result = number_1 / number_2
    print(f"Division of {number_1} with {number_2} is {division_result}")
