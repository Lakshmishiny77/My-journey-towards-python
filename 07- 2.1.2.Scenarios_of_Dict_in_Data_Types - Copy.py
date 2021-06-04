##2.1.2 SCENARIOS OF DICTIONARY

#printing dictionary
my_dictionary = {"a": 1, "b": 2}
print(my_dictionary)

#1.If keys are duplicated in different format
##var = {1:"dhoni",True:"kohli",1.0:"ashwin",2:"rohith"}
##print(var)                     # here the output is ashwin since the key 1,True and 1.0 all three is equal to 1 hence it is printing the latest one

#2.Get dictionary by assaigning key:value into empty set 
##var = {}
##var['country'] = "India"
##print(var)

#3.These are the 3 diff scenario for running a for loop in dictionary
####i.items() function will give key and values
####ii. values() function will give only values from the dict
####iii. normal for loop will give only the keys

##i.
##var = {"name":"dhoni","age":33,"team":"csk"}
##for x in var.items():
##    print(x)
##ii.
##for y in var.values():
##    print(y)
##iii.
##for z in var:
##    print(z)

#4.accesing dictionary values through index and keys
##test = [{'arizona':'phoenix','california':'sacromento','hawaii':'honolulu'},1000,2000,3000,['hat','shirt','jeans',{'socks':'red','sock2':'blue'}]]
##print(test[0]['arizona'])
##print(test[4][3]['sock2'])

#5.squaring the numbers in values
##output = {}
##for x in range(4):
##    output[x] = x*x
##print(output)
##or
##output = {x:x*x for x in range(4)}
##print(output)

#6.updating value in dictionary
##var = {"name":["india","ashwin","csk"]}
##var["name"][2]="rcb"
##print(var)

#7.updating key and value in dictionary
##example1:
##var = {"name":"dhoni"}
##var1 = {"age":33}
##var.update(var1)
##print(var)

##example2:
##var = {"name":"dhoni"}
##var1 = {"age":33}
##output = {**var,**var1}
##print(output)

#example3:
##var = {"name":"dhoni"}
##var1 = {"age":33}
##var3 = {"team":"country"}
##output = {**var,**var1,**var3}
##print(output)

##8. converting strings to dictionary using json
##import json                                            #java script object notation
##var = '{"Name":"dhoni","Age":33,"team":["csk","rcb"]}'
##print(type(var))             #it is string here
##output = json.loads(var) #converting into dict
##print(type(output))         #it is dict now
##print(output)

#9. converting tuple into dictionary

##def convert(tup,di):
##    di = dict(tup)
##    return di
##tups = [("a",10),("b",12),("c",14),("d",20)]
##dictionary = {}
##print(convert(tups,dictionary))

##10.performing arithmetic operation using dict
#example1: subtraction
##dict = {}
##x,y,z = 10,20,30
##dict[x,y,z]= x-y-z;
###example2: addition
##x,y,z = 5,2,4
##dict[x,y,z] = x+y+z;
##print(dict)
###example3: multiplication
##x,y,z = 5,2,4
##dict[x,y,z] = x*y*z;
##print(dict)

#11.fromkeys - is to assaign same value to all keys
##i.none by default
##keys = {'a','e','i','o','u'}
##vowels = dict.fromkeys(keys)
##print(vowels)

##ii.with values
##keys = {'a','e','i','o','u'}
##value = 1
##vowels = dict.fromkeys(keys,value)
##print(vowels)

print("\nThank you")

print("\t\t-learning is the never ending process \U0001f600")



