"""Debugging in python
bug-->error
finding and fixing errors in the program is called debugging
types of errors:
1.syntax error -->missing colon,bracket,indentation
2.logical error -->missing of logics
3.runtime error -->division of any num with zero
debugging techniques:
1.print() statement debugging
2.try-except
3.use of pdb
    purpose:
       1.pause the execution
       2.inspect variables value
       3.to run the code step by step
    pdb commands:
         1.n-->next
         2.p variable_name-->print variable value 
         3.l-->list nearby code
         4.c-->continue the execution
         5.s-->start the function  
         6.r-->run till the function return  
         7.h-->help
         8.q-->quit the execution

# print() statement debugging
a = int(input("enter a num:"))
b = int(input("enter b num:"))
c = a+b
print("value a is:",a)
print("value b is:",b)
print("sum of a and b is:",c)
try:
    a = int(input("enter a num:"))
    print(10/a)
except ZeroDivisionError:
    print("cannot divide a num with zero")
except ValueError:
    print("invalid input,please enter integers only")"""
import pdb
def add(a,b):
    pdb.set_trace()#set a breakpoint pdb
    retutrn a+b
a = int(input("enter a num:"))
b = int(input("enter b num:"))
print(add(a,b))