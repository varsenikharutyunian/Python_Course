"""icket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

    For n = 1230, the output should be
    solution(n) = true;
    For n = 239017, the output should be
    solution(n) = false."""
    


# def is_lucky(n):
#     # Convert the ticket number to a string
#     n_str = str(n)

#     # Get the length of the string
#     n_len = len(n_str)

#     # Check if the length is even
#     if n_len % 2 != 0:
#         return False

#     # Split the string into two halves
#     half_len = n_len // 2
#     first_half = n_str[:half_len]
#     second_half = n_str[half_len:]

#     # Convert the halves to lists of digits
#     first_half_digits = [int(d) for d in first_half]
#     second_half_digits = [int(d) for d in second_half]

#     # Check if the sums of the two halves are equal
#     if sum(first_half_digits) == sum(second_half_digits):
#         return True
#     else:
#         return False
# print(is_lucky(1230))


"""4.Your spouse is not concerned with the loss of material possessions but rather with his/her favorite pet. Is it gone?!

Given a dictionary of the stolen items and a string in lowercase representing the name of the pet (e.g. "rambo"), return:

    "Rambo is gone..." if the name is on the list.
    "Rambo is here!" if the name is not on the list.

Note that the first letter of the name in the return statement is capitalized.
Examples

 items = {
  "tv": 30,
  "timmy": 20,
  "stereo": 50,
} ➞ "Timmy is gone..."
# Timmy is in the dictionary.


 items = {
  "tv": 30,
  "stereo": 50,
} ➞ "Timmy is here!"
# Timmy is not in the  dictionary.


items = { } ➞ "Timmy is here!"
# Timmy is not in the dictionary."""

def find_it(items, name):
    if name in items:
        return f"{name.capitalize()},is gone"
    else:
        
        return f"{name.capitalize()},is here!"
items = {"tv": 30,   "timmy": 20,   "stereo": 50,} 
name= "rambo"

status= find_it(items,name)
print(status)


"""5.Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.

    wins get 3 points
    draws get 1 point
    losses get 0 points

Examples

football_points(3, 4, 2) ➞ 13

football_points(5, 0, 2) ➞ 15

football_points(0, 0, 1) ➞ 0"""
def football_points(wins, draws, losses):
    #  wins get 3 points
    # draws get 1 point
    # losses get 0 points
    return wins*3+draws*1+losses*0
print(football_points(3, 4, 2))

"""6.Create a function that takes a boolean variable flag and returns it as a string.
Examples

bool_to_string(True) ➞ "True"

bool_to_string(False) ➞ "False"

Notes

    Don't forget to return the result.
    If you get stuck on a challenge, find help in the Resources tab.
    If you're really stuck, unlock solutions in the Solutions tab."""
    
def bool_to_string(flag):
    return str(flag)
print(bool_to_string(True))

"""7.You call your spouse in anger and a "little" argument takes place. Count the total amount of insults used. 
Given a dictionary of insults, return the total amount of insults used.
Examples

total_amount_adjectives({ "a": "moron" }) ➞ 1

total_amount_adjectives({ "a": "idiot", "b": "idiot", "c": "idiot" }) ➞ 3

total_amount_adjectives({ "a": "moron", "b": "scumbag", "c": "moron", d: "dirtbag" }) ➞ 4

Notes

The dictionary will never be empty."""
def total_amount_adjectives(dct):
    return len(dct.values())
print(total_amount_adjectives({ "a": "moron" }))

def total_amount_adjectives(dct):
    count=0
    for i in enumerate(dct):
        count+=1
        return count
print(total_amount_adjectives({ "a": "moron" }))
    
        

"""8.The challenge is to recreate the functionality of the title() method into a function called emphasise(). 
The title() method capitalises the first letter of every word and lowercases all of the other letters in the word.
Examples

emphasise("hello world") ➞ "Hello World"

emphasise("GOOD MORNING") ➞ "Good Morning"

emphasise("99 red balloons!") ➞ "99 Red Balloons!"

Notes

    You won't run into any issues when dealing with numbers in strings.
    Please don't use the title() method directly :"""
