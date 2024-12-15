# https://adventofcode.com/2024/day/14

file_path = 'input.txt'

robots = []
width = 101
height = 103

# Read the input file
with open(file_path, 'r') as file:
    for line in file:
        p = line[line.index('p=') + 2:line.index('v=')].split(',')
        p = (int(p[0]), int(p[1]))
        v = line[line.index('v=') + 2:].split(',')
        v = (int(v[0]), int(v[1]))
        robots.append((p, v))

# Solve
seconds = 100

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

# Move robots   
for second in range(1, seconds + 1):
    for i in range(len(robots)):
        point = robots[i][0]
        mvmnt = robots[i][1]
        robots[i] = (move(point, mvmnt), mvmnt)

# Calculate how many robots in each quadrant
ignore_col = width // 2
ignore_row = height // 2
nw_quad = [1 for point, _ in robots if point[0] < ignore_col and point[1] < ignore_row]
sw_quad = [1 for point, _ in robots if point[0] < ignore_col and point[1] > ignore_row]
ne_quad = [1 for point, _ in robots if point[0] > ignore_col and point[1] < ignore_row]
se_quad = [1 for point, _ in robots if point[0] > ignore_col and point[1] > ignore_row]

safety_factor = sum(nw_quad) * sum(sw_quad) * sum(ne_quad) * sum(se_quad)

print(safety_factor)