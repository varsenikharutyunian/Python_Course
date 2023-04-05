#  24   tnainner

"""1.Create a function that takes a list containing only numbers and return the first element."""
numbers=[1, 2, 3 ]
print(numbers[0])


"""2.Create a function that takes a list of numbers. Return the largest number in the list."""
numbers =[4, 5, 1, 3]
numbers_max =max(numbers)
print(numbers_max)

"""3. Create a function that takes a list of numbers and returns the smallest
number in the list."""

numbers =[34, 15, 88, 2]
numbers_min =min(numbers)
print(numbers_min)

"""4.Create a function that takes a list and returns the difference between 
the biggest and smallest numbers."""

numbers =[10, 4, 1, 4, -10, -50, 32, 21]
numbers_min =min(numbers)     #Smallest number is -50, biggest is 32.
number_mar=max(numbers)        #Biggest number is 32.
print(max(numbers) -min(numbers))

"""5.Create a function to concatenate two integer lists."""

numbers1=[1, 3, 5]
numbers1.extend ([2, 6, 8])
print(numbers1)

       
"""6.Given a list of numbers, return True if the sum of the values in the 
list is less than 100; otherwise return False."""

numbers=[5, 57]

print(sum(numbers) < 100 * True and sum(numbers)>= 100 * False)

"""7. Given a list of integers, determine whether the sum of its elements is even or odd."""

numbers = [0, 1, 5]
# If the input list is empty, consider it as a list with a zero [0]
print((int(sum(numbers)%2 == 0)) * "even" + (int(sum(numbers)%2!= 0 )* "odd" ) or int(sum(numbers)==0)* "even")


"""8.Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM."""

 
import datetime
d = datetime.datetime.strptime("12/10/2020", "%d/%m/%Y")
s = d.strftime('%Y%m%d')
print(s)    
# data = "12/31/2019"
# data=data.replace("12/31/2019", "2019/31/12" )  
# data1=data.replace("/",'')
# print(data1)
# data_time=input("enter data_time >")
# data_time = "12/31/2019"
# data1 ="20193112"
# data1=data_time.replace(data_time , data1) 
# print(data1)

"""9.Create a function that takes two numbers as arguments num, length and returns a list
of multiples of num until the list length reaches length."""
# def multiples(num, length):
#     return [*range(num, length*num+1, num)]

# print(multiples(7, 5))
x, y = (7, 5)
print(list(x, x*y + 1, y))


"""10.Create a function that takes a list of numbers lst, a string s and return a list of numbers as per the following rules:
"Asc" returns a sorted list in ascending order.
"Des" returns a sorted list in descending order.
"None" returns a list without any modification."""

x =[4,3,2,1],"Asc"


y= sorted(x)
z= sorted(x, reverse=True)
print(y=="Asc")*sorted(x) + (y=="Des") *sorted(x,revers=True) +(y=="None"*x)

