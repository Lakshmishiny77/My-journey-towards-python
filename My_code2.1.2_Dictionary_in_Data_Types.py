##Mutable Data types in Python - 2.Dictionary 

##Let us start with 2.Dictionary

##Python Dictionary is an unordered sequence of data of key-value pair form.
##It is similar to the hash table type. Dictionaries are written within curly braces in the form key:value.
##It is very useful to retrieve data in an optimized way among a large amount of data.
##Keys in a dictionary doesn’t allows Polymorphism.

var  = {1:"first name",2:"last name", "age":33}
print(type(var))  #This print will give you the type of variable

##Creating a Dictionary

##In Python, a Dictionary can be created by placing sequence of elements within curly {} braces,separated by ‘comma’.
##Dictionary holds a pair of values, one being the Key and the other corresponding pair element being its
##Key:value. Values in a dictionary can be of any datatype and can be duplicated,
##                    whereas keys can’t be repeated and must be immutable.
##Dictionary keys are case sensitive, same name but different cases of Key will be treated distinctly.

### Creating a Dictionary with Integer Keys
##Dict = {1: 'netzwerk', 2: 'academy', 3: 'laxmi'}
##print("\nDictionary with the use of Integer Keys: ")
##print(Dict)

### Creating a Dictionary  with Mixed keys
##Dict = {'Name': 'Netzwerk', 1: [1, 2, 3, 4]}
##print("\nDictionary with the use of Mixed Keys: ")
##print(Dict)


### Creating an empty Dictionary
##Dict = {}
##print("Empty Dictionary: ")
##print(Dict)
  
### Creating a Dictionary with dict() method
##Dict = dict({1: 'Netzwerk', 2: 'academy', 3:'laxmi'})
##print("\nDictionary with the use of dict(): ")
##print(Dict)
  
### Creating a Dictionary with each item as a Pair
##Dict = dict([(1, 'netz'), (2, 'aca')])
##print("\nDictionary with each item as a pair: ")
##print(Dict)


# Creating a Nested Dictionary as shown in the below image
##Dict = {1: 'Python', 2: 'For', 
##        3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Netz'}}
##print(Dict)

#we have few built-in functions of list as follows

##1.clear - The clear() method removes all the elements from a dictionary.
##Syntax = dictionary.clear()

##my_dict = {
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##my_dict.clear()
##print(my_dict)

##2.copy - They copy() method returns a shallow copy of the dictionary.
##Syntax = dict.copy()      - The copy() method doesn't take any parameters.

##original = {1:'facebook', 2:'snapchat'}
##new = original.copy()
##print(new)

##3.fromkeys - The fromkeys() method returns a dictionary with the specified keys and the specified value.
##syntax=dict.fromkeys(seq[, value])   -seq − This is the list of values which would be used for dictionary keys preparation. value − This is optional, if provided then value would be set to this value bydefault it is none.

##x = ('key1', 'key2', 'key3')
##thisdict = dict.fromkeys(x)
##print(thisdict)
##
##dict = dict.fromkeys(x, 10)
##print ("New Dictionary :  %s"  %str(dict))

##4.get - The method get() returns a value for the given key. If key is not available then returns default value is None.
##syntax=dict.get(key, default=None)      -key − This is the Key to be searched in the dictionary.default − This is the Value to be returned in case key does not exist.

##dict = {'Name': 'sara', 'Age': 27}
##print ("Value : %s" %  dict.get('Age'))

##5.items -  items() method is used to return the list with all dictionary keys with values.
##syntax=dictionary.items()   - This method takes no parameters.

##Dictionary1 = { 'A': 'Datatypes', 'B': 4, 'C': 'Python' }  
##print("Dictionary items:")
##print(Dictionary1.items())

##6.keys - keys()method returns a view object that displays a list of all the keys in the dictionary in order of insertion.
##Syntax: dict.keys()   -There are no parameters.

##Dictionary1 = {'A': 'Dog', 'B': 'Doll', 'C': 'DoS'}
##print(Dictionary1.keys())
##empty_Dict1 = {}
##print(empty_Dict1.keys())

##7.pop - The pop() method removes the specified item from the dictionary.
##syntax=dictionary.pop(keyname, defaultvalue)     -          keyname -	Required. The keyname of the item you want to remove
##                                                                                     defaultvalue - Optional. A value to return if the specified key do not exist.If this parameter is not specified, and the no item with the specified key is found, an error is raised

##my_dict = {
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##my_dict.pop("model")
##print(my_dict)

##8.popitem - The popitem() method removes the item that was last inserted into the dictionary. 
##syntax = dictionary.popitem()                  -No parameters

##car = {
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##x = car.popitem()
##print(x)
##print(car)

##9.setdefault - In Python Dictionary, setdefault() method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
##syntax = dict.setdefault(key, default_value) - key – Key to be searched in the dictionary. 
##                                                     default_value (optional) – Key with a value default_value is inserted to the dictionary if key is not in the dictionary. If not provided, the default_value will be None.
#Example 1:
##Dictionary1 = { 'A': 'Greetings', 'B': 'For', 'C': 'festival'}
##Third_value = Dictionary1.setdefault('C')
##print("Dictionary:", Dictionary1)
##print("Third_value:", Third_value)

#Example 2:
##Dictionary1 = { 'A': 'Greetings', 'B': 'For'}
### using setdefault() method when key is not in the Dictionary
##Third_value = Dictionary1.setdefault('C')
##print("Dictionary:", Dictionary1)
##print("Third_value:", Third_value)
### using setdefault() method when key is not in the Dictionary but default value is provided
##Fourth_value = Dictionary1.setdefault('D', 'is')
##print("Dictionary:", Dictionary1)
##print("Fourth_value:", Fourth_value)

##10.update - The update() method updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.
##syntax = dict.update([other])  -The update() method takes either a dictionary or an iterable object of key/value pairs (generally tuples).

##example 1:
##d = {1: "one", 2: "three"}
##d1 = {2: "two"}
### updates the value of key 2
##d.update(d1)
##print(d)
##d1 = {3: "three"}
### adds element with key 3
##d.update(d1)
##print(d)

##example 2:
##d = {'x': 2}
##d.update(y = 3, z = 0)
##print(d)

##11.values - The values() method returns a view object that displays a list of all the values in the dictionary.
##syntax=dictionary.values()   -values() method doesn't take any parameters.

##example1:
##fruits = { 'apple': 2, 'orange': 3, 'grapes': 4 }
##print(fruits.values())

##example2:
##fruits = { 'apple': 2, 'orange': 3, 'grapes': 4 }
##values = fruits.values()
##print('Original items:', values)
### delete an item from dictionary
##del[fruits['apple']]
##print('Updated items:', values)

print("\nThank you")

print("\t\t-learning is the never ending process \U0001f600")



