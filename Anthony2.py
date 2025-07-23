import math

#Get the first number
number1 = float(input("Enter first number: "))
#Get the second number
number2 = float(input("Enter second number: "))

print("_____________________________")
print()

#Addition operation of num1 and num2
print("The sum of number1 and number2 is: ", number1 + number2)
print()

#Multiplication operation of num1 and num2
print("The product of number1 and number2 is: ", number1 * number2)
print()

#Division operation of num1 and num2
print("The quotient of number1 and number2 is: ", number1 / number2)
print()

#Floor Division operation of num1 and num2
print("The floor division of number1 and number2 is: ", number1 // number2)
print()

#Subcation operation of num1 and num2
print("The difference of number1 and number2 is: ", number1 - number2)
print()

#Exponent Operation of num1 and num2
print("The exponent of number1 and number2 is: ", number1 ** number2)
print()

#Module operation of num1 and num2
print("The remainder of number1 and number2 is: ", number1 % number2)
print()

#The square root of number1
print("The square root of number1 is: ", math.sqrt(abs(number1)))
print()

#The square root of number2
print("The square root of number2 is: ", math.sqrt(abs(number2)))
print()

#Remainder after division
print(f"{number1} % {number2} = {number1 % number2}")