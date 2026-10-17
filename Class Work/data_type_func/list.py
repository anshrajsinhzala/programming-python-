"""



Here's why lists fit this use case :

Lists allow us to add,remove and change items.
A shopping cart can change.
Items in a list are ordered. A shopping cart shows items in the order they were added.
Lists allow duplicate values


cart = ["T-Shirt", "Lamp", "Pen"]    #list
print(cart)

my_list = [1,"python", 3.14 ]    #A list of mixed data types
print(my_list)

my_list = []  #Empty List
print(my_list)

Python List Methods

append()    adds an item to the end of the list
pop()       Returns and Removes the last item or item at the given index

insert()    Inserts an item at the specified index 
remove()    Removes the specified value from the list

clear()     Removes all items from the list
del(2)      Remove specific index list value
del         Remove list variable

extend()    Adds all the items from another list(or any other iterable)
index()     Returns the index of the first matched item
count()     Returns the count of the specified item
sort()      Sorts the list in ascending/descending order
reverse()   Reverse the list
copy()      Returns the shallow copy of a list

BUilt-in functions such as enumerate(), len() , nax() , min() , sorted() , etc.

"""