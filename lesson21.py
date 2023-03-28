"""1.Create a function that takes a string and returns it as an integer."""
string="100"
integer = int(string)
print( integer)
"""2. Create a function that takes a boolean variable flag and returns it as a string."""
# bool = "True"
# print(bool)     @ sxal e
# bool= "False"
# print(bool)
"""3. Write a function that returns the string
"something" joined with a space " " and the given argument a."""
name = input("Enter name - >")
x="something is better than nothing"
y="something Bob Jane"
z="something"
result= (x* (name == " is better than nothing " ) +  y*(name == " Bob Jane")+(z*(name == "something")))
print(result)
"""4. Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name,
return the relation of that person to Luke."""
name = input("Enter name - >")
x =  "Luke, I am your father."
y = "Luke, I am your sister."
z= "Luke, I am your brother in law."
print(x * (name == "Darth Vader") + y*(name=="Leia")+ z*(name=="Han"))
"""5.Create a function that takes a string and returns the number (count)
 of vowels contained within it."""
name = input("Enter name - >")
print(name.count("a")+name.count("e")+name.count("i")+name.count("o")+name.count("u"))
"""6.Create a function that returns True if a given
 inequality expression is correct and False otherwise."""     # sxal e
# x=3<7<11 
y=13 > 44 > 33 > 1
# z=1 < 2 < 6 < 9 > 3
eval("print(y)")                                    
                                      #  eval funkcia stugum e ev tpum "True"
# 
# print(x )
# print(y)
# print(z)
"""7.Create a function that replaces all the vowels in a string with a specified character."""
input_str = input("enter string - >")
print(input_str.replace("a","#" ) .replace("e","#"))

"""8.Write a function that takes a credit card number and only displays the last four characters. 
The rest of the card number must be replaced by ************.
Examples
"1234123456785678" ➞ "************5678"
"8754456321113213" ➞ "************3213"
"35123413355523" ➞ "**********5523"""

x ="1234123456785678"
# ete qarti erkarutyun@ 16 e
# print(12*("*") + x[-4:])  
#   erkrord exanak
# y="35123413355523"
print(len(x)-4) * "*"+ x[-4: ]
print(result)



""""9.Create a function that takes a string (will be a person's first and last name)
and returns a string with the first and last name swapped."""

name=input("enter name_surname ->")
name=name.split()
print(name[1] +" " +name[0])
print(fstring)