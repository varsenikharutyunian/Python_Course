"""1. Write a function that takes a string name and a number num (either 0 or 1) and return
"Hello" + name if num is 1, otherwise return "Bye" + name.
Examples
say_hello_bye("alon", 1) ➞ "Hello Alon"
say_hello_bye("Tomi", 0) ➞ "Bye Tomi"
say_hello_bye("jose", 0) ➞ "Bye Jose"""
# name=input("Enter name > ")
# num=int(input("Enter num >"))
# if num==1:
#     print("Hello"+ " " + name.capitalize())
# elif num==0:
#     print("Bye"+ " " + name.capitalize())

# def say_hello_bye(name,num):
#     if name=="alon" and num == 1:
#         return f"Hello {name.capitalize()}"
#     if name=="Tomi" and num == 0:
#         return f"Bye {name}"
#     else:
#         return f"Bye {name.capitalize()}"
    
# print(say_hello_bye("alon", 1))
# print(say_hello_bye("Tomi", 0))
# print(say_hello_bye("jose", 0))
    
"""2. Create a function that takes a list (slot machine outcome) and returns True if all elements 
in the list are identical, and False otherwise. The list will contain 4 elements.
Examples
test_jackpot(["@", "@", "@", "@"]) ➞ True
test_jackpot(["abc", "abc", "abc", "abc"]) ➞ True
test_jackpot(["SS", "SS", "SS", "SS"]) ➞ True
test_jackpot(["&&", "&", "&&&", "&&&&"]) ➞ False
test_jackpot(["SS", "SS", "SS", "Ss"]) ➞ False  """
# slot=list(input("enter  element >enumerate"))
# slot = ["@", "@", "@", "@"]
# slot=["abc", "abc", "abc", "abc"]
#  slot=["SS", "SS", "SS", "SS"]
# slot=["&&", "&", "&&&", "&&&&"]
# slot=["SS", "SS", "SS", "Ss"]
# if len(slot)==4 and slot[0]==slot[1]==slot[2]==slot[3]:
#     print("True")
# else:
#     print("False")

"""3. Create a function that takes an array of hurdle heights and a jumper's 
jump height, and determine whether or not the hurdler can clear all the hurdles.
A hurdler can clear a hurdle if their jump height is greater than or equal to the hurdle height.
Examples
hurdle_jump([1, 2, 3, 4, 5], 5) ➞ True
hurdle_jump([5, 5, 3, 4, 5], 3) ➞ False
hurdle_jump([5, 4, 5, 6], 10) ➞ True
hurdle_jump([1, 2, 1], 1) ➞ False
Notes
Return True for the edge case of an empty array of hurdles. (Zero hurdles means that any 
jump height can clear them)."""

# def hurdle_jump(hurdle_heights, jump_height):
#   for i in hurdle_heights:
#     if i >= jump_height:
#       return False
#     else:
#       return True


# print(hurdle_jump([1, 2, 3, 4, 5], 5))
# print(hurdle_jump([5, 5, 3, 4, 5], 3))
# print(hurdle_jump([5, 4, 5, 6], 10))
# print(hurdle_jump([1, 2, 1], 1))

"""4. Create a function that takes a number as its argument and returns a list of all its factors.
Examples
factorize(12) ➞ [1, 2, 3, 4, 6, 12]
factorize(4) ➞ [1, 2, 4]
factorize(17) ➞ [1, 17]
Notes
The input integer will be positive.
A factor is a number that evenly divides into another number without leaving a remainder. 
The second example is a factor of 12, because 12 / 2 = 6, with remainder 0."""


