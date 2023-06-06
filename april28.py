
"""edabid /hard/string
1.Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

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
    The operators are * - + and //."""
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

"""2.Disarium Number
A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

Create a function that determines whether a number is a Disarium or not.
Examples

is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32

is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

is_disarium(544) ➞ False

is_disarium(518) ➞ True

is_disarium(466) ➞ False

is_disarium(8) ➞ True

Notes

Position of the digit is 1-indexed.
A recursive version of this challenge can be found via this link."""
    
    
    

def is_disarium(num):
    temp = 0
    for i in range(len(str(num))):
        temp += int(str(num)[i]) ** (i + 1)
    return temp == num
print(is_disarium(175))    


"""3.Add the Values of the Symbols in a Matrix
   Write a function that takes a list of lists and returns the value of all of the symbols in it, where each symbol adds or takes something from the total score. Symbol values:

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

"""4.Convert to Hex
Create a function that takes a string's characters as ASCII and returns each character's hexadecimal value as a string.
Examples

convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"

convert_to_hex("Big Boi") ➞ "42 69 67 20 42 6f 69"

convert_to_hex("Marty Poppinson") ➞ "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"

Notes

    Each byte must be seperated by a space.
    All alpha hex characters must be lowercase."""
    
def convert_to_hex(txt):
    hex_str = ''
    for i in txt:
        hex_val = hex(ord(i))[2:]  # remove the '0x' prefix from the hex string
        hex_str += hex_val + ' '
    return hex_str.strip()  # remove the trailing space from the hex string
      
print(convert_to_hex("hello world"))

"""5.C*ns*r*d Str*ngs

Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.

Given a censored string and a string of the censored vowels, return the original uncensored string.
Example

uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"

uncensor("abcd", "") ➞ "abcd"

uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"

Notes

    The vowels are given in the correct order.
    The number of vowels will match the number of * characters in the censored string."""
    
    
def uncensor(txt: str, vowels: str) -> str:
    uncensored_str = ''
    vowel_index = 0
    for i in txt:
        if i == '*':
            uncensored_str += vowels[vowel_index]
            vowel_index += 1
        else:
            uncensored_str += i
    return uncensored_str
   

print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo")) 
print(uncensor("abcd",""))  


"""6.  Tidy Hyperlinks
Using markdown, it's possible to format links such as https://edabit.com/challenges, into something tidier like this. Notice how the text "Go to the challenges!" appears when hovering over the link.

This was achieved by using this code:

[this](https://edabit.com/challenges "Go to the challenges!")

Given the url, the new name and optionally the hover_text, return the tidied up hyperlink as a string.
Examples

tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!") ➞ "[this](https://edabit.com/challenges "Go to the challenges!")"

tidy_link("https://www.google.com", "Google", "Google Search") ➞ "[Google](https://www.google.com "Google Search")"

tidy_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Click Me!") ➞ "[Click Me!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"""

def tidy_link(url, name, hover_text):
    return f"{[name]},{url},{hover_text}"
# if hover_txt==None:
#     return f"{[name]},{url}"

print(tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!"))
print(tidy_link("https://www.google.com", "Google", "Google Search"))

# print(tidy_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Click Me!"))

"""7.Remove The Word!
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


"""8.Pluralize!

iven a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.
Examples

pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }

Notes

    This is an oversimplification of the English language so no edge cases will appear.
    Only focus on whether or not to add an s to the ends of words.
    All tests will be valid.  """
def pluralize(lst):
    lst1=set(lst)
    lst2=lst1.difference()
    
    return set(i+'s'*(lst.count(i)>1) for i in lst)

print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))
print(["chair", "pencil", "arm"])  


"""9. Censor Words from List
Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.
Examples

censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"

censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")

censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"

Notes

N/A"""

def censor_string(txt, lst, char):
    new_lst=[]
    for word in txt.split():
        if word in lst:
            word=word.replace(word,char*len(word))
            new_lst.append(word)
        else:
            new_lst.append(word)
    return " ".join(new_lst)
                
                    
            
print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))

print(censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*"))


"""10.Secret Function 4.0
Create a function based on the input and output. Look at the examples, there is a pattern.
Examples

secret("p.one.two.three") ➞ "<p class='one two three'></p>"

secret("p.one") ➞ "<p class='one'></p>"

secret("p.four.five") ➞ "<p class='four five'></p>"

Notes

Input is a string."""

def secret(txt):
    simbol1="<"
    simbol2="class="
    simbol3="></p>"
    for i in txt.split():
        return  f"{simbol1}{i[0]}{simbol2}{i[1:]}{simbol3}"
print(secret("p.one.two.three"))
print(secret("p.one"))
print(secret("p.four.five"))

    




"""11.Create a function which takes in an encoded string and returns a dictionary according to the following example:
Examples

parse_code("John000Doe000123") ➞ {
  "first_name": "John",
  "last_name": "Doe",
  "id": "123"
}

parse_code("michael0smith004331") ➞ {
  "first_name": "michael",
  "last_name": "smith",
  "id": "4331"
}

parse_code("Thomas00LEE0000043") ➞ {
  "first_name": "Thomas",
  "last_name": "LEE",
  "id": "43"
}

Notes

    The string will always be in the same format: first name, last name and id with zeros between them.
    id numbers will not contain any zeros.
    Bonus: Try solving this using RegEx."""
    
def parse_code(txt):
    new_txt=["first name","last name", "id"]
    txt=txt.split("0")
    name=dict(zip(new_txt,txt))
    return name
print(parse_code("michael0smith004331"))
print(parse_code("Thomas00LEE0000043")) 
print(parse_code("michael0smith004331"))          
            

# def parse_code(code):
#     parts = code.split('000')
#     return {
#         'first_name': parts[0],
#         'last_name': parts[1],
#         'id': parts[2]


# print(parse_code("John000Doe000123"))
# print(parse_code("michael0smith004331"))
# print(parse_code("Thomas00LEE0000043"))

    
"""12.Loves Me, Loves Me Not...
"Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one, saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, loves them back.

Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.
Examples

loves_me(3) ➞ "Loves me, Loves me not, LOVES ME"

loves_me(6) ➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"

loves_me(1) ➞ "LOVES ME"

Notes

    Remember to return a string.
    The first phrase is always "Loves me"."""
    
def loves_me(n):
    result = ""
    for i in range(1, n+1):
        if i % 2 == 1:
            result += "Loves me"
        else:
            result += "Loves me not"
        if i != n:
            result += ", "
    result = result[:-9] + result[-9:].upper()  # capitalize last phrase
    return result
print(loves_me(30))


# def loves_me(n):
#     a = ["Loves me" if i%2==0 else "Loves me not" for i in range(n)]
#     return ", ".join([*a[:len(a)-1],a[-1].upper()])

# print(loves_me(3))

print(loves_me)