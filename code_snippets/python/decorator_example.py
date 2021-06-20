import time 
def time_func(func):
    def wrapper():
        print("This happens before the function is called")
        start = time.time()
        func()
        print('This happens after the funciton is called')
        end = time.time()
        print('The duration is', end - start, 's')

    return wrapper

@time_func
def say_hello():
    print("hello")

say_hello()
""" 
This happens before the function is called
hello
This happens after the funciton is called
The duration is 4.0531158447265625e-06 s
"""