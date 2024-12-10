# https://adventofcode.com/2024/day/2

import numpy as np

file_path = 'input.txt'

data = []

# Read the input file
with open(file_path, 'r') as file:
    for line in file:
        values = line.split()
        data.append(np.array(values, dtype=int))

# Solve
num_safe = 0

for i in range(len(data)):
    
    for removed_index in range(len(data[i])):
        
        is_increasing, is_decreasing, is_change_more_than_3, is_same = False, False, False, False

        array = np.delete(data[i], removed_index)
    
        for j in range(1, len(array)):
            if not is_increasing and array[j] > array[j-1]:
                is_increasing = True
            if not is_decreasing and array[j] < array[j-1]:
                is_decreasing = True
            if array[j] == array[j-1]:
                is_same = True
                break
            if abs(array[j] - array[j-1]) > 3:
                is_change_more_than_3 = True
                break
            
        if is_same or is_change_more_than_3 or (is_increasing and is_decreasing) or (not is_increasing and not is_decreasing):
            continue
        
        num_safe += 1
        break
        
print(num_safe)