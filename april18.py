""" xndir 1"""

# def solution(param1:int, param2:int):
#     if param1 >= -1000 and param1<=1000 and param2 >= -1000 and param2<=1000:
#         return param1+param2

 
# print(solution(1,2))

# """ xndir 2"""

# #  1-in lucum
# def solution(year):
#     x=year%100>0
#     if x>0:
#         return year//100 +1
#     else:
#         return year//100
    
# print(solution(1701))

# # 2-rd lucum
# def solution(year):
#     return (year + 99) // 100


"""Given the string, check if it is a palindrome.

Example

    For inputString = "aabaa", the output should be
    solution(inputString) = true;
    For inputString = "abac", the output should be
    solution(inputString) = false;
    For inputString = "a", the output should be
    solution(inputString) = true."""
 
 
#  -in lucum
# def solution(inputString):
#     rev = '' .join(reversed(inputString))
#     if rev == inputString:
#         return True
#     elif rev!=inputString:
#         return False
#   print(solution("abacaba"))
# 
#   2-rd lucum  
#     
# def solution(inputString):
#   if inputString==inputString[::-1]:
#     return True
#   else:
#       return False
# print(solution("aacb"))

#  optimal lucum
# solution = lambda s: s[::-1] == s


"""4.Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

# 7 and 3 produce the largest product."""
# def solution(inputArray):
#     max_product = float()
#     for i in range(len(inputArray) - 1):
#         product = inputArray[i] * inputArray[i+1]
#         if product > max_product:
#             max_product = product
#     return max_product

# print(solution ([3, 6, -2, -5, 7, 3]))
"""5.Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the 
n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 
4-interesting polygons in the picture below."""

# def solution(n):
#     if n==1:
#         return n
#     elif n+1:
#         return 1+2*n*(n-1)
            
# print(solution(1))

# 2-rd lucum
# def solution(n):
#     return n**2 + (n-1)**2
#  print(solution(4))


"""6.  Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, 
  each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange 
  them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may 
  need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
solution(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7."""

# def solution(statues):
#   return max(statues)- min(statues)+ 1 - len(statues)
# # statues=[0, 3]
# print(solution([0, 3]))
  
# return max(statues) - min(statues) - len(statues) + 1def solution(sequence):d
# def solution(sequence):
#   error = 0
#   second_error = 0
#   for index, i in enumerate(sequence[:-1]):
#     if sequence[index+1]<=i:
#       error+=1
#       if index<len(seguence)-2 and seguence[index+2]<=i:
#         second_error+=1
#         if error ==1 and second_error<=1:
#           return True
#         return False
  
#  print (solution([1, 3, 2, 1]))
# def solution(matrix):
#    total =0
#    j_columns=set()
#    for index, i in enumerate(matrix):
#      for jindex , j in enumerate(i):
#        if j==0:
#          j_columns.add(jindex)
#          continue
#        if index >0 and jindex in j_columns:
#          continue
#        total+=j
#     return total 
  
  
#   matrix = [[0, 1, 1, 2], 
#           [0, 5, 0, 0], 
#           [2, 0, 3, 3]]
# print(solution)
# """ 1. Using .sort() method, create a lambda function that sorts the list in descending order. Refrain from using the reverse parameter.
# (Hint: lambda will be passed to sort method's key parameter as argument)
# Please check out Hint 0 below to be informed about a glitch regarding this exercise.
# lst=[100, 10, 10000, 1, 9, 999, 99]"""

# lst =[100, 10, 10000, 1, 9, 999, 99]
# lst.sort(key=lambda x:-x)
# print(lst)

# def lst(rev_list):
#   for i in rev_list:
#   return lambda sorted.(rev_list)
# print(lst[100, 10, 10000, 1, 9, 999, 99])

# lst=[100, 10, 10000, 1, 9, 999, 99]
# return lambda lst:sorted(lst)
# print(lst)


#  hashvum e tvi erapatik
# from april7 import is_vowel


def my_func(n):
  return lambda a:a*n
mydoubler =my_func(3)

# print(mydoubler(11))

# c2.ars =["Ford", "Toyota", "Mersedes"]
# cars.append("BMV")
# print(cars)
# print("Type incars -> ", type(cars), len(cars))
# print(cars[0], cars[1], cars[2])

# 3.cars=["Ford", "Toyota", "Mersedes"]
# # cars.remove("Ford")
# # print(cars)
# cars.pop(0)
# print(cars)

# 4.numbers=[6, 9, 3, 1]
# numbers_tuple=(8,10,-9,3)
# num1=sorted(numbers_tuple)
# num=sorted(numbers)
# print(num,num1)
 
#  string_number_value =["34521"]  ?
# #  
# sorted_string_number=sorted(string_number_value)
# #  string _value='I like to ort'
# #  sorted_string =sorted(string _value)
# print(sorted_string_number)
# #  print(sorted_string )

# word ="paper"
# print(len(word))
# words=["bannana","pie","Washington","book"]
# # print(sorted(words, key=len))
# print(sorted(words,key=str.lower))

       
# """2. Using sorted() function, reverse parameter and lambda sort the tuples in the list based on the last character of the 
# second items in reverse order.
# lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
# #Type your answer here.
# Decorators, function inside function"""


# lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
# lst.sort( key=lambda x: x[1][-1], reverse=True)
# print(lst)

# lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
# sorted_lst = sorted(lst, key=lambda x: x[::-1], reverse=True)
# print(sorted_lst)
"""3.Write function which take a function as an input and run it and print how count how many times 
is_vowel have run the input provide functions."""

# def my_func(n):
#   return lambda a:a*n
# mydoubler =my_func(3)
# print(mydoubler)
"""3. Write function which take a function as an input and run it and print how count how many times I have run the
input provide functions."""


def some_func():
  count=0
  def inner(*args,**kwargs):
    nonlocal count
    count+=1
    print(count)
    return func()
  return inner  

def func():
  print("I am global func")

x = some_func()
x(func)
x(func)



# def count_runs():
#     count = 0
    
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(count)
#     return func()
    
#     return wrapper

# # Example usage
#  def my_function():
#    print("Hello world!")

# my_function = count_runs(my_function)

# my_function() # prints "Hello world!"
# print("Function has been run", my_function.count, "times") # prints "Function has been run 1 times"
# my_function() # prints "Hello world!"
# print("Function has been run", my_function.count, "times") # prints "Function has been run 2 times"