# def factorize(num):
#     factors = []
#     for i in range(1, num + 1):
#         if num % i==0 :
#             factors.append(i)
#     return factors
# print(factorize(12))
"""5. Create a function that returns the number of palindrome numbers in a specified range (inclusive).
For example, between 8 and 34, there are 5 palindromes: 8, 9, 11, 22 and 33. 
Between 1550 and 1552 there is exactly one palindrome: 1551.
Examples
count_palindromes(1, 10) ➞ 9
count_palindromes(555, 556) ➞ 1
count_palindromes(878, 898) ➞ 3
Notes
A palindrome number is a number which remains the same when its digits are reversed. For example, 
2552 reversed is still 2552. The reflectional symmetry of this number makes it a palindromic number.
Single-digit numbers are trivially palindrome numbers."""



# def count_palindromes(start, end):
#     count = 0
#     for num in range(start, end + 1):
#         if str(num) == str(num)[::-1]:
#             count += 1
#     return count

# print(count_palindromes(1, 10))
# print(count_palindromes(555,556))
# print(count_palindromes(878, 898))

"""6. Write a function that takes a string, breaks it up and returns it with vowels 
first, consonants second. For any character that's not a vowel (like special characters or spaces), treat them like consonants.
Examples
split("abcde") ➞ "aebcd"
split("Hello!") ➞ "eoHll!"
split("What's the time?") ➞ "aeieWht's th tm?"
Notes
Vowels are a, e, i, o, u.
Define a separate is_vowel() function for easier to read code (recommendation)."""

VOWEL_LIST={"a","e","i","o","u"}
def is_vowel(letter):
    if letter is VOWEL_LIST:
        return True
    
    return False
            
def vowel_first(expression):
    
    vowels =""
    
    for letter in expression:
        if is_vowel(letter):
            vowels += letter
            
            ind=expression.index(letter)
            
            expression= expression[:ind]+expression[ind +1:]
            
    return vowels + expression

print(vowel_first("abcde"))


"""7. Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.
Examples
hacker_speak("javascript is cool") ➞ "j4v45cr1pt 15 c00l"
hacker_speak("programming is fun") ➞ "pr0gr4mm1ng 15 fun"
hacker_speak("become a coder") ➞ "b3c0m3 4 c0d3r"
Notes
In order to work properly, the function should replace all "a"s with 4, "e"s with 3, "i"s with 1, 
"o"s with 0, and "s"s with 5."""

# def hacker_speak(some_string:str):
#     dic={"a":"4",
#         "e":"3",
#         "i":"1",
#         "o":"0",             
#         "s":"5"}
#     for i in dic:
#         return some_string.replace(i,dic[i])
# print(hacker_speak("javascript is cool") )
# print(hacker_speak("programming is fun")) 

# print(hacker_speak("become a coder") )



# def hacker_speak(some_string):
    
#     dic = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5'}
#     return some_string.translate(str.maketrans(dic))
# print( hacker_speak("javascript is cool"))
# print( hacker_speak("programming is fun"))
# print( hacker_speak("become a coder"))

"""8. Create a function that takes an integer and returns it as an ordinal number.
An Ordinal Number is a number that tells the position of something in a list,
such as 1st, 2nd, 3rd, 4th, 5th, etc.
Examples
return_end_of_number(553) ➞ "553-RD"
return_end_of_number(34) ➞ "34-TH"
return_end_of_number(1231) ➞ "1231-ST"
return_end_of_number(22) ➞ "22-ND"
return_end_of_number(412) ➞ "412-TH"""

# def end_of_number(num):
#     if num % 100 in [11, 12, 13]:
#         name= "th".upper()

#     elif num%10==1:
#         name= "st".upper()
#     elif num%10==2:
#         name="nd".upper()
#     elif num%10==3:
#         name="rd".upper()
#     else:
#         name= "th".upper()
#     return str(num)+ "-" + name
# print(end_of_number(553))
# print(end_of_number(34))
# print(end_of_number(1231))
# print(end_of_number(22))
# print(end_of_number(412))

"""9. Create a function that converts Celsius to Fahrenheit and vice versa.
Examples
convert("35*C") ➞ "95*F"
convert("19*F") ➞ "-7*C"
convert("33") ➞ "Error"
Notes
Round to the nearest integer.
If the input is incorrect, return "Error".
For the formulae to convert back and forth, check the Resources tab."""

