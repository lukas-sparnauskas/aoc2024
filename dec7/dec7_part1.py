import numpy as np

file_name = 'input.txt'

data = []

with open(file_name, 'r') as file:
    for line in file:
        parts = line.split(':')
        data.append((int(parts[0]), [int(x) for x in parts[1].split()]))

res_sum = 0

for res, nums in data:
    for op in range(pow(2, len(nums) - 1)):
        ops = np.binary_repr(op, width=len(nums) - 1)
        temp_res = nums[0]
        for i in range(1, len(nums)):
            if ops[i - 1] == '0':
                temp_res += nums[i]
            else:
                temp_res *= nums[i]
        if temp_res == res:
            res_sum += res
            break

print(res_sum)