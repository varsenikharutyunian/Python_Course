# def  reverse(s):
#     return s[::-1]
# x= ["ab","cd","fm"]
# y=[]
# for i in x:
#     y.append(reverse(i))
# print(y)
# """ sa grend map ov"""
# def  reverse(s):
#     return s[::-1]

# x= ["ab","cd","fm"]
# y=list(map(reverse,x))
# print(y)

"""1.Write a map function that adds plus 5 to each item in the list."""
def sguare(x):
    return x*5
print(list(map(lambda x:x*5,range(1,11))))

"""2.Write a map function that adds "Hello, " in front of each item in the list"""
def add_hello(items):
    return list(map(lambda x:"Hello,"+ x,items))
lst=["Ann","Mari","Varsik","Alvard"]
result = add_hello(lst)
print(result)

# print(list(map(lambda x:"Hello,"+ x,["Ann","Mari","Varsik","Alvard"])))

"""3.Using filter() function filter the list so that only negative numbers are left."""
def negativ_number(items):
    
    
    return list(filter(lambda x:x<0,items))
lst=[5,9,-50,6,-10,0,-3]
result=negativ_number(lst)
print(result)

"""4.Using filter function, filter the even numbers so that only odd numbers are passed to the new list"""

def even_number(items):
    return list(filter(lambda x:x%2!=0,items))
lst=[5,9,-50,6,-10,0,-3]
result=even_number(lst)
print(result)

"""5.Using map() and filter() functions add 2000 to the values below 8000."""
def new_func(a):
    return list(map(lambda x:x+2000,filter(lambda x:x<8000,a)))
lst=[ 1,20,5000,400000,9000]
result=new_func(lst)
print(result)
# c = map(lambda x:x+x,filter(lambda x: (x>=3), (1,2,3,4)))
# print(list(c))



"""6.  Return product of integer lists
Collapse"""

def my_collapse(a:int,b:int):
    return a+b
from functools import reduce
result= reduce(my_collapse,range(1,11))
print(result)
