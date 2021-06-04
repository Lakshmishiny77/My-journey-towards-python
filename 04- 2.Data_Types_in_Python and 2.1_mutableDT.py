##2. DATA TYPES

##"Data types are the classification or categorization of data items.
##It represents the kind of value that tells what operations can be performed on a particular data.
##Since everything is an object in Python programming, data types are actually classes and
##variables are instance (object) of these classes"

##Classifications of Data Types in Python

##Mutable and Immutable Objects

##2.1 MUTABLE DATA TYPES IN PYTHON
##     1. List
##     2.Dictionary
##     3.Set

##2.1.1 LIST
##The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets.
##Important thing about a list is that items in a list need not be of the same type.
##Lists are used to store multiple items in a single variable.
##Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
##Lists are created using square brackets.

var = ["github"]
print(type(var))  #This print will give you the type of variable 

##Creating a List

##Lists in Python can be created by just placing the sequence inside the square brackets[].
##Unlike Sets, list doesn’t need a built-in function for creation of list.Unlike Sets, list may contain mutable elements.

# Creating a List
##List = []
##print("Blank List: ")
##print(List)

# Creating a List of numbers
##List = [10, 20, 14]
##print("\nList of numbers: ")
##print(List)
  
# Creating a List of strings and accessing using index
##List = ["Amazon", "For", "Online", "Shopping"]
##print("\nList Items: ")
##print(List[0]) 
##print(List[2])
  
# Creating a Multi-Dimensional List (By Nesting a list inside a List)
##List = [['Facebook', 'Instagram'] , ['Whatsapp']]
##print("\nMulti-Dimensional List: ")
##print(List)


# Creating a List with  the use of Numbers (Having duplicate values)
##List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
##print("\nList with the use of Numbers: ")
##print(List)
  
# Creating a List with mixed type of values (Having numbers and strings)
##List = [1, 2, 'Apple', 4, 'For', 6, 'iphone']
##print("\nList with the use of Mixed Values: ")
##print(List)

#we have few built-in functions of list as follows

##1.append - The append() method appends an element to the end of the list

##my_list = ['google', 'microsoft', 'apple']
##my_list.append("amazon")
##print(my_list)

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



