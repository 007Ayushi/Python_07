#Tuple - Immutable,Duplicates,Ordered,Heterogeneous

a=(1,2,3,4,5)
print(type(a))

a=(1,"ayushi",9.9,False,"ayushi")
print(a)

# for i in a:
#    print(i)

for i in range(len(a)):
   print(a[i])


#index and count Methods only 2 method in Tuple

index=a.index("ayushi")
print(index)

count_ayushi=a.count("ayushi")
print(count_ayushi)

#TUPLE UNPACKING
a,b,c,d=(1,2,3,4)
print("a",a)
print("b",b)

a=(1)
print(type(a))#<class 'int'>

a=(1,)
print(type(a))#<class 'tuple'>





