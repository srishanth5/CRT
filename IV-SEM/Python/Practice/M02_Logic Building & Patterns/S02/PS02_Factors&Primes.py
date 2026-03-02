"""read a number and print all the factors of that number
input : 12
output : 1 2 3 4 6 12
n = int(input())
for i in range(1,n//2+1):
    if n%i==0:
        print(i,end=" ")
print(n)
# count the number of factors of a number
n = int(input())
count = 0
for i in range(1,n//2+1):
    if n%i==0:
        count+=1
print(count+1)
# check if a number is prime or not
n = int(input())
counter = 0
for i in range(2,n//2+1):
    if n%i==0:
        counter+=1
        break
if counter==0:
    print("prime")
else:    
    print("not prime")
# display all the prime numbers between given range
start = int(input())
end = int(input())
for n in range(start,end+1):
    counter  = 0
    for i in range(2,n//2+1):
        if n%i==0:
            counter+=1
    if counter==0 and n>1:
        print(n,end=" ")
#factorial of a number
n = int(input())
if n<0:
    print("factorial not defined")
elif n==0 or n==1:
    print(1)
else:
    fact = 1
    for i in range(1,n+1):
        fact*=i
    print(fact)"""
#gcd of two numbers
a = int(input())
b = int(input())
while b:
    a,b = b,a%b
print(a)
import math
print(math.gcd(a,b))