def emphasise(txt):
    return txt.title()
print(emphasise("hello world"))

"""9.Create a function that takes a country's name and its area as arguments and returns the area of the country's proportion of the total world's landmass.
Examples

area_of_country("Russia", 17098242) ➞ "Russia is 11.48% of the total world's landmass"

area_of_country("USA", 9372610), "USA is 6.29% of the total world's landmass"

area_of_country("Iran", 1648195) ➞ "Iran is 1.11% of the total world's landmass"

Notes

    The total world's landmass is 148,940,000 [Km^2]
    Round the result to two decimal places.
    If you get stuck on a challenge, find help in the Resources tab."""
def area_of_country(name, area):
    total_world=(area/148940000)*100
    total=round(total_world,2)
    return f"{name}, is {total}% ,of the total world's landmass"
print(area_of_country("Russia", 17098242))

"""10.A student learning Python was trying to make a function. His code should concatenate a passed string name with string "Edabit" and store it in a variable called result. He needs your help to fix this code.
Examples

name_string("Mubashir") ➞ "MubashirEdabit"

name_string("Matt") ➞ "MattEdabit"

name_string("python") ➞ "pythonEdabit"

Notes

    Don't forget to return the result.
    If you get stuck on a challenge, find help in the Resources tab.
    If you're really stuck, unlock solutions in the Solutions tab."""
def name_string(name):
    b ="Edabit"
    return f"{name}{b}"
print(name_string("Mubashir"))

"""11.For each challenge of this series you do not need to submit a function. Instead, you need to submit a template string that can formatted in order to get a certain outcome.

Write a template string according to the following example. Notice that the template will be formatted twice:
Example

a = "John"
b = "Joe"
template = "yourtemplatestringhere"

template.format(1).format(a, b) ➞ "My best friend is Joe."""
a = "John"
b = "Joe"
template = "yourtemplatestringhere"
print("My best friend is {}".format("Joe"))


"""12.Given a lottery ticket (ticket), represented by a list of 2-value lists, create a function to find out if you've won the jackpot.

To do this, you must first count the "mini-wins" on your ticket. Each sublist has both a string and a number within it. If the character code of any of the characters in the string matches the number, you get a mini-win. Note you can only have one mini-win per sublist.

Once you have counted all of your mini-wins, compare that number to the other input provided (win). If your number of mini-wins is more than or equal to win, return Winner!. Else, return Loser!.
Examples

lottery([["YYW", 70], ["WXK", 65], ["RPDI", 88]], 2)
➞ "Loser!"

lottery([["KG", 80], ["NTBBVZ", 79], ["CI", 73], ["AGXMEE", 74], ["IU", 68], ["VOSP" , 84]], 1)
➞ "Winner!"

lottery([["ZSAMZB", 81], ["XWWCXP", 72], ["SYBRQOHP", 88], ["HJSVV", 75]], 1)
➞ "Loser!"

Notes

    All inputs will be in the correct format.
    Strings on ticket are not always the same length."""
    
#  def lottery(ticket, win):
# lottery=([["KG", 80], ["NTBBVZ", 79], ["CI", 73], ["AGXMEE", 74], ["IU", 68], ["VOSP" , 84]], 1)
# unicode_val = ord("KG")
# def lottery(ticket, win):
#     result = sum([1 for s, n in ticket if chr(n) in s])
#     return {}.format('Winner!' if result >= win else 'Loser!')

# print(lottery([["YYW", 70], ["WXK", 65], ["RPDI", 88]], 2)) # Loser!
# print(lottery([["KG", 80], ["NTBBVZ", 79], ["CI", 73], ["AGXMEE", 74], ["IU", 68], ["VOSP" , 84]], 1)) # Winner!
# print(lottery([["ZSAMZB", 81], ["XWWCXP", 72], ["SYBRQOHP", 88], ["HJSVV", 75]], 1)) # Loser!

