"""1. Create a function which returns the number of true values there are in an array.
Examples
countTrue([True, False, False, True, False]) ➞ 2
countTrue([False, False, False, False]) ➞ 0
countTrue([]) ➞ 0
Notes
Return 0 if given an empty array.
All array items are of the type bool (true or false)."""
# def count_true(are):
#     for i in are:
#         if i==True:
#             return are.count(True)
#         elif i!= True:
#             return 0
#     else:
#         return 0
# print(count_true([True, False, False, True, False]))
# print(count_true([False, False, False, False]))
# print(count_true([]))
"""2. Create a function that validates whether a number n is within the bounds of lower and upper. 
Return false if n is not an integer.
Examples
intWithinBounds(3, 1, 9) ➞ true
intWithinBounds(6, 1, 6) ➞ false
intWithinBounds(4.5, 3, 8) ➞ false
Notes
The term "within bounds" means a number is considered equal or greater than a lower bound and lesser (but not equal) 
to an upper bound, (see example #2).
# Bounds will be always given as integers."""


# def intWithinBounds(n,lower,upper):
#     if not isinstance(n,int):
#         return False
#     return  lower<=n<= upper
# print(intWithinBounds(3, 1, 9))
# print(intWithinBounds(6, 1, 6))
# print(intWithinBounds(4.5,3,8))


"""3. Create a function that takes three values:
h hours
m minutes
s seconds
Return the value that's the longest duration.
Examples
longestTime(1, 59, 3598) ➞ 1
longestTime(2, 300, 15000) ➞ 300
longestTime(15, 955, 59400) ➞ 59400"""


# def longestTime(h, m, s):
#     a=s/3600
#     b=m/60
#     if h>a and h>b:
#         return h
#     elif a>h and a>b:
#         return int(a*3600)
#     else:
#         return int(b*60)


# h, m, s = 1, 59, 3598
# h, m, s = 2, 300, 15000
# h, m, s = 15, 955,59400
# print(longestTime(h, m, s))


"""4. Create a function that takes the month and year (as integers) and returns the number of days in that month.
# Examples
# days(2, 2018) ➞ 28
# days(4, 654) ➞ 30
# days(2, 200) ➞ 28
# days(2, 1000) ➞ 28
# Notes
# Don't forget about leap years!"""
# # February month==2  # Leap year # April, June, September, November

# def days(month, year):
#     if month == 2:
        
#         if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            
#             return 29
#         else:
#             return 28
#     elif month in [4, 6, 9, 11]:
        
#         return 30
#     else:
        
#         return 31


# month,year=2,1000

# print(days(month,year))
        

"""5. Create a function that takes a string and censors words over four characters with *.
Examples
censor("The code is fourty") ➞ "The code is ******"
censor("Two plus three is five") ➞ "Two plus ***** is five"
censor("aaaa aaaaa 1234 12345") ➞ "aaaa ***** 1234 *****"
Notes
Don't censor words with exactly four characters.
If all words have four characters or less, return the original string.
The amount of * is the same as the length of the word."""


# def censor(original_string):
#     words=original_string.split()
#     censors_words=[]
#     for i in words:
#         if len(i)>4:
#             censors_word ="*" * len(i)
#             censors_words.append(censors_word) 
#         else:
#             censors_words.append(i) 
#     string = ' '.join(censors_words)
#     return string
    
# # print(censor("The code is fourty"))
# print(censor("aaaa aaaaa 1234 12345"))

"""6. Given a sentence, create a function that replaces every "a" as an article with "an absolute". 
It should return the same string without any change if it doesn't have any "a".
Examples
absolute("I am a champion!!!") ➞ "I am an absolute champion!!!"
absolute("Such an amazing bowler.") ➞ "Such an amazing bowler."
absolute("A man with no haters.") ➞ "An absolute man with no haters."
Notes
Watch for uppercase letters as shown in example #3."""


# def absolute(sentence):
#     return sentence.replace(" a ", " an absolute ").replace( "A", " An absolute" )
# print(absolute("I am a champion!!!"))
# print("Such an amazing bowler.")
# print("A man with no haters.")


            
"""7. Return an Array of Subarrays
Write a function that takes three arguments (x, y, z) and returns an array containing x subarrays (e.g. [[], [], []]), each containing y number of item z.
x Number of subarrays contained within the main array.
y Number of items contained within each subarray.
z Item contained within each subarray.
Examples
matrix(3, 2, 3) ➞ [[3, 3], [3, 3], [3, 3]]
matrix(2, 1, "edabit") ➞ [["edabit"], ["edabit"]]
matrix(3, 2, 0) ➞ [[0, 0], [0, 0], [0, 0]]
Notes
The first two arguments will always be integers.
The third argument is either a string or an integer."""

# 1-in lucum
def matrix(a, b, c):
    ret_list=[]
    for i in range(a):
        sub_list=[]
        for j in range(b):
            sub_list.append(c)
        ret_list.append(sub_list)
    return ret_list
    
print(matrix(3, 2, 3))

# # 2-rd lucum
# def matrix(a, b, c):
#     ret_list=[[c for j in range(b)] for i in range(a)]

#     return ret_list
    
# print(matrix(3, 2, 3))
# 3-rd lucum
# def matrix(a,b,c):
#     return a*[b*[c]]
# print(matrix(3, 2, 3))

    
"""8. Given a string of numbers separated by a comma and space, return the product of the numbers

Examples
multiplyNums("2, 3") > 6
multiplyNums("1, 2, 3, 4") ➞ 24
multiplyNums("54, 75, 453, 0") ➞ 0
multiplyNums("10, -2") ➞ -20
Notes
Bonus: Try to complete this challenge in one line!"""


# def multiply_numbers(numbers_string):
#     numbers_list = numbers_string.split(", ")
#     product = 1
#     for number in numbers_list:
#         product *= int(number)
#     return product
# print(multiply_numbers("2, 3"))

    
"""9. Create a function that takes a string road and returns the car that's in first place. 
The road will be made of "=", and cars will be represented by letters in the alphabet.
Examples
firstPlace("====b===O===e===U=A==") ➞ "A"
firstPlace("e==B=Fe") ➞ "e"
firstPlace("proeNeoOJGnfl") ➞ "l"
Notes
Return "No car available" if there is no car on the road and "No road available" if there is no road."""

# def firstPlace(road_cars:str)->str:
#     if not road_cars:
#         return "No road"
#     x=road_cars.replace("=","")
#     if not x.isalpha():
#         return "wrong input string"
#     if not x:
#         return  "No cars"
#     return x[-1]

# print(firstPlace("====b===O===e===U=A=="))

"""10. Create a function that takes an array of numbers between 1 and 10 (excluding one number) and returns the missing number.
Examples
missingNum([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
missingNum([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
missingNum([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
Notes
The array of numbers will be unsorted (not in order).
Only one number will be missing."""

def missingNum(array):
    expected_sum=sum(range(1,11))
    actual_sum =sum(array)
    one_number=expected_sum-actual_sum
    return one_number
    
print(missingNum([1, 2, 3, 4, 6, 7, 8, 9, 10]))   
print(missingNum([7, 2, 3, 6, 5, 9, 1, 4, 8]))
print(missingNum([10, 5, 1, 2, 4, 6, 8, 3, 9]))
    
