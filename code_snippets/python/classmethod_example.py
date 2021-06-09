class Solver:
    def __init__(self, nums: list):
        self.nums = nums
    
    @classmethod
    def get_even(cls, nums: list):
        return cls([num for num in nums if num % 2 == 0])
    def print_output(self):
        print("Result:", self.nums)

# Not using class method       
nums = [1, 2, 3, 4, 5, 6, 7]
solver = Solver(nums).print_output()
"""
Result: [1, 2, 3, 4, 5, 6, 7]
"""

solver2 = Solver.get_even(nums)
solver2.print_output()
"""
Result: [2, 4, 6]
"""
