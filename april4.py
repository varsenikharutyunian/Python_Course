# """1. Luke Skywalker has family and friends. Help him remind them who is who.
# Given a string with a name, return the relation of that person to Luke.
# Person  Relation
# Darth Vader father
# Leia    sister
# Han brother in law
# R2D2    droid
# Examples
# relation_to_luke("Darth Vader") ➞ "Luke, I am your father."
# relation_to_luke("Leia") ➞ "Luke, I am your sister."
# relation_to_luke("Han") ➞ "Luke, I am your brother in law."""
# name=input("enter name  >> ")
# # name =("Darth Vader","Leia","Han","R2D2" )
# if name=="Darth Vader":
#     print("Luke, I am your father.")
# elif name=="Leia":
#     print("Luke, I am your sister.")  
# elif name=="Han":
#     print("Luke, I am your brother in law.")
# else:             
#     print("droid")
    
# def relation_to_luke(a:str):
#     b="Luke, I am your"
#     c="father."
#     d="sister."
#     k="brother in law."
#     if a== "Darth Vader":
#         return f"{b}, {c}"
#     elif a== "Leia":
#         return f"{b}, {d}"
#     elif a== "Han":
#         return f"{b}, {k}"
#     else:
#         return "droid"
# print(relation_to_luke("Darth Vader"))
# print(relation_to_luke("Leia"))
# print(relation_to_luke("Han"))
# print(relation_to_luke("Hn"))
    
        
    
    
    
# """2. Create a function that takes damage and speed (attacks per second) and returns the amount 
# of damage after a given time.
# Examples
# damage(40, 5, "second") ➞ 200
# damage(100, 1, "minute") ➞ 6000
# damage(2, 100, "hour") ➞ 720000
# Notes
# Return "invalid" if damage or speed is negative."""
# def calculate_damage(damage, speed, time):
#     damage_per_second = damage * speed
#     total_damage = damage_per_second * time
#     return total_damage
# print(calculate_damage(40, 5, 1))  
# print(calculate_damage(100, 1, 60))  
# print(calculate_damage(2, 100, 3600)) 

# def damage(a:int,b:int,c:str):
#     z=a*b
#     if c=="second":
#         return z
#     elif c=="minute":
#         return z*60
#     elif c== "hour":
#         return z*3600
            
# print(damage(40, 5, "second"))
# print(damage(100, 1, "minute"))
# print(damage(2, 100, "hour"))


# """3. Create a function that takes a list of strings and integers, and filters out the 
# list so that it returns a list of integers only.
# Examples
# filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]
# filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]
# filter_list(["Nothing", "here"]) ➞ []"""

# my_list = ([1, 2, 3, "a", "b", 4])
# new_list = list(filter(lambda x: (type(x)==int) , my_list))
# print(new_list)

# my_lst=([1, 2, 3, "a", "b", 4])
# my_list=(["Nothing", "here"])

# 1-in lutsum
x =(["A", 0, "Edabit", 1729, "Python", "1729"])
# new_lst=[]
# for i in x:
#     if type(i)==int:
#         new_lst.append(i)
# print(new_lst)


# 2-rd luc
# def my_list(lst):
#     filter_lst =[]
#     while True:
#         for i in lst:
#             if type(i)==int:
#                 filter_lst.append(i)
#         return filter_lst
                
# print(my_list([1, 2, 3, "a", "b", 4]))
# print(my_list(["A", 0, "Edabit", 1729, "Python", "1729"]))

            
    
# 3-rd lutsum
# print(list(filter(lambda x: isinstance(x, int), list1)))
"""4.Create a function that takes a number as an argument and returns True or False depending on 
whether the number is symmetrical or not.A number is symmetrical when it is the same as its reverse.
Examples
is_symmetrical(7227) ➞ True
is_symmetrical(12567) ➞ False
is_symmetrical(44444444) ➞ True
is_symmetrical(9939) ➞ False
is_symmetrical(1112111) ➞ True"""

