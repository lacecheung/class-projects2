#Part 1 - For Loops (Week 9)

#Q7
def for_loop_sum_num(num):
	total = 0
	for item in range(0,num + 1):
		total = total + item
	print "For Loop: The total of 0 to", num, "is", total

#for_loop_sum_num(3)


# Part 1 - While Loops Exercise (Week 9)

# Q7
def sum_nums(num):
	index = 0
	sum = 0
	if num < 0:
		while index >= num:
			sum = sum + index
			index += -1
		print "The sum of all numbers from 0 to", num, "is", sum
	else:
		while index <= num:
			sum = sum + index
			index += 1
		print "The sum of all numbers from 0 to", num, "is", sum

#test cases:
	#sum_nums(3)
	#sum_nums(-3)



#Week 9 homework

#Q1:

def show_message(message, repitition):
	for item in range(repitition):
		print message

#ASK: How do I only show these questions if the function show_message is called?
#message = raw_input("Type a message: ")
#repitition = int(raw_input("How many times do you want the message displayed?"))

#show_message(message, repitition)

#Q2
#for item in range(1500,2701):
	if item%5 == 0 and item%7 == 0:
		print item, "is divisible by 5 and 7"

#Q3
def find_num(a,b):
	for item in range(a, b+1):
		if item%2 != 0:
			print item


#Q4

string = "g9aB0iza5rvlugFxAQnzxYjzjUVzRjajEJ7P25FcwWHt4VYbOoSgGo5I8H94zOsBP0tAkq3dBurhinusxonARhdcy44zOjdOMyJdz8rqtOmZeimLY9rHkEvdauricalYh6x65Jy3ZFTS3F303GdMZr7YVgwN9o4Ouo"

def secret_message(string, a, b,c,d):
		print string[a:b+1], string[c:d+1]

#secret_message(string, 72,79,119,125)

#Q5

print "Please enter your email address:"
email = raw_input()


def valid(email):
	if "@" not in email or ".com" not in email:
		print "Error: missing @ or .com"
	elif email.index(".com") < email.index("@"):
		print "Error: Arguments are in the wrong position"
	elif email.index("@") == 0:
		print "Error: Email address cannot being with @"
	elif len(range(email.index("@")+1,email.index(".com"))) == 0:
		print "Error: second argument missing"
	elif len(email) - email.find(".com") != 4:
		print "Error: No arguments expected after .com"
	else:
		print "Your email is good to go!"

valid(email)



