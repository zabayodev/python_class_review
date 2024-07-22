import math as mt

# Enter the coefficiency of the quadratic equation
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

discriminant = b ** 2 - 4 * a * c
# For a positive discriminant
if discriminant > 0:
    root_1 = (-b + mt.sqrt(discriminant)) / (2 * a)
    root_2 = (-b - mt.sqrt(discriminant)) / (2 * a)
    print(f"Root_1 is: {root_1}")
    print(f"Root_2 is: {root_2}")
# For a discriminant equal to zero
elif discriminant == 0:
    root = -b / (2*a)
    print(f"Root is: {root}")
else:
# For a complex root
    real_part = -b / (2*a)
    imaginary_part = mt.sqrt(abs(discriminant)) / (2*a)
    print(f"Root 1 is: {real_part} + {imaginary_part}i")
    print(f"Root 2 is: {real_part} - {imaginary_part}i")




