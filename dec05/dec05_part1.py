# https://adventofcode.com/2024/day/5

import numpy as np

file_path = 'input.txt'

instructions = dict()
updates = []
read_instructions = True

# Read the input file
with open(file_path, 'r') as file:
    for line in file:
        if read_instructions:
            if line == '\n':
                read_instructions = False
                continue
            inst = line.split('|')
            num1 = int(inst[0].replace('\n',  ''))
            num2 = int(inst[1])
            if num1 in instructions:
                instructions[num1].append(num2)
            else:
                instructions[num1] = [num2]
        else:
            updates.append(np.array(line.replace('\n',  '').split(','), dtype=int))

# Solve
middle_numbers = []

for u in updates:
    is_correct = True
    current_update = []
    for num in u:
        if num in instructions and len(np.intersect1d(instructions[num], current_update)) > 0:
            is_correct = False
            break
        current_update.append(num)
    if is_correct:
        middle_numbers.append(u[len(u) // 2])
        
print(sum(middle_numbers))