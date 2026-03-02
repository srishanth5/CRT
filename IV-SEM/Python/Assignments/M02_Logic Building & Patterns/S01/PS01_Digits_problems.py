"""
sample input : 1234
sample output : 4
sample input : 455786
sample output : 6
sample input : 45
sample output : 2

num = int(input())
count = 0
while num>0:
    count+=1
    num//=10
print(count)
print(len(str(num)))
SUM OF DIGITS IN A NUMBER
n = int(input())
temp = n
sum = 0
while n>0:
    digit = n%10
    sum+=digit
    n//=10
print(sum)
print(sum(map(int,str(temp))))
#count of even and odd digits in a number
n = int(input())
count_even = 0
count_odd = 0
while n>0:
    digit = n%10
    if digit%2==0:
        count_even+=1
    else:
        count_odd+=1
    n//=10
print(count_even,count_odd)
#find the single digit from the given number by adding the digits repeatedly until a single digit is obtained
n = int(input())
while n>9:
    n = sum(map(int,str(n)))
print(n)"""
# reverse a number
n = int(input())
rev = 0
while n>0:
    digit = n%10
    rev = rev*10+digit
    n//=10
print(rev)






