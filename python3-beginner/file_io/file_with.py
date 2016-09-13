def Main():
	words = ["cat", "sat", "bat", "map"]

	with open("write_with", 'w') as f:
		for word in words:
			f.write(word + '\n')

	f.close()

if __name__ == "__main__":
	Main();
