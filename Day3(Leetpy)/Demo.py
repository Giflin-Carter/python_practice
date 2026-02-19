'''n=int(input("Enter a number"))
a=0
b=1
for i in range(n):
    print(a)
    a,b=b,a+b'''


'''n=int(input("Enter a number"))
a=0
b=1
c=1 
for i in range(n):
    print(a)
    a,b,c=b,c,a+b+c




a=[1,2,3,4,5,6,7]
b=[89,10,11,12,13,14]
#con
print(a+b)
#slice
print(a[:4])
print(b[:5])
#rep
print(a * 4)
#memb
print(17 in a)
print(15 not in b)
#comp
print(b>a)
#append
a.append(25)
print(a)
#insert
a.insert(4,45)
print(a)
#extend
a.extend(b)
print(a)
#remove
a.remove(3)
print(a)
#pop
a.pop(0)
print(a)
#clear
a.clear()
print(a)
#index
print(b.index(10))
print(b[3])
#count
print(b.count(14))
#sort
b.sort
print(b)
#sort rev
b.sort(reverse=True)
print(b)
b.reverse()
print(b)
#cpy
a=b.copy()
print(a)


def multiple():
    
    n=int(input("Enter a n value :"))
    count=2
    for i in range(n):
        x=count*i
        print(x)

multiple()

#map
def func(x):
    return x * 2

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(map(func, num))
print(result)

numone = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultone = list(filter(lambda x: x % 2 == 0, numone))
print(resultone)

#reduce
from functools import reduce

num = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, num)
print(result)
def func(x):
    return x * 2

count=0

num = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
result = list(map(func, num))
print(result)

numone = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
resultone = list(filter(lambda x: x % 2 == 0, numone))
count= count + len(resultone )
print(resultone)




#even count
count = 0
numone = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultone = list(filter(lambda x: x % 2 == 0, numone))
count = count + len(resultone)
print("Even numbers:", resultone)
print("Count of even numbers:", count)

#palindrome_slicing
word=input("Enter a word :")
if word==word[::-1]:
    print("palindrom")
else:
    print("not palindrome")'''



#palindrome
word=(input("Enter a num :"))
rev=""
for ch in word:
    rev=ch+rev
if word==rev:
    print("palindrom")
else:
    print("not palindrome")
  


  
'''#palindrome
word=int(input("Enter a num :"))
rev=0
for ch in word:
    rev=ch+rev
if word==rev:
    print("palindrom")
else:
    print("not palindrome")'''
  





