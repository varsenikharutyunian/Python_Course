"""Magic Function
Create a class with a few functions like these examples.

    magic.replace("string", 'char', char') is a function that replaces all of the specified characters with different specified characters.
    magic.str_length("string") is a function that returns the length of the string.
    magic.trim(" string ") is a function that returns a string with truncated spaces at both the beginning and end.
    magic.list_slice(list, tuple) is a function that returns the items in the list that are between the specified indexes. If the length of the new list is 0, return -1.

Examples

magic.replace("AzErty-QwErty", "E", "e") ➞ "Azerty-Qwerty"

magic.str_length("hello world") ➞ 11

magic.trim("      python is awesome      ") ➞ "python is awesome"

magic.list_slice([1, 2, 3, 4, 5], (2, 4)) ➞ [ 2, 3, 4 ]"""

# class Magic:
    
#     @staticmethod   
#     def replace(string,c1,c2):
#         return string.replace(c1,c2)
#     @staticmethod
#     def str_length(string):
#         return len(string)
#     @staticmethod
#     def trim(string):
#         return string.strip()
#     @staticmethod
#     def list_slice(list,indexes):
#         start, end = indexes
#         new_list = lst[start:end+1]
#         return new_list if new_list else -1
        
    
    

# class Magic:
#     @staticmethod
#     def replace(string, old_char, new_char):
#         return string.replace(old_char, new_char)

#     @staticmethod
#     def str_length(string):
#         return len(string)

#     @staticmethod
#     def trim(string):
#         return string.strip()

#     @staticmethod
#     def list_slice(lst, indexes):
#         start, end = indexes
#         new_list = lst[start:end+1]
#         return new_list if new_list else -1
# magic = Magic()

# print(magic.replace("AzErty-QwErty", "E", "e"))
# # Output: Azerty-Qwerty

# print(magic.str_length("hello world"))
# # Output: 11

# print(magic.trim("      python is awesome      "))
# Output: python is awesome

# print(magic.list_slice([1, 2, 3, 4, 5], (2, 4)))
# Output: [2, 3, 4]
"""2.Ones, Threes and Nines (Version #2)
Given an integer between 0 and 26, make a variable (self.answer). That variable would be assigned to a string in this format:

"nines:your answer, threes:your answer, ones:your answer"

You need to find out how many ones, threes, and nines it would at least take for the number of each to add up to the given integer when multiplied by one, three or nine (depends).
Examples

ones_threes_nines(10) ➞ "nines:1, threes:0, ones:1"

ones_threes_nines(15) ➞ "nines:1, threes:2, ones:0"

ones_threes_nines(22) ➞ "nines:2, threes:1, ones:1"

Notes

    Each of the ones, threes or nines could only be either 0, 1 or 2.
    You must use a class.
    After the comma, you must put a space.
    See version #1 of this series."""
    
    # class ones_threes_nines:
    
"""3.Employee Parsing
In the class Employee, implement the instance attributes as firstname, lastname and salary.

Create the method from_string() which parses a string containing these attributes and assigns them to the correct properties.
Properties will be separated by a dash.
Examples

emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")

emp1.firstname ➞ "Mary"

emp1.salary ➞ 60000

emp2.firstname ➞ "John"

emp2.salary ➞ 55000

Notes

    The salary is an integer.
    Check the Resources for some helpful tutorials on how to do this."""
    
# class Employee:
#     def __init__ (self,firstname, lastname ,salary):
#         self.firstname=firstname
#         self.lastname=lastname
#         self.salary=salary
#     def emp1(self):
#         return f"{self.firstname}"
#     def emp1(self):
#         return f"{self.salary}"

# emp1 = Employee("Mary", "Sue", 60000)
# emp2 = Employee.from_string("John-Smith-55000")
# print(emp1.emp1())
# print(emp1.emp1())
# class Employee:
#     def __init__(self, firstname, lastname, salary):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.salary = salary
    
