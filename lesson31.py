"""1. Given three lists of integers: lst1, lst2, lst3, return the sum of integers which are 
common in all three lists.
Examples
sum_common([1, 2, 3], [5, 3, 2], [7, 3, 2]) ➞ 5
// 2 & 3 are common in all 3 lists.
# sum_common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]) ➞ 7
# // 2, 2 & 3 are common in all 3 lists.
# sum_common([1], [1], [2]) ➞ 0"""
list1=[1, 2,2, 3]
list2=[5, 3,2, 2]
list3=[7, 3,2, 2]
  # x=set(list1)&set(list2)&set(list3) &= intersection

x=set(list1).intersection(set(list2)).intersection(set(list3))
print (sum(x))

# """2.Write a function that takes a list of numbers and returns a list with two elements:
#    The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.
# Example
# [1, 2, 3, 4, 5, 6] ➞ [12, 9]
# # 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9
# [-1, -2, -3, -4, -5, -6] ➞ [-12, -9]
# [0, 0] ➞ [0, 0]
# Notes
# Count 0 as an even number."""          ?
# num=[1,2,3,4,5,6]
# sum1=sum(num)*num%2==0
# sum2=sum(num)*num%2!=0

# print(sum1)

"""3. Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects like { "name": "John", "top_note": 5 }.
Examples
top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }
top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }
top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }"""



def get_top_notes(data):
    result = {}
    for item in data:
        name = item["name"]
        top_note = max(item["notes"])
        result[name] = {"name": name, "top_note": top_note}
    return result
data = [
    {"name": "John", "notes": [3, 5, 4]},
    {"name": "Jane", "notes": [2, 4, 6]},
    {"name": "Bob", "notes": [5, 5, 5]},
]

result = get_top_notes(data)

print(result)

"""4. Write a function that takes a list of numbers and returns a list with two elements:
The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list.
Example
sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9
sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])
sum_odd_and_even([0, 0]) ➞ [0, 0])"""
def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return [even_sum, odd_sum]
numbers = [1, 2, 3, 4, 5, 6]
result = sum_even_odd(numbers)
print(result)


"""5. You work for a manufacturer, and have been asked to calculate the total
profit made on the sales of a product. You are given a dictionary containing 
the cost price per unit (in dollars), sell price per unit (in dollars), 
and the starting inventory. Return the total profit made, rounded to the nearest dollar.
Examples
profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}) ➞ 14796
profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
}) ➞ 32411
profit({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
}) ➞ 44030"""

profit={
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}
x=profit.get("inventory")
y=profit.get("cost_price")
z=profit.get("sell_price")
a=x*z- x*y
print(int(a))


"""6. A number is said to be Harshad if it's exactly divisible by the sum of its digits. 
Create a function that determines whether a number is a Harshad or not.
Examples
is_harshad(75) ➞ False
# 7 + 5 = 12
# 75 is not exactly divisible by 12
 
is_harshad(171) ➞ True
# 1 + 7 + 1 = 9
# 9 exactly divides 171
 
is_harshad(481) ➞ True
is_harshad(89) ➞ False
is_harshad(516) ➞ True
is_harshad(200) ➞ True"""
num=int(input("enter num >"))
# x= 481
y=(num//100+(num%100)//10 +num%10)
print((num%y==0)*"True" or (num%y!=0)*"False")

"""7.Given an input string, reverse the string word by word.
Examples
"the sky is blue" ➞ "blue is sky the"
"  hello world!  " ➞ "world! hello"
"a good   example" ➞ "example good a"
Notes
A word is defined as a sequence of non-space characters.
The input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
Try to solve this in linear time."""
# word=input(" enter word >")
# input_str = input("enter string - >")
str="the sky is blue"
str1= str.strip()
x=str1.split()
reversed_string = ' '.join(x[ ::-1])
print(reversed_string)
"""13.Given an input string, reverse the string word by word (reversed word also).
Examples
the sky is blue" ➞ "eulb si yks eht"""
str="the sky is blue"
str1= str.strip()
reversed_string =''.join(str1[ ::-1 ])
print(reversed_string)




"""9.Create a function to test if a string is a valid pin or not.
A valid pin has:
Exactly 4 or 6 characters.
Only numerical characters (0-9).
No whitespace.
Examples
valid("1234") ➞ True
valid("45135") ➞ False
valid("89abc1") ➞ False
valid("900876") ➞ True
valid(" 4983") ➞ False
Notes
Empty strings should return False when tested."""
# test=input("enter valid pin  >")

# print(len(test) == 4  or  len(test) == 6)* "True" +  "NoneType"*"False"

"""10.Return a new set of identical items from two sets
Given:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:
{40, 50, 30}"""

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# methot intersection =&
print(set(set1.intersection(set(set2))))

"""11. Write a Python program to return a new set with unique items from both sets by removing duplicates.
Given:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:
{70, 40, 10, 50, 20, 60, 30}"""
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))


"""12. Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.
Given:
set1 = {10, 20, 30}
set2 = {20, 40, 50}
Expected output:
set1 {10, 30}"""
set1 = {10, 20, 30}
set2 = {20, 40, 50}
print(set1-set2)

"""8. Create a function that builds a word from the scrambled letters contained in the first list. 
Use the second list to establish each position of the letters in the first list. 
Return a string from the unscrambled letters (that made-up the word)
Examples
word_builder(["g", "e", "o"], [1, 0, 2]) ➞ "ego"
word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]) ➞ "test"
word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2]) ➞ "edabit"""
word = (["g", "e", "o"], [1, 0, 2]) 
dict1=dict(word[0])
dict2=dict(word[1])
print(dict1,dict2)







