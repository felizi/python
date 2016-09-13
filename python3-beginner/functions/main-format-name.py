def formatName(name):
	return "Hello, " + name + ". You're welcome!!"

def Main():
	print("Started")
	name = input("Enter your name: ")
	print(formatName(name))

if __name__ == "__main__":
	Main()