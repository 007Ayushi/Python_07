#If u want to get all the directories of String in python 
# print(dir(str))

#If u want to get all the directories of Integer in python 
# print(dir(int))

#While loop- when the number of execution is not known and
#want to iterate till the condition satisfy.

# a=1

# while(a<=20):
#    print(a)
#    a=a+1


#While loop Question
#Ques1 Separate each digit of a number and print it on the new line
a=123
while(a>0):
   r=a%10
   print(f"{r}\n")
   a=a//10

#Ques 2:Accept a number and print its reverse

# num=int(input("Enter your number "))
# a=""

# while(num>0):
#    n=num%10
#    a=a+str(n)
#    num=num//10
# print(a)

#Ques3:Accept a number and check if it is a pallindromic number (If
#number and its reverse are equal

number=int(input("Enter a number "))
# original_number=number
# rev=0
# while(number>0):
#    r=number%10
#    rev=rev*10+r
#    number=number//10

# if original_number==rev:
#    print("palindrome")
# else:
#    print("Not palindrome")



number=str(number)
i=0
j=len(number)-1
is_palindrome = True
while i<=j:
   if number[i]==number[j]:
      i=i+1
      j=j-1
   else:
      is_palindrome = False
      break

if is_palindrome:
    print("Palindrome")
else:
    print("Not palindrome")


#Ques4 Create a random number guessing game with python.
import random
random_number=random.randint(1,100)
user_input=0
while(user_input!=random_number):
   user_input=int(input("Enter your guess "))
   if user_input<random_number:
      print("Too low")
   elif user_input>random_number:
      print("Too high")
   else:
      print("You guessed it right!")