"""13.Create a class that takes the following four arguments for a particular football player:

    name
    age
    height
    weight

Also, create three functions for the class that returns the following strings:

    get_age() returns "name is age age"
    get_height() returns "name is heightcm"
    get_weight() returns "name weighs weightkg"

Examples

 p1 = player("David Jones", 25, 175, 75)

 p1.get_age() ➞ "David Jones is age 25"
 p1.get_height() ➞ "David Jones is 175cm"
 p1.get_weight() ➞ "David Jones weighs 75kg"

Notes

name will be passed in as a string and age, height, weight will be integers."""



"""14.Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.

eval() is not allowed. In case of division, whenever the second number equals "0" return -1.

For example:

"15 // 0"  ➞ -1

Examples

arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24

arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0

arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144

arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1"""

def arithmetic_operation(n):
    num = n.split()
    num1=int(num[0])
    operation=num[1]
    num2= int(num[2])
    if operation=="+":
        return num1+num2
    elif operation=="-":
        return num1-num2
    elif operation=="*":
        return num1*num2
    elif num2==0:
        return -1
#    num2==n[0]
#    num3=[1]
print(arithmetic_operation("12 + 12"))
# print(arithmetic_operation("12 + 12") )

"""15.Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated 
twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.
Examples

stutter("incredible") ➞ "in... in... incredible?"

stutter("enthusiastic") ➞ "en... en... enthusiastic?"

stutter("outstanding") ➞ "ou... ou... outstanding?"""


def stutter(word):
    elips="..."
    question_mark="?"
    word1=word[0:2]
    return f"{word1}{elips}{word1}{elips}{word}{question_mark}"
    
print(stutter("incredible"))


"""16.A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

Create a function that determines whether a number is a Disarium or not.
Examples

is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32

is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

is_disarium(544) ➞ False

is_disarium(518) ➞ True

is_disarium(466) ➞ False

is_disarium(8) ➞ True"""


# def is_disarium(n):
#     for i in n:
# n=544
# print(num)
    #calculateLength() will count the digits present in a number    
def is_disarium(num):
    temp = 0
    for i in range(len(str(num))):
        temp += int(str(num)[i]) ** (i + 1)
    return temp == num
print(is_disarium(175))


"""17.Write a function that takes a list of lists and returns the value of all of the symbols in it, where each symbol adds or takes something from the total score. Symbol values:

    # = 5
    O = 3
    X = 1
    ! = -1
    !! = -3
    !!! = -5

A list of lists containing 2 #s, a O, and a !!! would equal (0 + 5 + 5 + 3 - 5) 8.

If the final score is negative, return 0 (e.g. 3 #s, 3 !!s, 2 !!!s and a X would be (0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return 0.
Examples

check_score([
  ["#", "!"],
  ["!!", "X"]
]) ➞ 2

check_score([
  ["!!!", "O", "!"],
  ["X", "#", "!!!"],
  ["!!", "X", "O"]
]) ➞ 0

check_score([
  ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
  ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
  ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
  ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
  ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
  ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
  ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
  ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
  ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
  ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
  ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
  ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
  ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
  ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
]) ➞ 12"""


# heck_score=[
#   ["#", "!"],
#   ["!!", "X"]
# ] 

# flat=[]
# for i in heck_score:
#     for x in i:
#         flat.append(x)
# print(flat)
# flat[0]="#"
# flat[0]=5
# flat[1]="!"
# flat[1]=-1
# flat[2]="!!"
# flat[2]=-3
# flat[3]="X"
# flat[3]=1
# print(sum(flat))

def calculate_score(lst):
    symbol_values = {"#": 5, "O": 3, "X": 1, "!": -1, "!!": -3, "!!!": -5}
    total_score = 0
    for sublst in lst:
        for symbol in sublst:
            total_score += symbol_values.get(symbol, 0)
    return total_score
