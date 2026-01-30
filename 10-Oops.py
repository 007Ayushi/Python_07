# OOPS (Object Oriented Programming System) is a programming 
# paradigm based on the concept of objects
# which can contains data (attributes) and code (methods).


#Classes -
#A class is like a blueprint or template for creating Objects.

# There are 2 types of things inside class Attributes and Methods.

# 1. Attributes - Variables defined inside the class are Attributes.
# 2. Methods - Functions defined inside a class are Methods.


class Animal:
   species="Dog" #Attribute

   def make_sound(self): #Method
      print("Bark !")

# class Factory:
#    a=12 #attribute

#    def hello(self): #method
#       print("how are you")

#    print("Hello how are you, I am getting initialized")

# print(Factory().a)

# Factory().hello()

# Output is -
# Hello how are you, I am getting initialized
# 12
# how are you

# class Fruits:
#    a=12 #attribute

#    def hii(self): #methods
#       print("How are you")

# obj=Fruits()
# print(obj.a)
# obj.hii()

#Output is - 
# 12
# How are you

# Constructor 

# A constructor is a method that runs automatically when we call a class
# and this constructor function will target the objects location.

# To target the object location we use self keyword.


# class Student:
#    def __init__(self,name):
#       self.name=name #Instance attribute

# # Creating an object with a value
# s=Student("Ayushi")

# #Accessing the attribute
# print(s.name)
      
#self defines the location 

class Fac:
   def __init__(self,material,zips,pockets):
      self.material=material
      self.zips=zips
      self.pockets=pockets

   def show(self):
      print(f"Your object details are {self.material},{self.pockets} ,{self.zips}")

reebok=Fac("leather",3,2)
campus=Fac("Nylon",3,3)

reebok.show()