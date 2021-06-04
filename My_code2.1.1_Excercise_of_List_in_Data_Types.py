##2.1.1
##1.List   - In Python programming, a list is created by placing all the items (elements) inside square brackets [],
                         #separated by commas.                               

#printing list
my_list = [1,2,3,4,5]
print(my_list)



##1. adding the list elements

##a = [2,4,56,7]
##
##print(a[0] + a[1] + a[2] +a[3])
##print(sum(a))

##2. copy list and modifying the elements through index

##a = ["dhoni","kohli","aswin"]
##b = a[:]      #here im copying the elements of a to b
##print(a)
##print(b)
##b[2] = "zahir"   #here replacing the 2nd index aswin to zahir
##print(b)

##3. inserting an element. 

##i) .insert
##a = ["aswin","kohli","dhoni"]
##a.insert(1,"Rahul")
##print(a)

##ii) .append
##a = ["aswin","kohli","dhoni"]
####a.append("padikkal")
##a.append(["padikkal","ahmad"])
##print(a)

##iii) .extend
##a = ["aswin","kohli","dhoni"]
##a.extend(["padikkal","ahmad"])
##print(a)

##4. sorting of list

##a = ["dhoni","aswin","dhawan","rahul"]
##b = sorted(a)
##print(b)

##5. deleting elements from the list

##a = ["dhoni","kohli","dhawan","chocolate"]
####a.pop(2)                                                       #i)pop
##
####a.remove("kohli")                                            #ii)remove
####a.clear()                                                           #iii)clear 
##del a[0]                                                               #iv)delete
##print(a)

##a=[1,2,3,4,5]                                                       ##deleting multiple elements from a list
##del a[1::2]
##print(a)

##6.reversing the perticular item through index

##var = ['dhoni','kholi','aswin']
##var = var[0][::-1]
##print(var)           

##7. printing even no. and odd no.
##output = []
##for x in range(9):
##    if x%2 == 0:
##        output.append(x)
##print(output)

###or
##output = [x for x in range(9) if x%2 == 0] #list compresions
##print(output)

##8.to check the existence of a number in a list

##num =7
##if num in [1,2,3,4,5]:
##    print('hello world')
##else:
##    print('not present')

##9. both the lists are equivalent but not identical as they have different objects

##list1=[0,1,2]
##list2=[0,1,2]
##print(list1 is list2)

##10.  cumulative sum of elements in a list

##a=[1,2,3,4]
##b=[sum(a[0:x+1])for x in range(0,len(a))]
##print(b)

##11.Nested list

##list = [1,2,['a','b',['cat','dog'],'c'],3]
##print(list[2][2][0][2])

##12.joning 2 lists

##my_list1 = ['hi','python']
##my_list2 = [77,777]
##final_list = my_list1 + my_list2
##print(final_list)

print("\nThank you")

print("\t\t-learning is the never ending process \U0001f600")



