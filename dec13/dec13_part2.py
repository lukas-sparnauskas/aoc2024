# https://adventofcode.com/2024/day/13

import numpy as np

file_path = 'input.txt'

machines = []

# Read the input file
with open(file_path, 'r') as file:
    lines = file.readlines()
    length = len(lines)
    i = 0
    while i < length:
        buttonA = (int(lines[i][lines[i].index('X+') + 2:].split(',')[0]), int(lines[i][lines[i].index('Y+') + 2:].split('\n')[0]))
        buttonB = (int(lines[i + 1][lines[i + 1].index('X+') + 2:].split(',')[0]), int(lines[i + 1][lines[i + 1].index('Y+') + 2:].split('\n')[0]))
        prize = (10000000000000 + int(lines[i + 2][lines[i + 2].index('X=') + 2:].split(',')[0]), 10000000000000 + int(lines[i + 2][lines[i + 2].index('Y=') + 2:].split('\n')[0]))
        machines.append((buttonA, buttonB, prize))
        i += 4

# Solve
machine_index = 0
prices = dict()

for machine_index in range(len(machines)):
    buttonA, buttonB, prize = machines[machine_index]
    # xA + xB = prize | with A being the buttonA value and B being the buttonB value and x and y being the number of times the buttons are pressed
    # Solve a linear equation with matrices AX = B
    # [ buttonA[0] buttonB[0] ]   [ X ]   [ prize[0] ]
    # |                       | X |   | = |          |
    # [ buttonA[1] buttonB[1] ]   [ Y ]   [ prize[1] ]

    a = np.array([[buttonA[0], buttonB[0]], [buttonA[1], buttonB[1]]])
    b = np.array([prize[0], prize[1]])
    x = np.linalg.solve(a, b)

    # Round to 4 decimal digits to avoid int(0.99999) -> 0 when it should be 1
    if not int(round(x[0], 4)) * buttonA[0] + int(round(x[1], 4)) * buttonB[0] == prize[0] or not int(round(x[0], 4)) * buttonA[1] + int(round(x[1], 4)) * buttonB[1] == prize[1]:
        continue

    prices[machine_index] = 3 * x[0] + x[1]

print(int(sum(prices.values())))
