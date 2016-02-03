shopping_list = ["milk", "bread", "eggs", "quinoa"]

#function definitions:

def remove_item(item):
	shopping_list.remove(item)
	shopping_list.sort
	print shopping_list


#options

print "Select a choice:"
print "Type 1 to add a item"
print "Type 2 to remove an item"
print "type 3 to replace an item"
print "type 4 to show total number of items on list"
choice = int(raw_input())


#add an item
if choice ==1:
	new_item = raw_input("What do you want to add?")
	if new_item in shopping_list:
		print "you already have this item in your list"
	else:
		shopping_list.append(new_item)
		shopping_list.sort()
		print shopping_list

#remove an item
if choice == 2:
	show_list = str.lower(raw_input("Do you want to see your existing list?"))
	if show_list == "yes":
		print shopping_list

	delete_item = raw_input("What item would you like to remove?")
	if delete_item not in shopping_list:
		print "This item is not in the list"
		print "Your shopping list currently has", shopping_list
	else:
			remove_item(delete_item)

#replace an item

if choice == 3:
	old_item = raw_input("What item do you want to replace?")
	new_item = raw_input("What item do you want to replace it with?")
	if old_item not in shopping_list:
		print "This item is not in the list"
		print "Your shopping list currently has", shopping_list
	else:
		shopping_list[shopping_list.index(old_item)]=new_item
		shopping_list.sort()
		print shopping_list

#total items in list

if choice == 4:
	print "Your shopping list has", len(shopping_list), "items"