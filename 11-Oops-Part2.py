#Attributes and Methods
#Types of Attributes

#1. Class Attribute - A normal variable created inside a class is a class attribute and thats it.
#2. Instance Attribute- A attribute created using an instance like self.name,self.age etc.It is known as instance attribute.


class Animal:
   name="lion" #class Attribute

   def __init__(self,age):
      self.age=age #Instance attribute

   def show(self): #instance method
      print(f"How are you , your age is {self.age}")

   @classmethod
   def hello(cls):
      print("How are you brother,it uses @classmethod decorator")#cls invokes to the class Animal

   @staticmethod
   def static():
      print("How are you,it uses @staticmethod decorater")

obj=Animal(22)
# Accessing Instance method
obj.show()   
obj.hello()
obj.static()


#Types of Methods

#1. Instance Method- An instance method works with instance (object)
# of the class.This method can access and modify instance attributes.


