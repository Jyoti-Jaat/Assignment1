# task - 1: 

num1 = float(input("Enter the first number:"))

num2 = float(input("Enter the second number:"))

if(num2 == 0):
    print("Enter a valid second number other than zero!")
    
    num2 = float(input("Enter the second number:"))

Addition = num1 + num2
Substraction = num1 - num2
Multiplication = num1 * num2
Division = num1 / num2

print("Addition: ", Addition)
print("Substraction: ", Substraction)
print("Multiplication: ", Multiplication)
print("Division: ", Division)


