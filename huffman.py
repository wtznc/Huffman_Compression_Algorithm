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
def main():
	choice = True
	print("Huffman Coding")
	print("1. Input data\n2. Display the frequency table\n3. Compress\n4. Decompress\nX. Exit")
	while choice:
		choice = input("\nPlease, choose an option from the menu displayed above: ")
		if choice == "1":
			print("Input your text: ")
			
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