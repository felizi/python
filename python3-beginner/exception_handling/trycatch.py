#load a text file called blah.txt (this doesn't actually exist)
import os

def Main():
	filename = "blah.txt"

	print(":: Tryng to open file ::")
	ReadFile(filename)

	print("\n:: Writing on file ::")
	WriteOnFile(filename, ["cat","hat","map","dot"])

	print("\n:: Reading file ::")
	ReadFile(filename)

	print("\n:: Deleting file ::")
	DeleteFile(filename)

def ReadFile(filename):
	try:
		f = open(filename, 'r')
		for line in f:
			print(line.strip("\n\r"))

		f.close()
	except:
		print("The file was either not found or unable to be read")
	finally:
		print("Exiting")

def WriteOnFile(filename, words):
	try:
		f = open(filename, 'w')

		for word in words:
			f.write(word + '\n')

		f.close()
		print("Write %s with success" % words)
	except:
		print("Fail on write words in file")
	finally:
		print("Exiting")

def DeleteFile(filename):
	if os.path.exists(filename):
	    os.remove(filename)
	    print("File removed with success")
	else:
	    print("Sorry, I can not remove %s file." % filename)

if __name__ == "__main__":
	Main()