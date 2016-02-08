#input
plaintext = raw_input("Enter the text that you want to decrypt: ")
key1 = int(raw_input("Enter key value 1: "))
key2 = int(raw_input("Enter key value 2: "))
#key3 = int(raw_input("Enter key value 3: "))
 

#step 1: converting to int
number_list = [ord(letter) for letter in plaintext]
print "step 1: ", number_list


#step 2: multiply by key1 and key2
for section in number_list:
	even = int(section)%2
	if even == 0:
		mult = key1
	else: mult = key2

multiplied = [ord(letter)*mult for letter in plaintext]
print "step 2: ", multiplied


#step 3: Reverse each section
def scramble(multiplied):
	index = 0
	while index < len(multiplied):
		multiplied[index] = str(multiplied[index])[::-1] #reverse order
		index += 1
	return multiplied

reverse = scramble(multiplied)
print "step 3: ", reverse







# to encrypt: 
#1: ord() * keyvalue1
#2: chunk it up into sections of keyvalue2, and then put in inverse order
#3: oct()

# to decrypt:
#3: chr() then divide by keyvalue1
#2: chunk up sections, place in reverse order
#1: 
