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
from heapq import heappush, heappop, heapify
from collections import defaultdict
import os
import collections

class DataLoader:
	def __init__(self, filePath):
		self.filePath = filePath
		self.fileHandle = open(self.filePath, "r")
		self.data = self.fileHandle.read()

	# Build a dictionary of characters and corresponding frequencies
	def buildFrequencyTable(self):
		self.frequencyTable = defaultdict(int)
		for c in self.data:
			if c not in self.frequencyTable:
				self.frequencyTable[c] = 1
			else:
				self.frequencyTable[c] += 1
		print("Type of 'frequencyTable' = ", type(self.frequencyTable))

	# Print out the frequency table in desc order
	def printOutFrequencyTable(self):
		self.frequencyTableSorted = sorted(self.frequencyTable.items(), key=lambda x:x[1], reverse=True)
		for x in range(0, len(self.frequencyTableSorted)):
			print(self.frequencyTableSorted[x])

		# Testing
		#for char, freq in self.frequencyTable.items():
			#print("Char = ", char, ", freq = ", freq)

	# Helper function which returns size of the loaded file
	def getFileSize(self):
		return os.path.getsize(self.filePath)

	# Function takes as an input a frequency table and returns corresponding huffman codes
	def returnHuffmanCodes(self):
		# I'm using priority queue as main data structure
	    pqueue = [[frequency, [character, ""]] for character, frequency in self.frequencyTable.items()]

	    # To keep in order (lowest freq - highest freq)
	    heapify(pqueue)

	    # While there are nodes in our priority queue,
	    # we want to merge two nodes with the lowest frequency
	    while len(pqueue) > 1:
	        first = heappop(pqueue) # first node with lowest freq
	       	#print("first = ", first)
	        second = heappop(pqueue) # second node with lowest freq 
	       	#print("second = ", second)
	        for merge in first[1:]:
	            merge[1] = '0' + merge[1]
	        for merge in second[1:]:
	            merge[1] = '1' + merge[1]
	        heappush(pqueue, [first[0] + second[0]] + first[1:] + second[1:]) # add recently combined nodes to the priority queue
	    # sort the list in asc order by length of huff code
	    return sorted(heappop(pqueue)[1:], key=lambda p: (len(p[-1]), p))

def main():
	print("Advanced Algorithms and Data Structures\nFT BSc Computer Science (Year 3)\nGoldsmiths, University of London\n\nImplementation of Huffman Encoding Algorithm\nby Wojciech Tyziniec\n")
	choice = True
	data = ""
	dataLoader = ""

	# Perform the main loop until user enters X or x to exit
	while choice:
			print("\n1. Input data\n2. Build and display sorted frequency table\n3. Encode and display huffman codes\nX. Exit")
			choice = input("\nPlease, choose an option from the menu displayed above: ")

			if choice == "1":
				print("Example files: \n- long.txt,\n- short.txt")
				path = input("\nEnter the file's path: ")
				# Load a file from the given path
				dataLoader = DataLoader(path) 

				# If length of our data is > 100, we dont want to print it out, so im printing its overall size.
				if(len(dataLoader.data) > 100):
					print("Loading successful! Your data takes up: ", dataLoader.getFileSize(), "bytes of space\n")
					print("Next step is to build a frequency table!\n\n")
				else:
					print("You have loaded: ", dataLoader.data, " which takes: ", dataLoader.getFileSize(), "bytes of space.\n")
					print("Next step is to build a frequency table!\n\n")
				data = dataLoader.data

			if choice == "2":
				# If data has not been correctly loaded or is empty, we cannot build freq table
				if data != "":
					dataLoader.buildFrequencyTable()
					dataLoader.printOutFrequencyTable()
					print("Great! You're ready to compress the data!\n\n")
				else:
					print("\nFirst you need to enter some data!")

			if choice == "3":
				# If data has not been correctly loaded or is empty, we cannot build freq table
				if isinstance(dataLoader, str):
					print("First you need to load up some data!")
				else:
					print("Going to compress and print out tuples containing (character, frequency, corresponding huffman code).")
					codes = dataLoader.returnHuffmanCodes()
					for x in codes:
						print (x[0], dataLoader.frequencyTable[x[0]], x[1])
					print("There you go! My pleasure :)")

			if choice == "X" or choice == "x":
				print("Goodbye!")
				break;

if __name__ == "__main__":
	main()