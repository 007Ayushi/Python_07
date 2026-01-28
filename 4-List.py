#Function 
# Functions in Python group reusable code into a block that can be executed
#by calling the function name.This helps avoid repetition and makes programs modular and readable.
def hello():
   print("Hello world")
hello()
#Arguments- The values which we provide to the function
#Parameters - The values which the functions accept

def sum(a,b):
   print(f"The sum of your numbers is {a+b}")

sum(2,3) #2,3 are arguments and a,b are parameters.

#Types of Argument- positional,default and keyword Argument

#1. positional Argument
def add(a,b):
   return a+b
print(add(10,20))

#2.Keyword Argument
def intro(name,age):
   print(f"I am {name} and my age is {age}")
intro(age=21,name="Ayushi")

#Default Argument
def greet(name="Ayushi"):
   print(f"Hello guys, I am {name}")
greet()
greet("Geet")


#CHECK IF THE STRING IS PALINDROME OR NOT.
def palindrome(str):
   rev=""
   for i in range(len(str)-1,-1,-1):
      rev+=str[i]
   if rev==str:
      return "palindrome"
   else:
      return "Not Palindrome"
print(palindrome("tata"))

#In-Built Data Structures in Python
#1.List
#2.Tuple
#3.Set
#4.Dictionary

#Custom Data Structures- Stack,Queue,Linked List,Trees,Graphs
#List- A list is a collection which is ordered and changeable. Allows duplicate members.
fruits=["apple","banana","mango","grapes"]   
print(fruits)
print(fruits[0]) #Accessing elements
fruits.append("orange") #Adding elements
print(fruits)
fruits.remove("banana") #Removing elements
print(fruits)
fruits[1]="kiwi" #Modifying elements
print(fruits)
print(len(fruits)) #Length of list

#Tuple- A tuple is a collection which is ordered and unchangeable. Allows duplicate members.
my_tuple=("apple","banana","mango","grapes")
print(my_tuple)
print(my_tuple[1]) #Accessing elements
# my_tuple[1]="kiwi" #Modifying elements(not allowed)
# print(my_tuple)

print(len(my_tuple)) #Length of tuple
#Set- A set is a collection which is unordered and unindexed. No duplicate members.
my_set={"apple","banana","mango","grapes"}
print(my_set)
my_set.add("orange") #Adding elements  
print(my_set)
my_set.remove("banana") #Removing elements
print(my_set)
print(len(my_set)) #Length of set

#Dictionary- A dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
my_dict={"name":"Ayushi","age":21,"city":"Delhi"}
print(my_dict)
print(my_dict["name"]) #Accessing elements
my_dict["age"]=22 #Modifying elements
print(my_dict)
my_dict["profession"]="Engineer" #Adding elements
print(my_dict)
del my_dict["city"] #Removing elements
print(my_dict)
   

#List - Mutable,Duplicates,Ordered,Heterogeneous
a=[12,99,"Ayushi Gupta",print()]
#Slicing can also be performed in the List
# print(a[0:])

#Ways to traverse in the list

#1st way using index
# for i in range(len(a)):
#    print(a[i])

#2nd way diectly on values
# for i in a:
#    print(i)

#Method=functions defined inside a class is called Methods.
# and Functions 


# A method is a function that is associated with an object or a class.
# It defines the behavior of that object.
# A function is a block of code that performs a specific task and is not associated with any object or class.
# Defined independently
# Can be called directly
# Does not belong to a class or object

l=[1,2,3]
l.append(4)
l.insert(0,10)
print(l)
l.extend([10,20,330])#Adds multiple elements at the end
print(l)
l.remove(3)#Removes the first occurrence of a number
i=l.index(2)#Finds the index of 2
print(i)
cnt_3=l.count(4)#Count occurrences of 3
print(cnt_3)
l.sort()#Sorts the list in ascending order
l.reverse()#Reverse the list order
new_num=l.copy()#Creates a copy of the list
print(new_num)
print(l.clear())#Removes all elements from the list 
popped_item=new_num.pop(4)#remove  the 4th index element
print(popped_item)
print(new_num)

#Some Questions on List
#1.Print positive and negative elements of an List.
my_list=[10,20,-10,-20]
print("Negative numbers of my_list are")
for i in my_list:
      if i<0:
         print(i)

print("Positive Numbers of my_list are")

for i in my_list:
   if i>=0:
      print(i)
      
sum=0
cnt=len(my_list)
#2.Mean of List elements
for i in my_list:
   sum+=i
print(sum/cnt)

mx=float('-inf')
idx=0
#3. Find the greatest element and print its index too.
for i in my_list:
   if i > mx:
      mx=i
      idx=my_list.index(i)
print(mx,idx)

smx=float('-inf')
mx=float('-inf')
for i in my_list:
   if i> mx:
      smx=mx
      mx=i

   elif smx!=mx and i>smx:
      smx=i
print("second greatest element is ",smx)

#Check is the list is sorted or not

my_list=[-10,1,10,2,3]
def isSorted(my_list):
  return my_list==sorted(my_list)
print(isSorted(my_list))