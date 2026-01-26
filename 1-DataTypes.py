print("ayshi")

#comments in Python
# This is a single line comment
""" This is a Docstring comment
    which can span multiple lines  
     Helpful when u want to save paragraph"""

#Cases
#pascal case
MyName="Ayushi"

#camel case
myName="Ayushi"

#snake case
my_name="Ayushi"

#1.Datatypes - Numbers-Integer,Float,Complex
a=12
print(type(a))

b=3.2 #float

c=22/7 #Float
print(type(c))

d=24j #complex

#2.Strings
st='ayushi'

#3.Boolean
b=True


ch='A'
print(ord(ch)) #unicode - 65

num=65
print(chr(num)) #character - A

st="AYUSHI GUPTA"
#Accessing elements of the string
print(st[1],st[-5])

#slicing in string - str[start:stop:step]
print(st[0:7:1])


#TYPE CONVERSION
#converting number into string
a=12
a=str(a)
print(type(a)) #string class

a="12"
a=int(a)
print(type(a)) #int class

a=10
print(bool(a)) #True


"""
Falsy values - 0,0.0,"",[],(),{}
Truthy values - Any non-zero number → 1, -3, 2.5
Any non-empty string → "hi", "0",
Any non-empty collection → [1], (2,), {a:1}
True
👉 Rule: Non-empty / non-zero = True
"""

#Formatted String
# name="ayushi Gupta"
# age=22

# print(f"my name is {name} and my age is {age}")

""""
a=input("my age is ") #By default the data type is String
a=int(input("my age is "))
 """
#Operators - +,-,*,/,%,//,**

a=10
b=2
print(a/b,a//b,a**b)

"""
/ - Float Division  gives result in float
// - floor Division gives result in integer
"""
print(32%5)#Gives remainder

#Assignment Operator -used to assign values to the variables.
# a=10

#Compound Assignment operations
a*=10
a/=12
a-=10
a+=10

#Comparison Operators - 6 Types
# ==,!=,>,<,>=,<=

#Logical Operators - and,or,not
print(12>8 and 34>10 or 12<1 and 12!=19)#True

print(not 12==12)#False

#Conditional Statements
#if
a=13
if a>10:
   print("a is greater")

#if-else
if a>5:
   print("a is yes")
else:
   print("a is not taken")

#if elif else - only one condition will execute
#money=int(input("pls give me the money "))
# if money==10:
#    print("I will have a coco")
# elif money==20:
#    print("I will have a mango")
# else:
#    print("I will have a chocobar")


#Questions on Conditional
#Q1.Accept two numbers and print the greatest between them.
# a=int(input("Enter the first number "))
# b=int(input("Enter second number "))

# if a>b:
#    print("a is greatest")
# else:
#    print("b is greatest")

#Q2.
# gender=input("Enter the gender")
# if gender =='f' or gender =='F':
#    print("Good morning ma'am")
# else:
#    print("Good morning Sir")

#Q3.
# num=int(input('Enter a number '))
# if num %2==0:
#    print("even")
# else:
#    print("odd")

#Q4.
# name=input("Enter the name ")
# age=int(input("Enter your age "))

# if age>=18:
#    print("hello,you are a valid voter")


#Q5.Accept a year and check if it is leap year
# year=int(input('Enter a year'))
# if (year % 4 ==0 and year %100 !=0 ) or (year %400==0):
#    print(f'{year} is leap year')

#if-elif ladder
temp=int(input("Enter the temperature "))
if temp<0 :
   print("Freezing cold")
elif temp>0 and temp<=10:
   print("Very Cold")
elif temp>=10 and temp<=20:
   print("cold")
elif temp>=20 and temp<=30:
   print("hot")
else:
   print("very pleasant")