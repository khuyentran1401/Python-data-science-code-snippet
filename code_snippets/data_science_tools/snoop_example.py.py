# pip install snoop
import snoop 

@snoop
def factorial(x: int):
    if x == 1:
        return 1
    else: 
        return (x * factorial(x-1))

if __name__ == '__main__':
    num = 2
    print(f'The factorial of {num} is {factorial(num)}')
