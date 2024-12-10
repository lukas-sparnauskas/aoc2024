# https://adventofcode.com/2024/day/1

import numpy as np

file_path = 'input.txt'

column1 = []
column2 = []

# Read the input file
with open(file_path, 'r') as file:
    for line in file:
        values = line.split()
        column1.append(int(values[0]))
        column2.append(int(values[1]))

# Solve
column1 = np.sort(column1)
column2 = np.sort(column2)

result = np.sum(np.abs(column2 - column1))

print(result)