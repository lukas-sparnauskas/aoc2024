# https://adventofcode.com/2024/day/14

import numpy as np

from copy import deepcopy

file_path = 'input.txt'

original_robots = []
width = 101
height = 103

# Read the input file
with open(file_path, 'r') as file:
    for line in file:
        p = line[line.index('p=') + 2:line.index('v=')].split(',')
        p = (int(p[0]), int(p[1]))
        v = line[line.index('v=') + 2:].split(',')
        v = (int(v[0]), int(v[1]))
        original_robots.append((p, v))

# Solve
seconds = 10000

def move(point, mvmnt):
    point = (point[0] + mvmnt[0], point[1] + mvmnt[1])
    if point[0] > width - 1:
        point = (point[0] - width, point[1])
    elif point[0] < 0:
        point = (width + point[0], point[1])
    if point[1] > height - 1:
        point = (point[0], point[1] - height)
    elif point[1] < 0:
        point = (point[0], height + point[1])
    return point

def get_board(robot_positions):
    board = str()
    for j in range(height):
        row = ['X' if (i, j) in robot_positions else '.' for i in range(width)]
        board += ''.join(row) + '\n'
    return board

# Move robots and calculate variance for each iteration
robots = deepcopy(original_robots)
variances = []
print('1st run - calculating variance')
for second in range(1, seconds + 1):
    for i in range(len(robots)):
        point = robots[i][0]
        mvmnt = robots[i][1]
        robots[i] = (move(point, mvmnt), mvmnt)
    
    robot_positions = [point for point, _ in robots]
    variances.append(np.var(robot_positions))

# Find lowest variance
min_var = min(variances)
print('Average variance', np.average(variances))
print('Minimum variance', min_var)

# Move robots again and only print the iteration with lowest variance
robots = deepcopy(original_robots)
print('2nd run - searching for lowest variance')
for second in range(1, seconds + 1):
    for i in range(len(robots)):
        point = robots[i][0]
        mvmnt = robots[i][1]
        robots[i] = (move(point, mvmnt), mvmnt)
    
    robot_positions = [point for point, _ in robots]
    if np.var(robot_positions) == min_var:
        board = get_board(robot_positions)
        print(board)
        print(f'second={second} var={np.var(robot_positions)}')