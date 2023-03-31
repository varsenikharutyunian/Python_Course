"""1. For this challenge, you are supposed to find the sum of the digits of a two-digit number.
45 ➞ 9
38 ➞ 11
67 ➞ 13
Need extra knowledge!! """
x=45
sum=45//10 + 45%10
print(sum)
"""2. A repdigit is a positive number composed out of the same digit. 
Create a function that takes an two-digit integer and returns whether it's a repdigit or not.
44 ➞ True
45 ➞ False
-44 ➞ False"""

x=44
y=x//10
z=x%10
print(y==z)
"""3. Write a function that takes an integer minutes and converts it to seconds.
5 ➞ 300
2 ➞ 120"""

x=5
min=60
print(x*min)
"""4. Create a function that takes the age in years and returns the age in days.
65 ➞ 23725
0 ➞ 0
20 ➞ 7300"""
x=20
y=365
print(x*y)
"""5. Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.
1,3 ➞ 3780
2,0 ➞ 7200"""
def sum(x, y):
   sum= x*3600 + y*60
   return sum
print(sum(1, 3))
print(sum(2, 0))

""""6. Create a function that accepts a measurement value in inches 
and returns the equivalent of the measurement value in feet."""

# Feet = Inches/ 12;
# print("The length in Feet",round(Feet,2))

"""7. Create a function that takes a number as an argument and returns "even"
for even numbers and "odd" for odd numbers."""

# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("{0} is Even".format(num))
# else:
#    print("{0} is Odd".format(num))
x=10
y=x%2
# print("zuyg"*(y==0)+"kent"*y)
print("zuig"*(not y)+"kent"*y)
   
   
	