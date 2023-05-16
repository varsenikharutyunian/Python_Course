# ARRAYS

"""Imaginary Coding Interview
1.Create a function to check if a candidate is qualified in an imaginary coding interview of an imaginary tech startup.

The criteria for a candidate to be qualified in the coding interview is:

    The candidate should have complete all the questions.
    The maximum time given to complete the interview is 120 minutes.
    The maximum time given for very easy questions is 5 minutes each.
    The maximum time given for easy questions is 10 minutes each.
    The maximum time given for medium questions is 15 minutes each.
    The maximum time given for hard questions is 20 minutes each.

If all the above conditions are satisfied, return "qualified", else return "disqualified".

You will be given a list of time taken by a candidate to solve a particular question and the total time taken by the candidate to complete the interview.

Given a list , in a true condition will always be in the format [very easy, very easy, easy, easy, medium, medium, hard, hard].

The maximum time to complete the interview includes a buffer time of 20 minutes.
Examples

interview([5, 5, 10, 10, 15, 15, 20, 20], 120) ➞ "qualified"

interview([2, 3, 8, 6, 5, 12, 10, 18], 64) ➞  "qualified"

interview([5, 5, 10, 10, 25, 15, 20, 20], 120) ➞ "disqualified"
# Exceeded the time limit for a medium question.

interview([5, 5, 10, 10, 15, 15, 20], 120) ➞ "disqualified"
# Did not complete all the questions.

interview([5, 5, 10, 10, 15, 15, 20, 20], 130) ➞ "disqualified"
# Solved all the questions in their respected time limits but exceeded the total time limit of the interview.

Notes

Try to solve the problem using only list methods."""

def interview(lst, tot):
    for i in lst:
        if sum(lst)<= tot and 0<i<=20:
            i+=1
            return  "qualified"
        elif  sum(lst)> tot and i>20:
            return  "disqualified"
        
            
        
print(interview([5, 5, 10, 10, 15, 15, 20, 20,], 120))
print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))
print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120))

"""2.Natural Emptiness

n abstract set theory, a construction due to von Neumann represents the natural numbers by sets, as follows:

    0 = [ ] is the empty set
    1 = 0 ∪ [ 0 ] = [ 0 ] = [ [ ] ]
    2 = 1 ∪ [ 1 ] = [ 0, 1 ] = [ [ ], [ [ ] ] ]
    n = n−1 ∪ [ n−1 ] = ...

Write a function that receives an integer n and produces the representing set.
Examples

rep_set(0) ➞ []

rep_set(1) ➞ [[]]

rep_set(2) ➞ [[], [[]]]

rep_set(3) ➞ [[], [[]], [[], [[ ]]]]"""


# def rep_set(n):
#     n=int(n)
#     while i in n:
#         return []
# # while i<=n :
# #     b=[a]
# #     i+=1
# #     return b+[a]
    
# print(rep_set(0))
"""3.Basic Arithmetic Operations on a String Number
Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.

eval() is not allowed. In case of division, whenever the second number equals "0" return -1.

For example:

"15 // 0"  ➞ -1

Examples

arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24

arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0

arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144

arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1

Notes

    All the inputs are only integers.
    The operators are * - + and //.
    Hint: Think about the single space that appears before and after the arithmetic operator."""
def arithmetic_operation(n):
    num=n.split()
    num1=int(num[0])
    operator=num[1]
    num2=int(num[2])
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    else:
        return num1//num2
        
        
print(arithmetic_operation("12 - 12") )  


"""4.Encode Morse
Create a function that takes a string as an argument and returns the Morse code equivalent.
Examples

encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."

encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"

This dictionary can be used for coding:

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

Notes

    Ouput should be International Morse Code, and use the standard conventions for symbols not defined inside the ITU recommendation (see Resources).
    Input value can be lower or upper case.
    Input string can have digits.
    Input string can have some special characters (e.g. comma, colon, apostrophe, period, question mark, exclamation mark).
    One space " " is expected after each character, except the last one."""
                
# def encode_morse(message):
#     for i in message:
#         char_to_dots = {