# 1-in lutsum

# def is_symmetrical_num(n):
#   return str(n) == str(n)[::-1]
# print(is_symmetrical_num(7227))
# print(is_symmetrical_num(12567))
# print(is_symmetrical_num(1244444444))
# print(is_symmetrical_num(9939))
# 2-rt lutsum

# n=input("Enter simetrical_num >  ")
# if str(n)==str(n)[::-1]:
#     print("True")
# else:
#     print("False")

#  3rd lucum
    
def is_symmetrical_num(n):
    a=str(n)
    if a[0:] == a[ ::-1]:
        return True
    else:
        return False

print(is_symmetrical_num(7227))
print(is_symmetrical_num(9939))
print(is_symmetrical_num(12567))

"""5.Create a function that changes all the elements in a list as follows:
Add 1 to all even integers, nothing to odd integers.
Concatenates "!" to all strings and make the first letter of the word a capital letter.
Changes all boolean values to its opposite.
Examples
change_types(["a", 12, True]) ➞ ["A!", 13, False]
change_types([13, "13", "12", "twelve"]) ➞ [13, "13!", "12!", "Twelve!"]
change_types([False, "False", "true"]) ➞ [True, "False!", "True!"]
Notes
There won't be any float values.
You won't get strings with both numbers and letters in them.
Although the task may be easy, try keeping your code as clean and as readable as possible!"""

# 1-in lutsum

# def change_types(lst):
#     result = []
#     for i in lst:
#         if isinstance(i, int) and i % 2 == 0:
#             result.append(i + 1)
#         elif isinstance(i, str):
#             result.append(i.capitalize() + "!")
#         elif isinstance(i, bool):
#             result.append(not i)
#         else:
#             result.append(i)
#     return result
# print(change_types(["a", 12, True]))  # ["A!", 13, False]
# print(change_types([13, "13", "12", "twelve"]))  # [13, "13!", "12!", "Twelve!"]
# print(change_types([False, "False", "true"]))  # [True, "False!", "True!"]
#  2-rd  lutsum
x=([13, "13", "12", "twelve"])
return_value=[]
for i in x:
    if isinstance(i, int) and i % 2 == 0:
        return_value.append(i + 1)
    elif isinstance(i, str):
        return_value.append(i.capitalize() + "!")
    elif isinstance(i, bool):
        return_value.append(not i)
    else:
        return_value.append(i)
    # return return_value
print(return_value)
            

"""6. Create a function that takes a string s and returns a list of two-paired characters. If the string has an odd number of characters, add an asterisk * in the final pair.
See the below examples for a better understanding:
Examples
string_pairs("mubashir") ➞ ["mu", "ba", "sh", "ir"]
string_pairs("edabit") ➞ ["ed", "ab", "it"]
string_pairs("airforces") ➞ ["ai", "rf", "or", "ce", "s*"]
Notes
Return [] if the given string is empty."""

# 1-in lucum

# x = ("airforces")
# new_lst = []
# for i in range(0, len(x), 2):
#     new_lst.append(x[i : i+2])
# print(new_lst)

#  2-rd lucum
def string_pairs(x):
    if len(x)==0:
        return []
    
    new_lst=[]
    for i in range(0,len(x),2):
        if i+1 < len(x):
            new_lst.append(x[i:i+2])
            
        else:
            new_lst.append(x[i] + "*")

    return new_lst

print(string_pairs("mubashir"))   
print(string_pairs("edabit"))
print(string_pairs("airforces"))


