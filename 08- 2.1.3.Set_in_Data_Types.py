##2.1.2. SET

##A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements.
##Python’s set class represents the mathematical notion of a set.
##The major advantage of using a set, as opposed to a list, is that it has a highly optimized methodfor checking whether a specific element is contained in the set.
##This is based on a data structure known as a hash table.Since sets are unordered, we cannot access items using indexes like we do in lists.
##Sets are used to store multiple items in a single variable.
##Set is one of 4 built-in data types in Python used to store collections of data,the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
##A set is a collection which is both unordered and unindexed.Sets are written with curly brackets.

set = {"apple", "banana", "cherry"}
print(type(set))  #This print will give you the type of variable

##Creating a Set

##A set is created by using the set() function or placing all the elements within a pair of curly braces.

##Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
##Months={"Jan","Feb","Mar"}
##Dates={21,22,17}
##print(Days)
##print(Months)
##print(Dates)

# Distinguish set and dictionary while creating empty set

##a = {}                      # initialize a with {}
##print(type(a))          # check data type of a

##a = set()                   # initialize a with set()
##print(type(a))          # check data type of a

##To determine how many items a set has, use the len() method.

##set = {"apple", "banana", "cherry"}
##print(len(set))

# Different types of sets in Python

##set1 = {"apple", "banana", "cherry"}    #string
##set2 = {1, 5, 7, 9, 3}                          #int
##set3 = {True, False, False}                 #boolean
##print(set1)
##print(set2)
##print(set3)

##A set can contain different data types:
##set4 = {"abc", 34, True, 40, "male"}
##print(set4)

# set cannot have duplicates
##my_set = {1, 2, 3, 4, 3, 2}
##print(my_set)

# we can make set from a list
##my_set = set([1, 2, 3, 2])
##print(my_set)

##Using the set() constructor to make a set:

##thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
##print(thisset)

# set cannot have mutable items here [3, 4] is a mutable list this will cause an error.
##my_set = {1, 2, [3, 4]}
  
#we have few Python Set Methods as follows

##1.add - Adds an element to the set
#Syntax = set.add(elem)         - add() takes single parameter(elem) which needs to be added in the set.

##Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
##Days.add("Sun")
##print(Days)

##2.clear - Removes all elements from the set
#Syntax = set.clear()               - The clear() method doesn't take any parameters.

##vowels = {'a', 'e', 'i', 'o', 'u'}
##print('Vowels before clear:', vowels)
##vowels.clear()                                # clearing vowels
##print('Vowels after clear:', vowels)

##3.copy - The copy() method returns a shallow copy of the set in python.
##              If we use “=” to copy a set to another set, when we modify in the copied set, the changes are also reflected in the original set.
##              So we have to create a shallow copy of the set such that when we modify something in the copied set, changes are not reflected back in the original set.

##Syntax: set_name.copy()   - set_name: Name of the set whose copy we want to generate. The copy() method for sets doesn’t take any parameters.

#example1:
##set1 = {1, 2, 3, 4} 
##set2 = set1.copy()  # function to copy the set
##print(set2)

#example2:created using set copy is shallow
##first = {'a', 'e', 'i', 'o', 'u'} 
##second = first.copy() # before adding
##print ('before adding: ')
##print ('first: ',first)
##print ('second: ', second) 
  
#example3:Adding element to second, first does not change.
##second.add('f')            # after adding
##print ('after adding: ')
##print ('first: ', first)
##print ('second: ', second)

##4.difference - The difference() method returns a set that contains the difference between two sets.
##                        Meaning: The returned set contains items that exist only in the first set, and not in both sets.

##Syntax = set.difference(set) - Parameter set - Required. The set to check for differences in

##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##z = y.difference(x)
##print(z)

##5.difference_update - The difference_update() method removes the items that exist in both sets.
##                                  The difference_update() method is different from the difference() method, because the difference() method returns a new set,
##                                  without the unwanted items, and the difference_update() method removes the unwanted items from the original set.

