def Main():
	f = open("words", "r")
	for line in f:
		print(line)

	print("----------")
	
	f.seek(0)
	for line in f:
		print(line.strip("\n\r"))

	f.close()
if __name__ == "__main__":
	Main();