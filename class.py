"""1.Simple OOP Calculator
Create methods for the Calculator class that can do the following:

    Add two numbers.
    Subtract two numbers.
    Multiply two numbers.
    Divide two numbers.

Examples

calculator = Calculator()

calculator.add(10, 5) ➞ 15

calculator.subtract(10, 5) ➞ 5

calculator.multiply(10, 5) ➞ 50

calculator.divide(10, 5) ➞ 2

Notes

    The methods should return the result of the calculation.
    Don't worry about needing to handle division by zero errors.
    See the Resources tab for some helpful tutorials on Python classes."""
    
class Calculator:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b!=0:
            return a//b
    
    
    
    
    
calculator = Calculator()   
print( calculator.add(10, 5))==15

print(calculator.subtract(10, 5)) ==5

print(calculator.multiply(10, 5)) == 50

print(calculator.divide(10, 5))== 2


"""2.Ones, Threes and Nines (Version #1)
Given an int, figure out how many ones, threes and nines you could fit into the number.
You must create a class. You will make variables (self.ones, self.threes, self.nines) to do this.
Examples

n1 = ones_threes_nines(5)
n1.nines ➞ 0

n1.ones ➞ 5

n1.threes ➞ 1

Notes

    Do not use the math module.
    See version #2 of this series."""
    
class ones_threes_nines:
    def __init__(self,num):
        self.ones=num
        self.trees=num//3
        self.nines =num//9

n1 = ones_threes_nines(5)
x=n1.nines
y=n1.ones
z=n1.trees
print(x)

print(y)
print(z)


"""3.Classes For Fetching Information on a Sports Player
Create a class that takes the following four arguments for a particular football player:

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
p1.get_weight() ➞ "David Jones weighs 75kg"""

class player():
    def __init__(self, name:str, age:int, height:int, weight:int):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        
    def get_age(self):
        return f"{self.name} is age {self.age}"
    def get_height(self):
        return (f"{self.name} is { self.height}cm")
    def get_weight(self):
        return (f"{self.name} weight {self.weight}kg")
        
p1 = player("David Jones", 25, 175, 75)
print(p1.get_age() )
print(p1.get_height() )
print(p1.get_weight())
        
        
        
"""4.Fullname and Email
Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:

    Form the fullname by simply joining the first and last name together, separated by a space.
    Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.

Examples

emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")

emp_1.fullname ➞ "John Smith"

emp_2.email ➞ "mary.sue@company.com"

emp_3.firstname ➞ "Antony"

Notes

    The attributes firstname and lastname are already made for you.
    See the Resources tab for some helpful tutorials on Python classes!  """   

class Employee:
    def __init__(self, first_name, last_name):
        self.fullname = f"{first_name} {last_name}"
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"
        self.first_name = first_name
        self.last_name = last_name
emp_1 = Employee("John", "Smith")
print(emp_1.fullname)  # Output: John Smith

emp_2 = Employee("Mary", "Sue")
print(emp_2.email)  # Output: mary.sue@company.com

emp_3 = Employee("Antony", "Walker")
print(emp_3.first_name)  # Output: Antony


"""5.Create a class named User and create a way to check the number of users (number of instances) that were created, so that the value can be accessed as a class attribute.
Examples

u1 = User("johnsmith10")
User.user_count ➞ 1

u2 = User("marysue1989")
User.user_count ➞ 2

u3 = User("milan_rodrick")
User.user_count ➞ 3

Make sure that the usernames are accessible via the instance attribute username.

u1.username ➞ "johnsmith10"

u2.username ➞ "marysue1989"

u3.username ➞ "milan_rodrick"

Notes

Feel free to check out the resources provided in the Resources tab for some helpful information on Python classes!"""



class User:
    user_count = 0

    def __init__(self,username):
        self.username = username
        User.user_count += 1 
        
    
u1 = User( "johnsmith10")
print(User.user_count)
print(u1.username)

u2 = User("marysue1989")
print(User.user_count)
print(u2.username)


u3 = User("milan_rodrick")
print(User.user_count)
print(u3.username)

"""6.Write a class called Name and create the following attributes given a first name and last name (as fname and lname):

    An attribute called fullname which returns the first and last names.
    An attribute called initials which returns the first letters of the first and last name. Put a . between the two letters.

Remember to allow the attributes fname and lname to be accessed individually as well.
Examples

a1 = Name("john", "SMITH")

a1.fname ➞ "John"

a1.lname ➞ "Smith"

a1.fullname ➞ "John Smith"

a1.initials ➞ "J.S"

Notes

    Make sure only the first letter of each name is capitalised.
    Check the Resources tab for some helpful tutorials on Python classes."""
    
class Name:
    def __init__(self,fname ,lname) -> None:
        self.fname=fname.capitalize()
        self.lname=lname.lower().capitalize()
        self.fulname=f"{self.fname} {self.lname}"
        self.initials=f"{self.fname[0]}.{self.lname[0]}"
        

a1 = Name("john", "SMITH")
print(a1.fname)
print(a1.lname)
print(a1.fulname)
print(a1.initials)

# a1.fname ➞ "John"

# a1.lname ➞ "Smith"

# a1.fullname ➞ "John Smith"

# a1.initials ➞ "J.S"


