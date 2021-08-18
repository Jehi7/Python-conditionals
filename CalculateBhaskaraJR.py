import math

# Getting the data from the user
a = float(input("Type the constant a here: "))
b = float(input("Type the constant b here: "))
c = float(input("Type the constant c here: "))

# Processing data
delta = b**2 - 4 * a * c

# Validating and printing data
if delta > 0:
    x1 = ((-1 * b) + math.sqrt(delta)) / (2 * a) 
    x2 = ((-1 * b) - math.sqrt(delta)) / (2 * a) 
    print("the roots of your function are: " + str(x1) + " and " + str(x2) + ".")
    
elif delta == 0:
    x = (-1 * b) / (2 * a)
    print("The root of your function is: " + str(x))

else:
    print("This function doesn't have any real roots!")