print( calculate_score([
  ["#", "!"],
  ["!!", "X"]
]))
"""18.Create a function that takes a string's characters as ASCII and returns each character's hexadecimal value as a string.
Examples

convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"

convert_to_hex("Big Boi") ➞ "42 69 67 20 42 6f 69"

convert_to_hex("Marty Poppinson") ➞ "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"

Notes

    Each byte must be seperated by a space.
    All alpha hex characters must be lowercase."""
    
# def convert_to_hex(txt):
#     hexa= ''
#     for i in range(len(txt):
#         character=txt[i]
#         value=ord(character)
#         part = hex(value).lstrip("0x").rstrip("L")
#         hexa+=part
#         return hexa
#     printconvert_to_hex("hello world")
        
        
# def convert_to_hex(txt):
#     hex_str = ''
#     for i in txt:
#         hex_val = hex(ord(i))[2:]  # remove the '0x' prefix from the hex string
#         hex_str += hex_val + ' '
#     return hex_str.strip()  # remove the trailing space from the hex string
      
# print(convert_to_hex("hello world"))


"""19.Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.

Given a censored string and a string of the censored vowels, return the original uncensored string.
Example

uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"

uncensor("abcd", "") ➞ "abcd"

uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"""

# sxal
# def uncensor(txt, vowels):
#     vowels_index=0
#     for i in range(len(txt)):
#         if i=="*":
#             for j in vowels:
#                 return txt.replace(i,j)
#             vowels_index+=1
    
        # j=j[0]+1
        # if len(j)==0:
        #     return txt
# print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))  
# chicht
# def uncensor(txt: str, vowels: str) -> str:
#     uncensored_str = ''
#     vowel_index = 0
#     for i in txt:
#         if i == '*':
#             uncensored_str += vowels[vowel_index]
#             vowel_index += 1
#         else:
#             uncensored_str += i
#     return uncensored_str
   

# print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo")) 
# print(uncensor("abcd","")) 
        
"""20.Using markdown, it's possible to format links such as https://edabit.com/challenges, into something tidier like this. Notice how the text "Go to the challenges!" appears when hovering over the link.

This was achieved by using this code:

[this](https://edabit.com/challenges "Go to the challenges!")

Given the url, the new name and optionally the hover_text, return the tidied up hyperlink as a string.
Examples

tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!") ➞ "[this](https://edabit.com/challenges "Go to the challenges!")"

tidy_link("https://www.google.com", "Google", "Google Search") ➞ "[Google](https://www.google.com "Google Search")"

tidy_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Click Me!") ➞ "[Click Me!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"

Notes

    Supply double quotes for the hover text.
    Keep in mind that some tests will not include an argument for hover_text."""
    
# def tidy_link(url, name, hover_text):
#     return f"{[name]},{url},{hover_text}"



# print(tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!"))
# print(tidy_link("https://www.google.com", "Google", "Google Search"))

# print(tidy_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Click Me!"))  

"""21.
Gbiven a list of words in the singular form, return a set of those words in the plural form if they appear more than once 
in the list.
Examples

pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }

Notes

    This is an oversimplification of the English language so no edge cases will appear.
    Only focus on whether or not to add an s to the ends of words.
    All tests will be valid."""
    
def pluralize(lst):
    lst1=set(lst)
    lst2=lst1.difference()
    for i in lst2:
    
        return {i[:]+"s",}
    # i+=1
      
        
print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))
print(["chair", "pencil", "arm"])
        

"""21.Create a function that takes a list and string. 
The function should remove the letters in the string from the list, and return the list.
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

        
        
"""22.Create a function that takes a string txt and censors any word from a given list lst. 
 The text removed must be replaced by the given character char.
Examples
censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"

censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")

censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"""

# def censor_string(txt, lst, char):
#     censor_string
    
    
#     for i  in  txt:
#         for j in lst:
#             if i==j:
#                 return 
                
                
#   censor_string= "Today is a Wednesday!"
#   print(" ".join())     
    
            
# print(censor_string("Today is a Wednesday!", ["Today", "a"]) )


censor_string="Today is a Wednesday!"
censor_string= censor_string.split(" ") 
print(censor_string)

