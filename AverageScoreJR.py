firstNumber = float(input("Type your first score: "))
secondNumber = float(input("Type your second score: "))
thirdNumber = float(input("Type your third score: "))

average = (firstNumber + secondNumber + thirdNumber)/3

if average > 60:
    print("You were approved!")
else:
    print("You weren't approved...")