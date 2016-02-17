#input
plaintext = raw_input("Enter the text that you want to encrypt: ")
key1 = int(raw_input("Enter key value 1: "))
key2 = int(raw_input("Enter key value 2: "))
#key3 = int(raw_input("Enter key value 3: "))

print
print "Results:"
print 


#step 1: converting to int
number_list = [ord(letter) for letter in plaintext]

print "step 1: ", number_list


#step 2: multiply by key1 and key2 based on if the index is even or odd
def multiply(number_list):
 for index, element in enumerate(number_list,0):
 	if index%2 == 0:
 		number_list[index] = key1 * element
 	else:
 		number_list[index] = key2 * element
 return number_list	

multiplied = multiply(number_list)

print "Step 2: ", multiplied	


#step 3: Reverse each section
def scramble(multiplied):
	index = 0
	while index < len(multiplied):
		multiplied[index] = str(multiplied[index])[::-1] #reverse order
		index += 1
	return multiplied

reverse = scramble(multiplied)

print "step 3: ", reverse
print


#step 4: convert to int. 
#NOTE: is there any way to keep int format without losing leading zeroes?
def scramble(reverse):
	return reverse[::-1]

print "Encrypted: "
for item in scramble(reverse):
	print item,

encrypted_message = scramble(reverse)


#step 5: write to text file
create_file = raw_input("\n"+"Do you want to create a new file with this code?")

if create_file.lower() == "yes":
	print "Where to you want to save this file?"
	print "1: Current directory"
	print "2: Custom File path"
	location_option = int(raw_input())

	if location_option == 1:
		file_location = "encrypted_message.txt"
	elif location_option == 2:
		file_location = raw_input("Type in file path. eg. ~\\Desktop\\")+"encrypted_message.txt"


	new_file = open(file_location, "w")
	for section in encrypted_message:
		new_file.write(section + "\n")
	new_file.close()
	print "Your file has been successfully saved as", file_location









