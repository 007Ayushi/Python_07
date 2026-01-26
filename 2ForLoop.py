#Loops - loops in py allows us to execute a block of code multipe times without rewriting it.
# have only 2 Loops - while loop and for loop

#for Loop works on numbers and while Loop works on some conditions.

#For Looop - range function , it accepts three things- start,stop and step
#Default values of start is 0 and step  is  1.
a=range(1,20,1)

# for i in a :
#    print(i)
 
# i is a variable which we are using for iteration.

# Print numbers from 20 to 50
# for i in range(20,51,1):
#    print(i)


# -3 to -15
# for i in range(-3,-16,-1):
#    print(i)


# 16 to 1
# for i in range(16,0,-1):
#    print(i) 

#For loop
#lets prints a table of 5

# num=int(input("Enter the number"))
# for i in range(1,11,1):
#       print(f"{num}*{i}={num*i}")

#lets print a table of 7 
# for i in range(7,71,7):
#       print(i)


# n=int(input("Enter the number"))
# for i in range(n,(n*10)+1,n):
#    print(i)


a="I will get job for sure"

#1st way to write  
# for i in range(len(a)):
#    print(a[i])

# 2nd way to write
# for char in a:
#    print(char)

#break - terminates the Execution
# for i in range(1,21):
#    if i==15:
#       break
#    print(i)

#continue - use to skip
# for i in range(1,10):
#    if i==20:
#       print("continue statement is executed")
#       continue
#    print(i) 
# else:
#    print("continue  statement is not excuted")

#For Loop Questions

#1.Accept an integer and print the hello world n times
# n=int(input("Enter the number n "))

# for i in range(n):
#    print("Hello World")

#Ques2. Print the natural number up to n.
# for i in range(1,n+1,1):
#    print(i)

#Ques3. Reverse for loop .print n to 1
# for i in range(n,0,-1):
#    print(i)


#Ques4 Take a number as input and print its table.
# for i in range(n,(n*10)+1,n):
#    print(i)

sum=0
#Ques5 sum up to n terms
# for i in range(n+1):
#    sum+=i
# print(sum)

#Ques6 Factorial of a number
# fact=1
# for i in range(n,0,-1):
#    fact*=i
# print(fact)

even=0
odd=0
#Ques7 print the sum of all even and odd numbers in a range separately.
# for i in range(n+1):
#    if i % 2==0:
#       even+=i
#    else:
#       odd+=i

# print(odd)
# print(even)

#Ques8 Print all the factors of a number.
# for i in range(1,n+1):
#    if n % i == 0:
#       print(i)

sum=0
#Ques9 Accept a  number and check if it a perfect number or not.
# for i in range(1,n):
#    if n % i==0:
#       sum+=i

# if sum==n:
#    print(f"{n} is a perfect Number")
# else:
#    print(f"{n} is not a perfect number")

cnt=0
#Ques10 check whether the number is prime or not.
# if n<=1:
#    print("It is not prime")
# else:
#    for i in range(1,n+1):
#       if n % i == 0:
#          cnt=cnt+1
# if cnt > 2:
#    print(f"{n} is not a prime number")
# else:
#    print(f"{n} is a prime number")

st="Ayushi"
ans=""
for char in range(len(st)-1,-1,-1):
   ans+=st[char]

print(ans)

#Ques11 Check string is Pallindrome or not

if str==ans:
   print("It is a palindrome")
else:
   print("It is not a palindrome")

#Ques 12 Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"
chars=0
Digits=0
Symbols=0
for ch in str1:
   ascii=ord(ch)
   if (ascii>=65 and ascii <=90) or (ascii>=97 and ascii<=122):
      chars=chars+1
   elif ascii>=48 and ascii<=57:
      Digits=Digits+1
   else :
      Symbols=Symbols+1

print(chars)
print(Digits)
print(Symbols)


#2nd way to do the same question
str1 = "P@#yn26at^&i5ve"
chars=0
Digits=0
Symbols=0

for i in str1:
   if i.isdigit():
      Digits+=1
   elif i.isalpha():
      chars+=1
   else:
      Symbols+=1
print(f"digits are {Digits}\n Alphabets are {chars} \n Symbols are {Symbols}") 