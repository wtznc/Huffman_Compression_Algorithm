'''
	Advanced Algorithms and Data Structures
	FT BSc Computer Science (Year 3)
	Goldsmiths, University of London

	Static / Adaptive Huffman Coding
	by Wojciech Tyziniec

	"Huffman codes compress data very effectively: savings of 20% to 90% are typical,
	depending on the characteristics of the data being compressed. 
	We consider the data to be a sequence of characters. 
	Huffman's greedy algorithm uses a table giving how often each character occurs (i.e. its frequency) 
	to build up an optimal way of representing each character as a binary string. "

'''
import sys
import os


class ExternalDataLoader:
	def __init__(self, path):
		self.path = path
		self.fileHandle = open(path, "rb") 

	def printOutFileContent(self):
		return self.fileHandle.read()
		# print(self.fileHandle.read()) // instead of ^

	def close(self):
		if self.fileHandle:
			fileHandle.close()

	def getFileSize(self):
		fileStats = os.stat(self.path)
		size = fileStats.st_size
		return size

def main():
	choice = True
	print("Advanced Algorithms and Data Structures\nFT BSc Computer Science (Year 3)\nGoldsmiths, University of London\n\nStatic / Adaptive Huffman Coding\nby Wojciech Tyziniec\n")

	print("1. Input data\n2. Display the frequency table\n3. Compress\n4. Decompress\nX. Exit")
	while choice:
		choice = input("\nPlease, choose an option from the menu displayed above: ")
		if choice == "1":
			print("F. Read from file\nS. Get input string from the user")
			sub_choice = input("\nPlease, choose an option from the menu displayed above: ")
			if sub_choice == "F" or sub_choice == "f":
				path = input("\nEnter the file's path: ")
				dataLoader = ExternalDataLoader(path)
				#dataLoader.loadDataFromFile(path)
				print("You have loaded: ", dataLoader.printOutFileContent(), " which takes: ", dataLoader.getFileSize(), "bytes of space")
				dataLoader.printOutFileContent()
			elif sub_choice == "S" or sub_choice == "s":
				text = input("\nInput data you would like to compress: ")
				print(text)
			
		if choice == "2":
			print("I'm going to print out the frequency table.")

		if choice == "3":
			print("I'm going to compress the data.")

		if choice == "4":
			print("I'm going to decompress the data.")
			
		if choice == "X" or choice == "x":
			print("\nGoodbye!")
			choice = None
if __name__ == "__main__":
	main()