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
def check(num, u):
    intersection = np.intersect1d(instructions[num], u)
    if num in instructions and len(intersection) > 0:
        return intersection
    return []

def fix_update(u):
    # Fix the update by swapping the numbers in the update
    current_update = []
    for i, num in enumerate(u):
        intersection = check(num, current_update)
        if len(intersection) > 0:
            temp = u[i]
            u[i] = intersection[0]
            u[list(u).index(intersection[0])] = temp
        current_update.append(u[i])
    
    # Check if the update is correct, if not, fix it again
    current_update = []
    for num in u:
        intersection = check(num, current_update)
        if len(intersection) > 0:
            # Fix again if still incorrect
            u = fix_update(u)
            break
        current_update.append(num)
    
    return u

# Find the incorrect updates
incorrect_updates = []
for u in updates:
    current_update = []
    for num in u:
        intersection = check(num, current_update)
        if len(intersection) > 0:
            incorrect_updates.append(u)
            break
        current_update.append(num)

middle_numbers = []
for u in incorrect_updates:
    u = fix_update(u)
    middle_numbers.append(u[len(u) // 2])

print(sum(middle_numbers))