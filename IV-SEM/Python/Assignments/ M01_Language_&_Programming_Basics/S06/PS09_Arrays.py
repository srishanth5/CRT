"""
Arrays
numpy:
numpy-->numerical python
uses in ml and data science

import numpy as np
arr = np.array([10,20,30,40,50])
print("array is:",arr)"""
import numpy as np
arr = np.array([10,20,30,40,50])
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.sum(arr))
print(np.zeros(5))
print(np.ones(5))
print("even numbers:",np.arange(2,10,2))
print("odd numbers:",np.arange(1,10,2))
n = int(input("enter size of array:"))
ele = list(map(int,input("enter elements:").split()))
print("array elements are:",np.array(ele))