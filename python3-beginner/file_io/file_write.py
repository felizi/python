def Main():
	f = open("write", "w")

	for i in range(4):
		f.write(input("Please enter a word: ") + '\n')

	f.close()

if __name__ == "__main__":
	Main();
