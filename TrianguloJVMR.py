x = input("Type here the length of the side x of your triangle: ")
y = input("Type here the length of the side y of your triangle: ")
z = input("Type here the length of the side z of your triangle: ")

if x == y == z:
    print("This is an equilateral triangle.")
elif x == y or x == z or y == z:
    print("This is an isosceles triangle.")
elif x != y != z:
    print("This is a scaleno triangle")