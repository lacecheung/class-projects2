sequence = raw_input("Enter the sequence that you want to decrypt, separated with commmas: ")
key1 = int(raw_input("Enter key value 1: "))
key2 = int(raw_input("Enter key value 2: "))
print

print "Results: "
print 

#create list:
sequence = sequence.split(",")

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

print "Decrypted ", "".join(decrypted)
print

