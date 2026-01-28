#Set
s={1,2,3,4,5}
 #if s={} then it will become Dictionary

 #Set -Mutable,No Duplicates,Unordered,Heterogeneous
 #cannot access elements through index,No index values exists
#it can only store string,numbers,tuples but not everything

a={1,8,9,"hello",2,3,4,5}
#for i in a:
#   print(i) #order depends on systems hash value 

a.add(10);#Adds an element to the set
a.remove(10) #Removes 10 (Raises an error if not found)
a.discard(10) #Removes 10 (NO error if not found)
popped_ele=a.pop() #Removes a random element
print(popped_ele) # 1
a.clear() # Removes all elements
print(a)#set()

#Operations on set
a={1,2,3}
b={3,4,5}

union_set=a.union(b)
print("union set is",union_set)#{1, 2, 3, 4, 5}
print("Another way of union is",a|b)

intersection_set=a.intersection(b)
print("intersection ",intersection_set)#{3}
print("Another way of intersection is",a&(b))

difference_set=a.difference(b)
print("Differences",difference_set) #{1,2}
print("another way of difference is ",a-b)#elements of a only
print("diff of b-a",b-a)#{4,5}

symmetric_diff=a.symmetric_difference(b)#{1, 2, 4, 5}
print("Symmetric Difference are",symmetric_diff)#{1, 2, 4, 5} #It removes common elements.

b-=a
print(b) #{4,5}

#Dictionary Powers - Mutable,Duplicates,Order,Heterogeneous
d={1:"hello",2:56,"hello":"hii"}
print(d)

d={10:100,20:200,30:300,40:400}
print(d[10])
d[10]=1000 #updation
print(d[10])

d.update({50:500})
d[50]=550 #updating

d[60]=600 #creating
del d[60] #Deleting
print(d)

#We cannot update keys of Dictionary
d={10:100,20:200,30:300,40:400}

#Traversing in the Dictionary
# for i in d:
#    print(i)#Keys

# for i in d:
#    print(d[i]) #Values

for i in d.values():
   print(i) #values

d.clear() #Removes all key value pairs of the dic
print(d) 

a=[1,2,3,4,5]

#Deep copy - means changes has done in deep copy
b=a

b[0]=100
print(a)

#Shallow copy means separate copy of b has created.
b=a.copy()
b[0]=200
print(b)


d={10:100,20:200,30:300,40:400}
# help(dict)

d2=d.get(20)
print(d2)

print(d.items())#dict_items([(10, 100), (20, 200), (30, 300), (40, 400)])


#1.Write a Python script to merge two Python dictionaries?
a={1:100,2:200}
b={3:300,4:400}
# a.update(b)
# print(a)

def merge_dict(a,b):
   for key in b:
      if key not in a:
         a[key]=b[key]
   return a
print("merged dictionary is",merge_dict({1:100,2:200},{3:300,4:400}))


sum=0
#2.Write a Python program to sum all the values in a dictionary?
for i in a.values():
   sum=sum+i
print(sum)

#3.Count the frequency of each element
def frq(a):
   for i in a:
      f=1
      if i not in a:
         for j in a:
          if i==j:
            f=f+1
      print(i,":",f)
frq(a)

#4.Write a Python program to combine two dictionary by adding
#values for common keys.
a={1:100,2:200}
b={3:300,4:400}
def combine_twokey(a,b):
   res={}
   for key in a:
      if key in b:
         res[key]=a[key]+b[key]
      else :
       res[key]=a[key]

   for key in b:
      if key not in res:
          res[key]=b[key]
   return res

print(combine_twokey(a,b))
a={1:100,2:200}
b={3:300,4:400}
for i in b:
   if i in a.keys():
      a[i]+=b[i]
   else:
      a[i]=b[i]
print(a)


