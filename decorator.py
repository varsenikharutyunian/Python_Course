# 1
def decorator1(func):
    def inner():
        print("start")
        result=func()
        print("end")
        return result
    return inner
@decorator1

def new_func():
    return 1

x=new_func()
print(("x = "), x)

# 2
def decorator1(func):
    def inner(*args, **kwargs):
        # print("start")
        result=func(*args, **kwargs)
        # print("end")
        return result
    return inner
@decorator1

def new_func(a,b,c):
    return a+b+c

x=new_func(3,5,6)
print(("x = "), x)


"""3."""

# from time import sleep,time



# def some_delay():
#     start=time()
#     sleep(3)
#     print("Hello")
#     end=time()
#     print(end-start)
# some_delay()

"""3. decoratot in time"""

from time import sleep,time



def running_time(func):
    def inner():
        start = time()
        result=func()
        end = time()
        print(end-start)
        return result
    return inner
@running_time
def some_delay():
    sleep(3)
    print("Hello")
# some_delay=running_time(some_delay)
some_delay()
@running_time
def some_delay2():
    sleep(1)
    print("Hello")
    return 5
x=some_delay2()
print(("x="),x)


"""4. decorator in type"""
def running_time(func):
    def inner(*args, **kwargs):
        
        result=func(*args,**kwargs)
        
        print(type(result))
        return result
    return inner
        
@running_time
def some_delay():
    sleep(3)
    print("Hello")
some_delay()
@running_time
def some_delay2():
    sleep(1)
    print("Hello")
    return 5
x=some_delay2()
print(("x="),x)


