from functools import reduce

nums = [val for val in range(100, 1001) if val % 2 == 0]
sum_all = reduce(lambda x, y: x * y, nums)

print(sum_all)
