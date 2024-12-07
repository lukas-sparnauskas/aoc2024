# https://adventofcode.com/2024/day/7

import numpy as np

file_name = 'input.txt'

data = []

# Read the input file
with open(file_name, 'r') as file:
    for line in file:
        parts = line.split(':')
        data.append((int(parts[0]), [int(x) for x in parts[1].split()]))

# Solve
res_sum = 0

index = 0
for res, nums in data:
    index += 1
    print(f'Checking {index}/{len(data)} ({index/len(data)*100:.2f}%)')

    # Number of possible operation combinations = 3^(len(nums) - 1)
    for op in range(pow(3, len(nums) - 1)):

        # This time create a ternary string that describes what operation to use
        # 0 - addition
        # 1 - multiplication
        # 2 - concatenate
        ops = np.base_repr(op, base=3)
        ops = ('0' * (len(nums) - 1 - len(ops))) + ops
        temp_res = nums[0]

        for i in range(1, len(nums)):
            if ops[i - 1] == '0':
                temp_res += nums[i]
            elif ops[i - 1] == '1':
                temp_res *= nums[i]
            else:
                temp_res = int(str(temp_res) + str(nums[i]))

        if temp_res == res:
            res_sum += res
            break

print(res_sum)