##syntax = set.difference_update(set) - parameter is set - required. the set to check for differences in

##A = {10, 20, 30, 40, 80}
##B = {100, 30, 80, 40, 60}
##A.difference_update(B)   # Modifies A and returns None
##print (A)

##6.discard - Removes an element from the set if it is a member. (Do nothing if the element is not in set)

#syntax = set.discard(value)    -parameter(value) Required. The item to search for, and remove

##fruits = {"apple", "banana", "cherry"}
##fruits.discard("banana")
##print(fruits)

##7.intersection - Intersection of two given sets A and B is a set which consists of all the elements which are common to both A and B.

##syntax = set1.intersection(set2, set3, set4….) In parameters, any number of sets can be given

##set1 = {2, 4, 5, 6} 
##set2 = {4, 6, 7, 8} 
##set3 = {4,6,8}
##print("set1 intersection set2 : ", set1.intersection(set2)) # union of two sets  
##print("set1 intersection set2 intersection set3 :", set1.intersection(set2,set3)) # union of three sets

##8.intersection_update - Updates the set with the intersection of itself and another

#syntax = A.intersection_update(*other_sets)  - The intersection_update() method allows an arbitrary number of arguments (sets).

#example1:
##A = {1, 2, 3, 4}
##B = {2, 3, 4, 5}
##result = A.intersection_update(B)
##print('result =', result)
##print('A =', A)
##print('B =', B)
###example2:
##A = {1, 2, 3, 4}
##B = {2, 3, 4, 5, 6}
##C = {4, 5, 6, 9, 10}
##result = C.intersection_update(B, A)
##print('result =', result)
##print('C =', C)
##print('B =', B)
##print('A =', A)

##9.isdisjoint - Returns True if two sets have a null intersection

#syntax = set.isdisjoint(other_set)             - parameter (other set) is required .The set to checked for being a disjoint set with set A.

##nums = {1, 2, 3, 4, 5 }
##oddNums = {1, 3, 5, 7, 9}
##primeNums = {7, 11, 13}
##print(nums.isdisjoint(oddNums))
##print(nums.isdisjoint(primeNums))

##10.issubset - Returns True if another set contains this set

##syntax = A.issubset(B)   -checks whether A is a subset of B or not.returns true if A is a subset of B otherwise false.

##A = {4, 1, 3, 5}
##B = {6, 0, 4, 1, 5, 0, 3, 5}
##print(A.issubset(B))
##print(B.issubset(A))

##11.issuperset - Returns True if this set contains another set

##syntax = set.issuperset(set)          -parameter set to search for equal items in

#example1:
##x = {"f", "e", "d", "c", "b"}
##y = {"a", "b", "c"}
##z = x.issuperset(y)
##print(z)

#example2:
##x = {"f", "e", "d", "c", "b", "a"}
##y = {"a", "b", "c"}
##z = x.issuperset(y)
##print(z)

##12.pop - Removes and returns an arbitrary set element. Raises KeyError if the set is empty

## syntax = S.pop()        -Pops a random element from S and returns it.

##S = {"ramya", "rahima", "ajay", "rajiv", "aksha"}
##print(S.pop())
##print(S.pop())
##print(S.pop())
##print("Updated set is", S)

##13.remove - Removes an element from the set. If the element is not a member, raises a KeyError

##syntax = set.remove(element)

##language = {'Kannada', 'Telugu', 'Tamil','German'}
##language.remove('German')
##print('Updated language set:', language)

##14.symmetric_difference - Returns the symmetric difference of two sets as a new set

##syntax = set.symmetric_difference(set)

##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##z = x.symmetric_difference(y)
##print(z)

##15.symmetric_difference_update - Updates a set with the symmetric difference of itself and another

##syntax = A.symmetric_difference_update(B)