#         if i in char_to_dots.keys():
#             x=message.replace("i",char_to_dots.values())
#             return x
# print(encode_morse("EDABBIT CHALLENGE"))

"""6.Combined Consecutive SequenceWrite a function that returns True if two arrays, when combined, form a consecutive sequence. 
A consecutiveeq suence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, 
but 1, 2, 4, 5 is not.
Examples

consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

consecutive_combo([44, 46], [45]) ➞ True

Notes

    The input lists will have unique values.
    The input lists can be in any order."""
            
# def consecutive_combo(lst1, lst2):
#     lst=list(set(lst1+lst2))
#     for i in range(1,len(lst)):
#         if lst[i]- lst[i-1]!=1:
#             return False
        
#     return True

# print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
# print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))

"""7.Tallest Skyscraper
A city skyline can be represented as a 2-D list with 1s representing buildings. In the example below, the height of 
the tallest building is 4 (second-most right column).

[[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]

Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.
Examples

tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 3

tallest_skyscraper([
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 4

tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 2

Notes

N/A"""

# def tallest_skyscraper(lst):
#     lst1= [sum(x) for x in zip(*lst)]
#     return max(lst1)
    


# print(tallest_skyscraper([
#   [0, 1, 0, 0],
#   [0, 1, 0, 0],
#   [0, 1, 1, 0],
#   [1, 1, 1, 1]
# ]))

# print(tallest_skyscraper([
#   [0, 0, 0, 0],
#   [0, 1, 0, 0],
#   [0, 1, 1, 0],
#   [1, 1, 1, 1]
# ]) )


"""8.Sales by Match
Given a list of integers representing the color of each sock, determine how many pairs of socks with matching colors there are. For example, there are 7 socks with colors [1, 2, 1, 2, 1, 3, 2]. There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

Create a function that returns an integer representing the number of matching pairs of socks that are available.
Examples

sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]) ➞ 3

sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]) ➞ 4

sock_merchant([]) ➞ 0"""

# def sock_merchant(lst):
#     my_dict={i:ist.count(i) for i in lst}
#     pairs=0
#     for value in my_dict:
#         if my_dict[value]%2!=0:
#             add=(value-1)/2
#             pairs+=add
#             return pairs
#         else:
#             add1=my_dict[value]/2
#             pairs+=add1
#             return pairs
    
    
#     print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))
#     print(sock_merchant([]))


"""9.Remove The Word!
Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.
Examples

remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]

remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]

remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []

Notes

    If number of times a letter appears in the list is greater than the number of times the letter appears in the string, the extra letters should be left behind (see example #2).
    If all the letters in the list are used in the string, the function should return an empty list (see example #3)."""

def remove_letters(letters, word):
    for i in word:
        letters = [j for j in letters if j != i]
    return letters
print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))
print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit"))

"""10.Majority Vote
Create a function that returns the majority vote in a list.
A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).
Examples

majority_vote(["A", "A", "B"]) ➞ "A"

majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"

majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None

Notes

    The frequency of the majority element must be strictly greater than 1/2.
    If there is no majority element, return None.
    If the list is empty, return None."""
    
def majority_vote(lst):
    lst1=set(lst)
    for i in lst1:
        count=lst.count(i)
        if count>len(lst)/2:
            return i
        

print(majority_vote(["A", "A", "B"]))
print(majority_vote(["A", "A", "A", "B", "C", "A"]))



"""11.Geometry 3: Perimeter of a Triangle
Write a function that takes the coordinates of three points in the form of a 2d array and returns the perimeter of the triangle. 
The given points are the vertices of a triangle on a two-dimensional plane.
Examples

perimeter([[15, 7], [5, 22], [11, 1]]) ➞ 47.08

perimeter([[0, 0], [0, 1], [1, 0]]) ➞ 3.41

perimeter([[-10, -10], [10, 10 ], [-10, 10]]) ➞ 68.28

Notes

    The given points always create a triangle.
    The numbers in the argument array can be positive or negative.
    Output should have 2 decimal places
    This challenge is easier than it looks."""

