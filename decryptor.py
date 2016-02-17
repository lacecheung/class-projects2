print "Do you want to type in your code or open from a file?"
print "1: Type in"
print "2: open from file"
open_option = int(raw_input())

if open_option == 1:
	sequence = raw_input("Enter the sequence that you want to decrypt, separated with a space eg. 304 603 493")
	sequence = sequence.split(" ")
elif open_option == 2:
	file_location = raw_input("type in file location. eg. C:\\Users\\Desktop\\encrypted_message.txt")
	with open(file_location) as my_file:
		sequence = my_file.readlines()
		print "Your code has been successfully uploaded"


key1 = int(raw_input("Enter key value 1: "))
key2 = int(raw_input("Enter key value 2: "))
print

print "Results: "
print 


#create list:

print "List form: ", sequence


#step 1: reverse order:
def unscramble(sequence):
	return sequence[::-1]

unscrambled = unscramble(sequence)

print "Step 1: ", unscrambled



#step 2: unreverse each element
unreverse = [element[::-1] for element in unscrambled]

print "Step 2: ", unreverse



#step 3: divide by key values
def divide(unreverse):
 for index, element in enumerate(unreverse,0):
 	if index%2 == 0:
 		unreverse[index] = int(element) / key1
 	else:
 		unreverse[index] = int(element) / key2
 return unreverse

divided = divide(unreverse)

print "Step 3: ", divided
print



#step 4: Change back to ascii
decrypted = [chr(element) for element in divided]

print "Decrypted: ", "".join(decrypted)
print

