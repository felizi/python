def multipy(num1, num2):
	return num1 * num2

def sum(num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2

def divide(num1, num2):
	return num1 / num2

def Main():
	print("Multiply")
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))
	print("Result: " + str(num1) + " x " + str(num2) + " = " + str(multipy(num1, num2)))

	print("Sum")
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))
	print("Result: " + str(num1) + " + " + str(num2) + " = " + str(sum(num1, num2)))

	print("Subtract")
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))
	print("Result: " + str(num1) + " - " + str(num2) + " = " + str(subtract(num1, num2)))

	print("Divide")
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))
	print("Result: " + str(num1) + " / " + str(num2) + " = " + str(divide(num1, num2)))

if __name__ == "__main__":
	Main()