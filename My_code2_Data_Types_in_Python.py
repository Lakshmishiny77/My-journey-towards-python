##"Data types are the classification or categorization of data items.
##It represents the kind of value that tells what operations can be performed on a particular data.
##Since everything is an object in Python programming, data types are actually classes and
##variables are instance (object) of these classes"

##Classifications of Data Types in Python

##Mutable and Immutable Objects

##2.1 Mutable Data types in Python 1. List 2.Dictionary 3.Set

##Let us start with 1.List                                     - in python we use [  ] - for list

var = ["github"]
print(type(var))  #This print will give you the type of variable 

#we have few built-in functions of list as follows

##1.append - The append() method appends an element to the end of the list

my_list = ['google', 'microsoft', 'apple']
my_list.append("amazon")
print(my_list)

##2.clear - The clear() method removes all the elements from a list.

##my_list = ['google', 'microsoft', 'apple']
##my_list.clear()
##print(my_list)

##3.copy - The copy() method returns a copy of the specified list.

##my_list = ['google', 'microsoft', 'apple']
##x = my_list.copy()
##print(x)

##4.count - The count() method returns the number of elements with the specified value.

##my_list = ['google','apple', 'microsoft', 'apple']
##x = my_list.count('apple')
##print(x)

##5.extend - The extend() method adds the specified list elements (or any iterable) to the end of the current list.

##my_list = ['google','apple', 'microsoft', 'apple']
##cars = ['Ford', 'BMW', 'Audi']
##my_list.extend(cars)
##print(my_list)

##6.index - The index() method returns the position at the first occurrence of the specified value.

##my_list = ['google', 'microsoft', 'apple']
##x = my_list.index("microsoft")
##print(x)

##7.insert - The insert() method inserts the specified value at the specified position.

##my_list = ['google', 'microsoft', 'apple']
##my_list.insert(1, "instagram")
##print(my_list)

##8.pop - The pop() method removes the element at the specified position.

##my_list = ['google', 'microsoft', 'apple','orange']
##my_list.pop()       #- here it will delete the last element from the list
####my_list.pop(1)   #- also you can specifically mention index no.
##print(my_list)

##9.remove - The pop() method removes the specified index.

##my_list = ['google', 'microsoft', 'apple','banana']
##my_list.remove("banana")
##print(my_list)

##10.reverse - The reverse() method reverses the sorting order of the elements.

##my_list = ['google', 'microsoft', 'apple']
##my_list.reverse()
##print(my_list)

##11.sort - The sort() method sorts the list ascending by default.

##my_list = ['google', 'microsoft', 'apple']
##my_list.sort()
##print(my_list)

print("\nThank you")

print("\t\t-learning is the never ending process \U0001f600")



