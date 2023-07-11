list1=[1,2,3]
list2=[1,2,3]
print(list1 is list2)
print("Hi")

myString = "abadfseadr"
myList = []
for i in myString:
    if i not in myList:
        myList.append(i)
print(myList)
myString = "abadfseadr"
myDict = {}
for i in myString:
    if i not in myDict:
        myDict[i] = 1
    else:
        myDict[i] += 1
x = myDict.pop('a')
print(myDict)

# myString = "abadfseadr"
# x = tuple()
# print(x)
# for i in myString:
#     if i not in x:
#         x.append(i)
# print(x)
given_range = 10
for i in range(given_range):
    if i%2==0:
        print(i)
        programmingLanguages = {'J':'Java','P':'Python'}
for key,value in programmingLanguages.items():
    print(key,value)
    list1 = [5,10,15,20]
list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']

for x in list1:
    for y in list2:
        print(x,y)
        
        n = 1

while n < 5:
    if n == 2:
        n = n+1
        continue
    print("Hello Pythonista")
    n = n+1
    
# 
# print("Hi" ,end ="")

# x=5
# y=6

# print(y==x)
# print(x,y)

def myFruits(f1,f2,f3,f4):
    FruitsList = [f1,f2,f3,f4]
    return FruitsList
    
output = myFruits("Apple","Bannana","Grapes","Orange")
print(output)

def function1():
    p ="Hello Pythonista" 
    def function2():
        print(p)
    function2()
    
function1()


"""1.Create a function that takes a list of
numbers and returns the sum of the two lowest 
positive numbers."""\


def sum_two_smallest_numbers(numbers):
    number=numbers 
    number.sort(reverse=True)
    a=number.pop()
    b=number.pop()
    if a>0 and b>0:
        return a+b

# print(sum_two_smallest_numbers([4,3,2,1]))

# lst= [1,2,8,9]
# print(range(len(lst)))

# def sum_two_smallest_numbers(lst):
#     new_lst =[]
    
#     for i in range(len(lst)-1):
#         if lst[i]<lst[i]+1:
#             new_lst.append(lst[i])
#             return new_lst

# def sum_two_smallest_numbers(numbers):



#     return sum(sorted(numbers)[:2])


# print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))

# print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))

# sum_two_smallest_nums([2, 9, 6, -1]) ➞ 8
def sum_two_smallest_nums(nums):
    positive_nums = sorted(filter(lambda x: x > 0, nums))
    return positive_nums[0] + positive_nums[1]


print(sum_two_smallest_nums([19, 5, 42, 2, 77]))

print(sum_two_smallest_nums([10, 343445353, 3453445, 3453545353453]))
print(sum_two_smallest_nums([879, 953, 694, -847, 342, 221, -91, -723, 791, -587]) )

print(sum_two_smallest_nums([3683, 2902, 3951, -475, 1617, -2385]))




    

    
# my_lst=["932c", "832u32", "2344b"]
def sort_by_letter(lst):
    return sorted (lst,key=lambda x: sorted(x)[-1])
print(sort_by_letter(["932c", "832u32", "2344b"]))
