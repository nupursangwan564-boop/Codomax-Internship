#function
def fibo(a):
  if a==0:
    return 0
  elif a==1:
    return 1
  else:
    return fibo(a-1) + fibo(a-2)
a=int(input("enter a number"))
for i in range(a):
  print(fact(i),end=" ")

#loops
n=int(input("enter no of lines u want : "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    print("*"*i)
print()
    

#if else statement 
c=int(input("enter a number"))
d=int(input("enter a number"))
if c>d:
  print("c is greater tha d")
else:
  print("d ig greater")


#list 
lst=[1,4,5,10,2,3,74]
print(len(lst))
print(lst.append(12))
print(lst.sort())
print(min(lst))
print(max(lst))
print(.insert(2,11))


#list second largest number
l=[1,10,54,21,30,77,85,55,11]
ln=l.sort()
print("second largest element in the list is : ",ln[-2])



#
