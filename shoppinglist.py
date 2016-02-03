shopping_list = ["milk", "bread", "eggs", "quinoa"]

print "Select a choice:"
print "Type 1 to add a item"
print "Type 2 to remove an item"
print "type 3 to replace an item"
print "type 4 to show total number of items on list"
choice = int(raw_input())

if choice ==1:
	new_item = raw_input("What do you want to add?")
	if new_item in shopping_list:
		print "you already have this item in your list"
	else:
		shopping_list.append(new_item)
		shopping_list.sort()
		print shopping_list

