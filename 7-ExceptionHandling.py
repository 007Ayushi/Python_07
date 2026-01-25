"""
Errors-Errors occur due to mistakes in the code
that prevent it from running .These can be syntax errors or logical errors.
"""

#1.Indentation Error
# a=12
# if a==12:
# print(a)

#2.Syntax Errors
#print("Hello world"

#Exceptions 
# a=int(input("Tell me your number-"))
# print(10/a) # if a=0 ZeroDivisionError: division by zero

# print("OK i have done the division")

#Syntax for Exception Handling
"""
try-wrap the block of code that might cause an exception.
except- Handles the exception if it occurs.
else-run code only if no exception occurs.
finally-Run code no matter what,whether there is an exception or not.
raise-Manually throw an exception.
"""
# a=int(input("Enter a number "))
# try:
#    print(10/a)
# except Exception as err:
#    print( f"Sorry there is an err as {err}")
# else :
#    print("Good There is no exception")
# finally:
#    print("I will run no matter what")
# print("Ok i have done my task")




#Another Exception
# a=input("Tell me your number - ")
# try:
#    print(10/a)
# except Exception as err:
#    print(f"sorry there is error occurred {err}")
# print("ok i have done my divison")

age=int(input("Tell me your age - "))

try:
   if age<10 or age>18:
      raise ValueError("Your age must be between 10 and 18")
   else:
      print("Welcome to the club")
except Exception as err:
   print(f"an error occurred as {err}")
print("The club will start soon")

