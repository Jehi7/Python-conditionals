# Getting the data from the user
age = int(input("Type here your age: "))

# Validating and printing data
if age < 9:
    print("Você é um nadador mirim!")
elif age >= 9 and age < 14:
    print("Você é um nadador infantil!")
elif age >= 14 and age < 18:
    print("Você é um nadador juvenil!")
elif age >= 18:
    print("Você é um nadador adulto!")