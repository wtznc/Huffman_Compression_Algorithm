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
import logging
import sys
import os
import queue as Q
class Huffman:
	def __init__(self, content):
		self.content = content
		self.frequencyTable = {}

class ExternalDataLoader:
	def __init__(self, filePath):
		self.filePath = filePath
		self.fileHandle = open(self.filePath, "r") # At this point we want to read only ASCII representation of characters, not bytes yet, as we have to build a frequency table, thus we're using "r" not "rb"
		
		self.data = self.fileHandle.read()
		self.frequencyTable = {}

	def buildFrequencyTable(self):
		for c in self.data:
			if c not in self.frequencyTable:
				self.frequencyTable[c] = 1
			else:
				self.frequencyTable[c] += 1
		print("Type of 'frequencyTable' = ", type(self.frequencyTable))

	def closeFileHandle(self):
		if self.fileHandle:
			fileHandle.close()

	def getFileContent(self):
		return self.fileHandle.read()

	def getFileSize(self):
		return os.path.getsize(self.filePath)

	def printOutFrequencyTable(self):
		self.frequencyTable = sorted(self.frequencyTable.items(), key=lambda x:x[1], reverse=True)
		for x in range(0, len(self.frequencyTable)):
			print(self.frequencyTable[x])

def main():
	logging.basicConfig(format='%(asctime)s %(message)s')
	# Printing menu
	print("Advanced Algorithms and Data Structures\nFT BSc Computer Science (Year 3)\nGoldsmiths, University of London\n\nStatic / Adaptive Huffman Coding\nby Wojciech Tyziniec\n")
	data = ""

	# Perform the main loop until user enters X or x to exit
	choice = True
	while choice:
		print("1. Input data\n2. Display sorted frequency table\n3. Compress\n4. Decompress\nX. Exit")
		choice = input("\nPlease, choose an option from the menu displayed above: ")

		if choice == "1":
			path = input("\nEnter the file's path: ")
			logging.warning("Loading data...")
			dataLoader = ExternalDataLoader(path)
			logging.warning("Finished loading data!")
			if(len(dataLoader.data) > 100):
				print("Loading successful! Your file takes: ", dataLoader.getFileSize(), "bytes of space\n")
			else:
				print("You have loaded: ", dataLoader.data, " which takes: ", dataLoader.getFileSize(), "bytes of space.\n")
			data = dataLoader.data

		if choice == "2":
			print("I'm going to print out the frequency table. \n")
			huffman = Huffman(data)
			dataLoader.buildFrequencyTable()
			dataLoader.printOutFrequencyTable()

		if choice == "3":
			print("I'm going to compress the data.")





















		if choice == "4":
			print("I'm going to decompress the data.")
			
		if choice == "X" or choice == "x":
			print("\nGoodbye!")
			choice = None
if __name__ == "__main__":
	main()