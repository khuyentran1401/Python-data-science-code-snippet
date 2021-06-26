from decorator import decorator
from time import time, sleep

def time_func(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        end_time = time()
        print(
            f"""It takes {round(end_time - start_time, 3)} seconds to execute the function"""
        )
    return wrapper 

@decorator
def time_func_with_decorator(func, *args, **kwargs):
    start_time = time()
    func(*args, **kwargs)
    end_time = time()
    print(
            f"""It takes {round(end_time - start_time, 3)} seconds to execute the function"""
        )
@time_func_with_decorator  
def test_func():
    sleep(1)
    
if __name__== '__main__':
    test_func()
