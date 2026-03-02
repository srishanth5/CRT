'''import array
arr = array.array('i',[])
print(arr,type(arr))
arr.append(10)
arr.append(20)
print(arr)'''
"""li = [12,25.4,6+5j,"hello",12,25.4]
print(li)
print(type(li))
print(li[2])
print(li[3:6:1])
print(li[::-1])
print(len(li))
li.append("100")
print(li)
li.insert(2,"world")
print(li)
li.insert(-20,"python")
print(li)"""
x = 1234
count = 0
while x>0:
    digit = x%10
    count+=1
    x = x//10
print(count)
