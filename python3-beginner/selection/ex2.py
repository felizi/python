num1 = int(input("Please enter your fisrt number: "))
num2 = int(input("Please enter your second number: "))

if num1 > num2:
	print("The first number is greater than second number.")
	print("The difference is "+ str(num1 - num2))
elif num1 < num2:
	print("The first number is less than first number.")
	print("The difference is "+ str(num1 - num2))
else:
	print("The numbers are equal.")