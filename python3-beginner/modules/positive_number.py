#Our program will get an number from the user and make sure that its always positive
#We will use math.fabs(x) where x is will be made absolute. (negatives will be made positive)

import math

def Main():
	try:
		number = float(input("Please enter a number: "))
		number = math.fabs(number)
		print(number)
	except:
		print("You did not enter a number!")

if __name__ == "__main__":
	Main()