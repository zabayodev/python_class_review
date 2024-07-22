variable_1 = input("Enter the length of a variable 1: ")
variable_2 = input("Enter the length of variable 2: ")

# Print the original value
print(f" The original variable are variable_1 = {variable_1} and variable_2 = {variable_2}")

# Swap the variable using temporary variable
temp = variable_1
variable_1 = variable_2
variable_2 = temp

print(f"Swapped values: variable_1 = {variable_1}, variable_2 = {variable_2}")