#     @classmethod
#     def from_string(cls, employee_string):
#         firstname, lastname, salary = employee_string.split('-')
#         return cls(firstname.strip(), lastname.strip(), float(salary.strip()))

    
"""3.To the Right, to the Right!
Create a class that imitates a select screen. For simplicity, the cursor can only move right!

In the display method, return a string representation of the list, but with square brackets around the currently selected element. Also, create the method to_the_right, which moves the cursor one element to the right.

The cursor should start at index 0.
Examples

menu = Menu([1, 2, 3])
menu.display() ➞ "[[1], 2, 3]"

menu.to_the_right()
menu.display() ➞ "[1, [2], 3]"

menu.to_the_right()
menu.display() ➞ "[1, 2, [3]]"

menu.to_the_right()
menu.display() ➞ "[[1], 2, 3]"

Notes

The cursor should wrap back round to the start once it reaches the end."""

# class Menu:
# 	def__init__(self,lst):
#         self.lst=lst
#         def to_the_right(self):
		
		
# 	def display(self):
		# write code here
    
"""5.People Sort
    Given a list of people objects, create a function that sorts the list by an attribute name. The attribute to sort by will be given as a string.

The Person class will only include these attributes in the following order:

    firstname
    lastname
    age

Examples

p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)

people_sort([p1, p2, p3], "firstname") ➞ [p2, p1, p3]
# Alice, Michael, Zoey

people_sort([p1, p2, p3], "lastname") ➞ [p3, p1, p2]
# Jones, Smith, Waters

people_sort([p1, p2, p3], "age") ➞ [p2, p3, p1]
# 21, 29, 40"""

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def __repr__(self):
        return f"{self.firstname}" f"{self.lastname}" f"{str(self.age)}"
    
def people_sort(people, attribute):
    attribute_order = ["firstname", "lastname", "age"]
    attribute_index = attribute_order.index(attribute)
    return sorted(people, key=lambda p: getattr(p, attribute_order[attribute_index]))

# Testing the examples from the prompt
p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)


print(people_sort([p1, p2, p3], "firstname"))
# Output: [p2, p1, p3] (Alice, Michael, Zoey)

print(people_sort([p1, p2, p3], "lastname"))
# Output: [p3, p1, p2] (Jones, Smith, Waters)

print(people_sort([p1, p2, p3], "age"))
# Output: [p2, p3, p1] (21, 29, 40)

"""6.Wait... Who Am I?
Hello there, I... seem to not remember who I am, my memories is all... cloudy, although maybe if I could piece it together...

Oh! Maybe you could help me make a class that helps me remember things. Maybe a method called add that would add to my memory if I would recall things and a remember method that would let me recall a specific memory.

But you have to make add more flexible, I might recall many things in an instant or only one that I would forget again.
Examples :D

# add method doesn't return anything.
memories.add(name="Shane", gender="M", catch_phrase="bazinga")

memories.add(work="None", love_life=0)

memories.add(adress="car")

memories.remember("work") ➞ "None"

memories.remember("gender") ➞ "M"

# If memory was not added, return False
memories.remember("lover") ➞ False

Notes

The add method should be able to handle any number of arguments."""
class Memories:
    def __init__(self,**kwargs):
        self.name=kwargs['name']
        self.gender=kwargs['gender']
        self.catch_phrase=kwargs['catch_phrase']
    
    
memories.add=Memories(name="Shane", gender="M", catch_phrase="bazinga")

# memories.add(work="None", love_life=0)

# memories.add(adress="car")
    
# print(memories.remember("work") =="None")

print(memories.add.gender)


class car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, **kwargs):
        # access args index like array does
        self.speed = kwargs['s']
        self.color = kwargs['c']


# creating objects of car class
audi = car(s=200, c='red')
bmw = car(s=250, c='black')
mb = car(s=190, c='white')

# printing the color and speed of cars
print(audi.color)
print(bmw.speed)


    
    
    
    
    
"""8.Employee Class with Keywords

Create a class Employee that will take a full name as argument, as well as a set of none, one or more keywords. 
Each instance should have a name and a lastname attribute plus one more attribute for each of the keywords, if any.
Examples

john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")

john.name ➞ "John"
mary.lastname ➞ "Major"
richard.height ➞ 178
giancarlo.nationality ➞ "Italian"

Notes

    First and last names will be separated by whitespace. The test will not include any middle names or initials."""
    
class Employee:
    def __init__(self,ful_name, **kwargs):
        self.name=ful_name.split()[0]
        self.lastname=ful_name.split()[1]
        for key,value in kwargs.items():
            self.__setattr__(key,value)
            
        
john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")

print(john.name )
print(mary.lastname )
print(richard.height)
print(giancarlo.nationality)

        
9.