def perimeter(lst):
    a=(lst[0][0]-lst[1][0])**2 +(lst[0][1]-lst[1][1])**2
    b=(lst[0][0]-lst[2][0])**2 +(lst[0][1]-lst[2][1])**2
    c=(lst[1][0]-lst[2][0])**2 +(lst[1][1]-lst[2][1])**2
    k=a**0.5+b**0.5+c**0.5
    perimeter=(round(k,2))
    return perimeter
print(perimeter(([[15, 7], [5, 22], [11, 1]])))
        
"""12.Count and Identify Data Types

Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. 
Finally return the total in a list.

List order is:

[int, str, bool, list, tuple, dictionary]

Examples

count_datatypes(1, 45, "Hi", False) ➞ [2, 1, 1, 0, 0, 0]

count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) ➞ [3, 0, 0, 1, 1, 0]

count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23) ➞ [2, 2, 3, 1, 0, 2]

count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]) ➞ [2, 0, 1, 2, 2, 0]"""

def count_datatypes(*args):
    data_types = [int, str, bool, list, tuple, dict]
    counts = [0] * len(data_types)

    for arg in args:
        for i, data_type in enumerate(data_types):
            if isinstance(arg, data_type):
                counts[i] += 1

    return counts

print(count_datatypes(1, 45, "Hi", False))
        
        
# print(count_datatypes(1, 45, "Hi", False))
# def count_datatypes(*args):
#     counts = {
#         'int': 0,
#         'bool': 0,
#         'str': 0,
#         'list': 0,
#         'tuple': 0,
#         'dict': 0,
        
#     }
#     for arg in args:
#         if isinstance(arg, int):
#             counts['int'] += 1
#         elif isinstance(arg, str):
#             counts['bool'] += 1
#         elif isinstance(arg, bool):
#             counts['str'] += 1
#         elif isinstance(arg, list):
#             counts['list'] += 1
#         elif isinstance(arg, tuple):
#             counts['tuple'] += 1
#         elif isinstance(arg, dict):
#             counts['dict'] += 1
        
#     return [counts['int'],counts['str'], counts['bool'], counts['list'], counts['tuple'], counts['dict']]
# print(count_datatypes(1, 45, "Hi", False))
# print(count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23))

# def count_datatypes(*args):
#     counts = [0, 0, 0, 0, 0, 0]  # int, str, bool, list, tuple, dictionary
#     for arg in args:
#         if isinstance(arg, int):
#             counts[0] += 1
#         elif isinstance(arg, str):
#             counts[1] += 1
#         elif isinstance(arg, bool):
#             counts[2] += 1
#         elif isinstance(arg, list):
#             counts[3] += 1
#         elif isinstance(arg, tuple):
#             counts[4] += 1
#         elif isinstance(arg, dict):
#             counts[5] += 1
#     return counts
# print((count_datatypes(1, 45, "Hi", False)))

    

"""18.
Multiplication Table
Your task, is to create N x N multiplication table, of size n provided in parameter.

For example, when n is 5, the multiplication table is:

    1, 2, 3, 4, 5
    2, 4, 6, 8, 10
    3, 6, 9, 12, 15
    4, 8, 12, 16, 20
    5, 10, 15, 20, 25

This example will result in:

[[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]

Examples

multiplication_table(1) ➞ [[1]]

multiplication_table(3) ➞ [[1, 2, 3], [2, 4, 6], [3, 6, 9]]"""

def multiplication_table(n):
    table = []
    for i in range(1, n+1):
        row = []
        for j in range(1, n+1):
            row.append(i*j)
        table.append(row)
    return table

        


print( multiplication_table(1))
print(multiplication_table(3))
"""19.Sharing is Caring
Given a list of numbers, create a function that removes 25% from every number in the list except the smallest number,
and adds the total amount removed to the smallest number.
Examples

show_the_love([4, 1, 4]) ➞ [3, 3, 3]

show_the_love([16, 10, 8]) ➞ [12, 7.5, 14.5]

show_the_love([2, 100]) ➞ [27, 75]

Notes

There will only be one smallest number in a given list."""

def show_the_love(lst):
    remove_lst=[]
    for i in lst:
        remove_lst.append(i- i*25/100)
        return remove_lst
    

print(show_the_love([4, 1, 4]))

    
        
        
