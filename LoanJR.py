# Getting the data from the user
value = float(input("Type here the loans value (only the number): "))
installments = float(input("Type here the amount of installments the loan will be divided: "))
salary = float(input("Type here your salary: "))

# Processing data
dividedValue = value/installments

print(dividedValue)

# Validating and printing data
if salary >= dividedValue * 3:
    print("Loan accepted!")
else:
    print("Loan denied!")