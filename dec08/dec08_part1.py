# https://adventofcode.com/2024/day/8

file_name = 'input.txt'

data = []

# Read the input file
with open(file_name, 'r') as file:
    for line in file:
        data.append([*line.replace('\n', ''),])

# Solve
points = set()
antenna_map = dict()
antinodes = set()
max_col = len(data[0]) - 1
max_row = len(data) - 1

# Create a coordinate map
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '.':
            continue
        points.add((i, j))
        if data[i][j] in antenna_map:
            antenna_map[data[i][j]].append((i, j))
        else:
            antenna_map[data[i][j]] = [(i, j)]

# Calculate antinode coordinates
for antenna in antenna_map:
    antennas = antenna_map[antenna]
    if len(antennas) < 2:
        continue
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            point_1 = antennas[i]
            point_2 = antennas[j]
            dist_row = point_2[0] - point_1[0]
            dist_col = point_2[1] - point_1[1]
            antinode_1 = (point_1[0] - dist_row, point_1[1] - dist_col)
            antinode_2 = (point_2[0] + dist_row, point_2[1] + dist_col)
            for a in [antinode_1, antinode_2]:
                if a == point_1 or a == point_2:
                    continue
                if 0 <= a[0] <= max_row and 0 <= a[1] <= max_col:
                    antinodes.add(a)
            
print(len(antinodes))