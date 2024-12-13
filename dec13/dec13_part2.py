# https://adventofcode.com/2024/day/13

import numpy as np

file_path = 'input1.txt'

machines = []

# Read the input file
with open(file_path, 'r') as file:
    lines = file.readlines()
    length = len(lines)
    i = 0
    while i < length:
        buttonA = (int(lines[i][lines[i].index('X+') + 2:].split(',')[0]), int(lines[i][lines[i].index('Y+') + 2:].split('\n')[0]))
        buttonB = (int(lines[i + 1][lines[i + 1].index('X+') + 2:].split(',')[0]), int(lines[i + 1][lines[i + 1].index('Y+') + 2:].split('\n')[0]))
        #prize = (int(lines[i + 2][lines[i + 2].index('X=') + 2:].split(',')[0]), int(lines[i + 2][lines[i + 2].index('Y=') + 2:].split('\n')[0]))
        prize = (10000000000000 + int(lines[i + 2][lines[i + 2].index('X=') + 2:].split(',')[0]), 10000000000000 + int(lines[i + 2][lines[i + 2].index('Y=') + 2:].split('\n')[0]))
        machines.append((buttonA, buttonB, prize))
        i += 4

# Solve
machine_index = 0
multipliers = dict()

# Calculate possible multipliers for each machine
for machine_index in range(len(machines)):
    print(f'Processing machine {machine_index}')
    buttonA, buttonB, prize = machines[machine_index]
    # xA + yB = prize | with A being the buttonA value and B being the buttonB value and x and y being the number of times the buttons are pressed
    # x = (prize - yB) / A
    # y = (prize - xA) / B
    x_range = np.arange(0, max(prize[0] // buttonA[0], prize[1] // buttonB[1], prize[0] // buttonB[0], prize[1] // buttonA[1]))
    x_range = (prize[0] - x_range * buttonB[0]) / buttonA[0]
    x_range = x_range[[index for index, x in enumerate(x_range) if x.is_integer() and x >= 0]]
    for x in x_range:
        y = (prize[1] - x * buttonA[1]) / buttonB[1]
        if not x * buttonA[0] + y * buttonB[0] == prize[0] or not x * buttonA[1] + y * buttonB[1] == prize[1]:
            continue
        
        if y.is_integer() and y >= 0 and machine_index not in multipliers:
            multipliers[machine_index] = [(int(x), int(y))]
        elif y.is_integer() and y >= 0:
            multipliers[machine_index].append((int(x), int(y)))

print(multipliers)

num_tokens = 0 
# Find the cheapest combinations
for machine_index in multipliers.keys():
    min_cost = -1
    for x, y in multipliers[machine_index]:
        if min_cost == -1 or 3 * x + y < min_cost:
            min_cost = 3 * x + y
    num_tokens += min_cost
    
print(num_tokens)