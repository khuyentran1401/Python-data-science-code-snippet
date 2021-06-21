def get_multiples_of_n(nums: list, n: int):
	"""Select only numbers whose remainders
	 are 0 when dividing them by n"""
	return [num for num in nums if num % n == 0]

nums = [1, 4, 9, 12, 15, 16]

print(get_multiples_of_n(nums, 2)) # multiples of 2
# [4, 12, 16]

print(get_multiples_of_n(nums, 3)) # multiples of 3
# [9, 12, 15]

print(get_multiples_of_n(nums, 4)) # multiples of 4
# [4, 12, 16]