# def convert(temp,unit):
#     if unit=="C":
#         return (temp*1.8) + 32 
#     elif unit=="F":
#         return  (temp - 32) / 1.8
#     elif unit==" ":
#         return ("Error")
    
# print(int(convert(35,"C")),"*F")
# print(int(convert(19,"F")),"*C")
# print(convert(33," "))




# """10. Create a funcf=tion that finds the reverse complement of a ribonucleic acid (RNA) strand. 
# The RNA will be represented as a string containing only the characters "A", "C", "G" and "U".
# Since RNA can only (canonically) allow pairings of A/U and G/C, the complement of an RNA would be as follows:
# Original    Complement
# "AAA" "UUU"
# "UUU" "AAA"
# "GGG" "CCC"
# "CCC" "GGG"
# Your function should find the complement on the right AND also reverse the resulting string.
# Examples
# reverse_complement("GUGU") ➞ "ACAC"
# reverse_complement("UCUCG") ➞ "CGAGA"
# reverse_complement("CAGGU") ➞ "ACCUG"
# Notes
# You can assume all input seqeuences will be valid."""

# 1-in lucum

# input_txt="GUGU"

# mydict={"A": "U", "U":"A", "C":"G", "G":"C"}       

# converted_txt = " "
# for i in input_txt:
#     converted_txt += mydict[i]
# print(converted_txt[::-1])



# # 2-rd lucum
# def reverse_complement(txt):
#     complement={"A": "U", "U":"A", "C":"G", "G":"C"}
#     revers_complement = " "                                    
#     for i in txt:
#         revers_complement +=complement[i]
#     return revers_complement[::-1]
# print(reverse_complement("GUGU"))
# print(reverse_complement("UCUCG"))
#     # print(reverse_complement("CAGGU"))


# def reverse_complement(rna):
#     # Define the complement dictionary
#     complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
    
#     # Convert the RNA to a list of nucleotides
#     rna_list = list(rna)
    
#     # Reverse the list
    # rna_list.reverse()                                     3-rd lucum
    
#     # Replace each nucleotide with its complement
#     for i in range(len(rna_list)):
#         rna_list[i] = complement[rna_list[i]]
    
#     # Convert the list back to a string and return it
#     return ''.join(rna_list)

# rna = 'ACGU'
# print(reverse_complement('ACGU') ) # returns 'ACGU'











# 
# test_dict = {"a" : 4, "e" : 3, "i" : 1, "o":0, "s":5}

# print("The original dictionary : " + str(test_dict))
# res =dict(reversed(list(test_dict.items())))

# # printing reversed order dictionary
# print("The reversed order dictionary : " + str(res) )


# keys={"a":"4" ,"e":"3", "i":"1", "o":"0","s":"5"}           1-in lusum
# inp = "javascript is cool"

# for i in keys:
#   inp = inp.replace(i,keys[i])
# print (inp=="j4v45cr1pt 15 c00l")



"""11. Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and 
division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").
Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to 
have only two numbers between 1 valid operator. The return value should be a number.
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



def arithmetic_operation(string_number):
    # Split the string into three parts: the first number, the operator, and the second number
    parts = string_number.split()
    num1 = int(parts[0])
    operator = parts[1]
    num2 = int(parts[2])

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "//":
          num2!=0
          return num1 // num2
    else:
        return(-1)
print(arithmetic_operation("12 + 12"))
print(arithmetic_operation("23 - 21") ) 
print(arithmetic_operation("12 // 12") ) 
print(arithmetic_operation("12 * 21") )


# 12.xndir  1-in lucum
#  match case katarum e stugum ,ete c=b ,tpir a
def func(a:int,b:int,c:int):
    match c==b:
        case True:
            return a
        case False:
            return  b
a,b,c=1,2,2
print(func(a,b,c))


# 2-rd lucum
# a,b,c=(27,31,31)
# print((b==c)*a + (c==a)*b)
