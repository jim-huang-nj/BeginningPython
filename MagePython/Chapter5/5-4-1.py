from functools import reduce
nums = [6,9,4,2,4,10,5,9,6,9]
print(nums)
print(sum(nums))
print(reduce(lambda val,x:val + x, nums))