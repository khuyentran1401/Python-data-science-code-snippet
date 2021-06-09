def division(num1: int, num2: int):
    assert num2 != 0, "“num2 must be different from 0"
    return num1 / num2


division(2, 0)
""" 
AssertionError: “num2 must be different from 0
"""