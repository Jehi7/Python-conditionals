birthYear = int(input("Type here your birth year: "))
currentYear = int(input("Type here the current year: "))

age = currentYear - birthYear

if age >= 18:
    print("You are an adult!")
else:
    print("You aren't an adult.")