"""7. Create a function that takes two parameters and, if both parameters are strings, add them
as if they were integers or if the two parameters are integers, concatenate them.
Examples
stupid_addition(1, 2) ➞ "12"
stupid_addition("1", "2") ➞ 3
stupid_addition("1", 2) ➞ None
Notes
If the two parameters are different data types, return None.
All parameters will either be strings or integers."""
# def stupid_addition(param1, param2):
#     if isinstance(param1, str) and isinstance(param2, str):
#         return str(int(param1) + int(param2))
#     elif isinstance(param1, int) and isinstance(param2, int):
#         return str(param1) + str(param2)
#     else:
#         return "None"
# result1=stupid_addition(1, 2) 
# result2=stupid_addition("1", "2") 
# result3=stupid_addition("1", 2) 
# print(result1)
# print(result2)
# print(result3)

# 2-rd lutsum

x=("1",2)
for i in x:
    if isinstance(x[0], str) and isinstance(x[1], str):
        print(str(int(x[0]) + int(x[1])))
    elif isinstance(x[0], int) and isinstance(x[1], int):
        print( str(x[0]) + str(x[1]))
else:
    print("None")
    
    

"""8. Write a function that does the following operations: adding, subtracting, dividing,
or multiplying values. It is simply referred to as variable operation variable. Of course, t
he variables have to be defined, but in this challenge the variables will be defined for you.
All you have to do is look at the variables, do some string to integer conversions, use some 
if conditionals, and combine them based on the operation.
The numbers and operation will be given as strings, and you should return the value as a string as well.
Examples
operation("1", "2", "add" ) ➞ "3"
operation("4", "5", "subtract") ➞ "-1"
operation("6", "3", "divide") ➞ "2"
Notes
The numbers and operation will be given as strings, and you should also return the value as a string.
If the answer is "undefined", return "undefined" (e.g. dividing by zero).
For divide, go ahead and round down to an integer"""

# x=("1", "2", "add" )    
# if isinstance(x[0], str) and isinstance(x[1], str):
#     print(str(int(x[0])+int(x[1])))
#     y=("4", "5", "subtract")
#     if isinstance(y[0], str) and isinstance(y[1], str):
#         print(str(int(y[0])-int(y[1])))
#         z=("6", "3", "divide")
#         if isinstance(z[0], str) and isinstance(z[1], str):
#             print(str(int(z[0])/int(z[1])))

var1,var2,oper=("1", "0", "divide" )
if not(var1.isnumeric() and var2.isnumeric()):
    print("Please, enter numeric value")
    exit()
var1,var2=int(var1),int(var2)
return_value="Undefined"
if oper== "add":
    return_value= var1+var2
elif oper=="subtract":
    return_value=var1-var2
elif oper =="multiple":
    return_value=var1*var2
elif oper=="divide" and var2!=0:
    return_value=var1//var2
elif oper=="divide" and var2==0:
    return_value="var2!=0"
else:
    return_value="Plese corect the operator name"
print(str(return_value))
    


#  """9. Check if the given string consists of only letters and spaces and if every letter is 
# in lower case.
# Examples
# letters_only("PYTHON") ➞ False
# letters_only("python") ➞ True
# letters_only("12321313") ➞ False
# letters_only("i have spaces") ➞ True
# letters_only("i have numbers(1-10)") ➞ False
# letters_only("") ➞ False
# Notes
# Empty arguments will always return False.
# Input values will be mixed (symbols, letters, numbers)"""

txt=input("Enter letters >")
x=txt.isalpha()
y=txt.islower()
if x and y:
    print("True")
else:
    print("False")
"""10. Write a function that takes a list and determines whether it's strictly increasing, 
strictly decreasing, or neither.
Examples
check([1, 2, 3]) ➞ "increasing"
check([3, 2, 1]) ➞ "decreasing"
check([1, 2, 1]) ➞ "neither"
check([1, 1, 2]) ➞ "neither"
Notes
The last example does NOT count as strictly increasing, since 1-indexed 1 is not strictly greater 
than the 0-indexed 1.
Input lists have a minimum length of 2."""

check=input("Enter check >")
if check[0]< check[1]<check[2]:
    print("increasing")
elif check[0]> check[1]>check[2]:
    print("decreasing")
else:
    print("neither")