##A = {'a', 'c', 'd'}
##B = {'c', 'd', 'e' }
##result = A.symmetric_difference_update(B)
##print('A =', A)
##print('B =', B)                                    # Here, the set A is updated with the symmetric difference of set A and B. However, the set B is unchanged.
##print('result =', result) 

##16.union - Returns the union of sets in a new set

##syntax = set.union(set1, set2...)

##x = {"a", "b", "c"}
##y = {"f", "d", "a"}
##z = {"c", "d", "e"}
##result = x.union(y, z)
##print(result)

##17.update - Updates the set with the union of itself and others

#syntax = set1.update(set2)  -Parameters :Update() method takes only a single argument. The single argument can be a set, list, tuples or a dictionary. It automatically converts into a set and adds to the set.

##list1 = [1, 2, 3] 
##list2 = [5, 6, 7] 
##list3 = [10, 11, 12]
##set1 = set(list2)     # Lists converted to sets 
##set2 = set(list1)
##set1.update(set2)  # Update method 
##print(set1)             # Print the updated set 
##set1.update(list3)  # List is passed as an parameter which gets automatically converted to a set 
##print(set1)

##Built-in Functions with Set

##1.all - Returns True if all elements of the set are true (or if the set is empty).
##Syntax = all( iterable )   - it is an iterable object such as a dictionary,tuple,list,set,etc.

##l = [4, 5, 1]           # All elements of list are true
##print(all(l))
##l = [0, 0, False]       # All elements of list are false
##print(all(l))
##l = [1, 0, 6, 7, False] # Some elements of list are true while others are false
##print(all(l))
##l = []                        # Empty List
##print(all(l))

##2.any - Returns True if any element of the set is true. If the set is empty, returns False.
##Syntax = any(iterable)

##l = [ 4, 5, 1]              # All elements of list are true
##print(any( l ))
##l = [ 0, 0, False]          # All elements of list are false
##print(any( l ))
##l = [ 1, 0, 6, 7, False]    # Some elements of list are true while others are false
##print(any( l ))
##l = []                              # Empty List
##print(any( l ))



##3.len - Returns the length (the number of items) in the set.
##Syntax = len(set)

##s = {"amazing", "code"}
##s1 = {"windows", "linux", "repeat"}
##x = len(s)
##x1 = len(s1)
##print(x)
##print(x1)


##4.max - Returns the largest item in the set or The max() function returns the item with the highest value.
##syntax= max(n1, n2, n3, ...) or  max(iterable)

#example1:
##a = (1, 5, 3, 9)
##x = max(a)
##print(x)
##example2:
##y = max("Mike", "John", "Vicky")
##print(y)

##5.min - Returns the smallest item in the set
##syntax=min(set)

##example1:
##a = (1, 5, 3, 9)
##x = min(a)
##print(x)
##example2:
##y = min("Mike", "Job", "Vicky")
##print(y)


##6.sorted - Returns a new sorted list from elements in the set(does not sort the set itself).
##Syntax: sorted(iterable, key, reverse)

##list_of_items = ['e', 'b', 'h', 'i', 'e']         # List
##print(sorted(list_of_items))

##tuple_of_items = ('z', 'r', 'p', 'v', 'x')      # Tuple
##print(sorted(tuple_of_items))
  
##string = "netzwerk"                             # String-sorted based on ASCII translations
##print(sorted(string))
  
##dictionary = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u':5}  # Dictionary
##print(sorted(dictionary))
  
##set_of_values = {'j', 'd', 'g', 'm', 'n'}       # Set
##print(sorted(set_of_values))
  
##frozen_set = frozenset(('t', 'j', 's', 'u', 'b'))   # Frozen Set
##print(sorted(frozen_set))

##7.sum - Returns the sum of all elements in the set.
##syntax=sum(iterable, start)

##a = (1, 2, 3, 4, 5)
##x = sum(a, 7)               #start with the number 7, and add all the items in a tuple to this number
##print(x)

print("\nThank you")

print("\t\t-learning is the never ending process \U0001f600")






















