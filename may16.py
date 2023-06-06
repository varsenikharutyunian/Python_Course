def solution(a):
    b = sorted([i for i in a if i!=-1])
    j = 0
    for i in range(len(a)):
        if a[i] == -1:
            pass
        else:
            a[i]=b[j]
            j+=1
    return a
    
        
        
print(solution([-1, 150, 190, 170, -1, -1, 160, 180]))          



def solution(inputString):
    if len(inputString)==0
    return inputString
while "(" in inputString:
    index1= inputString.index("(")
    index2= inputString.index(")")
substring=inputString[index1:index1+index2+1][1:-1][::-1]]
inputString=inputString[:index1]+substring+inputString[index1+index2+1:]
return inputString
    
    