"""7.Counting Instances Created from a Class
Write a Composer class that has three instance variables:

    name
    dob
    country

Add an additional class variable .count which counts the total number of instances created.
Examples

# Just finished writing the Composer class
Composer.count ➞ 0

c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
Composer.count ➞ 1

c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
c3 = Composer("Johannes Brahms", 1833, "Germany")
Composer.count ➞ 3"""
class Composer:
    composer_count=0
    def __init__(self,name,dob,country) -> None:
        self.name=name
        self.dob=dob
        self.country=country
        Composer.composer_count+=1
        
# Just finished writing the Composer class
print(Composer.composer_count)

        
c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
print(Composer.composer_count)

c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
print(Composer.composer_count)

c3 = Composer("Johannes Brahms", 1833, "Germany")
print(Composer.composer_count)
        
        
"""8.Book Shelf
Create a Book class that has two attributes:

    .title
    .author

and two methods:

    A method named .get_title() that returns: "Title: " + the instance title.
    A method named .get_author() that returns: "Author: " + the instance author.

and instantiate this class by creating 3 new books:

    Pride and Prejudice - Jane Austen (PP)
    Hamlet - William Shakespeare (H)
    War and Peace - Leo Tolstoy (WP)

The name of the new instances should be PP, H, and WP, respectively.

For instance, if I instantiated the following book using this Book class:

    Harry Potter - J.K. Rowling (HP)

I would get the following attributes and methods:
Examples

HP.title ➞ "Harry Potter"
HP.author ➞ "J.K. Rowling"
HP.get_title() ➞ "Title: Harry Potter"
HP.get_author() ➞ "Author: J.K. Rowling"

Notes

    Read more about Python classes in Resources.
    Remember, after you've finished writing the class and its methods, you must instantiate it through the creation of new objects."""
    
class Book:
    def __init__(self,title,author) -> None:# Write your attributes and methods here
        self.title=title
        self.author=author    # Instantiate your Book class here
    def get_title(self):
        return f"Title:{self.title}"
    def get_author(self):
        return f"Author:{self.author}"
    
    
PP=Book("Pride and Prejudice", "Jane Austen")
print(PP.title)
print(PP.author)
print(PP.get_title())
print(PP.get_author())
H =Book("Hamlet"," William Shakespeare") 
print(H.title)
print(H.author)
print(H.get_title())
print(H.get_author())

WP=Book("War and Peace" ," Leo Tolstoy") 
print(WP.title)
print(WP.author)
print(WP.get_title())
print(WP.get_author())

"""9.Food for Everyone!
Create a Person class which will have three properties:

    Name
    List of foods they like
    List of foods they hate

In this class, create the method taste():

    It will take in a food name as a string.
    Return {person_name} eats the {food_name}.
    If the food is in the person's like list, add 'and loves it!' to the end.
    If it is in the person's hate list, add 'and hates it!' to the end.
    If it is in neither list, simply add an exclamation mark to the end.

Examples

p1 = Person("Sam", ["ice cream"], ["carrots"])

p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"

p1.taste("cheese") ➞ "Sam eats the cheese!"

p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"

Notes

    A person can have an empty list for foods they hate and/or love.
    Check the Resources for some helpful tutorials on Python classes."""
    
class Person:
    def __init__(self,name,like,hads) -> None:
        self.name=name
        self.like=like
        self.hads=hads
        
    def taste(self,food):
        if food in self.like:
            return f"{self.name} eats the {food} and loves it!"
        if food in self.hads:
            return f"{self.name} eats the {food} and hates it!"
        else:
            return f"{self.name} eats the cheese!"
        
p1 = Person("Sam", ["ice cream"], ["carrots"])
print(p1.taste("ice cream")) 
print(p1.taste("cheese"))
print(p1.taste("carrots"))
    
	

"""10.Big Countries 
A country can be said as being big if it is:

    Big in terms of population.
    Big in terms of area.

Add to the Country class so that it contains the attribute is_big. Set it to True if either criterea are met:

    Population is greater than 250 million.
    Area is larger than 3 million square km.

Also, create a method which compares a country's population density to another country object. Return a string in the following format:

{country} has a {smaller / larger} population density than {other_country}

Examples

australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

australia.is_big ➞ True
andorra.is_big ➞ False
andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"""

    
# class Country:
#     def __init__(self, name:str, population:str, area:float):
#         self.name = name
#         self.population = population
# 		self.area = area
# 		self.is_big=False
#         if self.population > 250000000 and  self.area >3000000:
#             self.is_big =True
#     def compare_pd(self, other):
#         isbiger= self.population/self.area > other.population / other.area
#         txt=["smaller","larger"][isbiger]
#         return f" {self.name} has a {txt} population density than {other.name}"
        
		
# australia = Country("Australia", 23545500, 7692024)
# print(australia.is_big)
# print(australia.compare_pd(australia))
# print(andorra.is_big)
# andorra = Country("Andorra", 76098, 468)		
class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.check_if_big()
    
    def check_if_big(self):
        return self.population > 250_000_000 or self.area > 3_000_000
    
    def compare_pd(self, other_country):
        if self.population / self.area > other_country.population / other_country.area:
            return f"{self.name} has a larger population density than {other_country.name}"
        else:
            return f"{self.name} has a smaller population density than {other_country.name}"


# Create Country instances
australia = Country("Australia", 23_545_500, 7_692_024)
andorra = Country("Andorra", 76_098, 468)

# Test the is_big attribute
print(australia.is_big)     # Output: True
print(andorra.is_big)       # Output: False

# Test the compare_pd() method
print(andorra.compare_pd(australia))    # Output: Andorra has a larger population density than Australia
