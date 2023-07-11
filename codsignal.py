# xndir 13
def solution(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return solution(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s
print(solution("(bar)"))


"""14.Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.

You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.

Example

For a = [50, 60, 60, 45, 70], the output should be
solution(a) = [180, 105]."""

def solution(a):
    lst=[]
    lst1=[]
    for i ,j in enumerate(list(a)):
        if i%2==0:
            lst.append(j)
        else:    
            lst1.append(j)
    return [sum(lst),sum(lst1)]
        
    
print(solution([50, 60, 60, 45, 70]))


# def alternatingSums(a):

#     return [sum(a[::2]),sum(a[1::2])]
# print(alternatingSums([50, 60, 60, 45, 70]))



""" 15
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]

the output should be

solution(picture) = ["*****","*abc*",*ded*","*****"]"""


def solution(picture):
    lst=[]
    lst.append("*" * (len(picture[0])+2))
    for i  in range(len(picture)):
        lst.append("*"+picture[i]+"*")
    lst.append("*"* (len(picture[0])+2))
    return lst
print(solution(["abc","ded"]))

# def addBorder(picture):
#     answer = []
#     answer.append("*" * (len(picture[0]) + 2))
#     for i in range (len(picture)):
#         answer.append("*" + picture[i] + "*")
#     answer.append("*" * (len(picture[0]) + 2))

#     return answer
# print(addBorder(["abc","ded"]))
"""16.Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

    For a = [1, 2, 3] and b = [1, 2, 3], the output should be
    solution(a, b) = true.

    The arrays are equal, no need to swap any elements.

    For a = [1, 2, 3] and b = [2, 1, 3], the output should be
    solution(a, b) = true.

    We can obtain b from a by swapping 2 and 1 in b.

    For a = [1, 2, 2] and b = [2, 1, 1], the output should be
    solution(a, b) = false.

    Any swap of any two elements either in a or in b won't make a and b equal."""
# a= [1, 2, 2]
# b= [2, 2, 1]
# x=sum(a)-sum(b)
# print(x)

def solution(a, b):
    if a==b:
        return True
    ercount=0
    x=[]
    for index in range(len(a)):
        if a[index]!=b[index]:
            ercount+=1
            x.append([a[index],b[index]])
    if ercount<3 and x[0]==x[1][::-1]:
        return True
    
    return False
print(solution([832, 998, 148, 570, 533, 561, 894, 147, 455, 279],
[832, 570, 148, 998, 533, 561, 455, 147, 894, 279]))



# def solution(a, b):
#     element = sorted(a) == sorted(b) 
#     diff = sum([i != j for i,j in zip(a,b)]) <3 
#     return element and diff  
# print(solution([832, 998, 148, 570, 533, 561, 894, 147, 455, 279],
# [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]))

"""17.You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
solution(inputArray) = 3.
Example

For inputArray = [1, 1, 1], the output should be
solution(inputArray) = 3."""
def solution(inputArray):
    lst=0
    for i in range(len(inputArray)-1):
        if inputArray[i]>= inputArray[i+1]:
            lst+= (inputArray[i]+1 - inputArray[i+1])
            inputArray[i+1] = inputArray[i]+1
        else:
            inputArray[i]
    
    return lst
print(solution([1, 1, 1])) 

"""18.Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
Example

For inputString = "aabb", the output should be
solution(inputString) = true."""

# def solution(inputString):
#     for i in range(0,int(len(inputString)/2)):
#             if inputString[i]==inputString[len(inputString)-1-i]:  
#                 return False
#             else:
#                 return True
# print(solution("aabb"))
def solution(inputString):
    s = set()
    for i in inputString:
        if i in s:
            s.remove(i)
        else:
            s.add(i)
    
    return len(s) <= 1
print(solution("aabb"))

"""19.Call two arms equally strong if the heaviest weights 
they each are able to lift are equal.

Call two people equally strong if their strongest 
arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' 
lifting capabilities find out if you two are equally strong.
Example

    For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, the output should be
    solution(yourLeft, yourRight, friendsLeft, friendsRight) = true;
    For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 10, the output should be
    solution(yourLeft, yourRight, friendsLeft, friendsRight) = true;
    For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 9, the output should be
    solution(yourLeft, yourRight, friendsLeft, friendsRight) = false"""

def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    # if yourLeft==friendsLeft and yourRight== friendsRight:
    #     return True
    # return False   
    return {yourLeft, yourRight} == {friendsLeft, friendsRight}
print(solution(15,10,15,10)) 


"""20.Given an array of integers, find the maximal absolute difference 
between any two of its adjacent elements.
Example

For inputArray = [2, 4, 1, 0], the output should be
solution(inputArray) = 3"""

#     def solution(inputArray):
        # a=0
        # for i in range(len(inputArray)-1):
        #     v=abs(inputArray[i+1]-inputArray[i])
        #     if a < v:
        #         a=v
        # return a




def solution(inputArray):

        max_diff = inputArray[1] - inputArray[0]
        dif =[]
        for i in range( 1, len(inputArray) ):      
                
                if (abs(inputArray[i-1] - inputArray[i]) > max_diff ):               
                    max_diff = abs(inputArray[i-1] - inputArray[i])
                    dif.append(max_diff)
                    print(max_diff)
        return max_diff
    
print(solution([2, 4, 1, 0]))


"""21."An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

    For inputString = "172.16.254.1", the output should be
    solution(inputString) = true;

    For inputString = "172.316.254.1", the output should be
    solution(inputString) = false.

    316 is not in range [0, 255].

    For inputString = ".254.255.0", the output should be
    solution(inputString) = false.

    There is no first number."""
# def solution(inputString):
#     x = inputString.split(" . ")
#     for i in range(len(inputString)):
        
#         if  len(x) == 4 and i > 0 and i > 255:
#             return True
#         else:
#             return False
        
def solution(inputString):
    splt = inputString.split('.')
    return len(splt) == 4 and all(i.isdigit() and 0 <= int(i) <= 255 for i in splt)
# def solution(inputString):
#     a=inputString.split('.')
#     try:
#         for i in a:
#             if len(a)!=4:
#                 return False
#             else:
#                 if i == None:
#                     return False
#                 else:
#                     b=float(i)
#                     if b>255.0 or b<0.0:
#                         return False
#     except ValueError:
#         return False
#     return True

print(solution("172.16.254.1"))
print(solution("0.254.255.0"))