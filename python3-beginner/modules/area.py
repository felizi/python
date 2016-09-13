#Calculete area of circle area = PI x r²
import math

def Main():
	try:
		radius = float(input("Please enter a radius: "))
		area = math.pi * radius ** 2 # ** the power of
		print("Area:", area)
	except:
		print("You did not enter a number!")

if __name__ == "__main__":
	Main()
