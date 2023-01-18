# Description: A timer decorator function is used to time how long it takes functions to run

import time

def my_timer(func):
    def inner():
        start=time.time()
        func()
        end=time.time()
        print("Inside decorator:",func.__name__,"ran in:",end-start,"sec")
        return
    return inner

@my_timer
def func1():
   time.sleep(1); # delay of 1 second
   print('func1 is executing!')   

@my_timer
def func2():
   time.sleep(2); # delay of 2 seconds
   print('func2 is executing!')   

def test_timer () :
   print("Output: my_time()")
   func1()
   func2()
   '''
   Output: my_timer()
   func1 is executing!
   Inside decorator: func1 ran in: 1.000206708908081 sec
   func2 is executing!
   Inside decorator: func2 ran in: 2.00041127204895 sec   
    '''
test_timer()