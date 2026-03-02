"""fibonacci series
n = int(input())
a,b = 0,1
for i in range(n):
    print(a,end=" ")
    a,b = b,a+b
fib = [0,1]
for i in range(2,n):
    fib.append(fib[i-1]+fib[i-2])
print(fib)"""
#power of number series