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

            antinodes.add(point_1)
            antinodes.add(point_2)

            dist_row = point_2[0] - point_1[0]
            dist_col = point_2[1] - point_1[1]

            is_1_in_bounds = True
            is_2_in_bounds = True
            while is_1_in_bounds or is_2_in_bounds:
                antinode_1 = (point_1[0] - dist_row, point_1[1] - dist_col)
                antinode_2 = (point_2[0] + dist_row, point_2[1] + dist_col)
                
                if antinode_1 != point_1 and antinode_1 != point_2 and 0 <= antinode_1[0] <= max_row and 0 <= antinode_1[1] <= max_col:
                    antinodes.add(antinode_1)
                elif not (0 <= antinode_1[0] <= max_row) or not (0 <= antinode_1[1] <= max_col):
                    is_1_in_bounds = False

                if antinode_2 != point_1 and antinode_2 != point_2 and 0 <= antinode_2[0] <= max_row and 0 <= antinode_2[1] <= max_col:
                    antinodes.add(antinode_2)
                elif not (0 <= antinode_2[0] <= max_row) or not (0 <= antinode_2[1] <= max_col):
                    is_2_in_bounds = False

                point_1 = antinode_1
                point_2 = antinode_2
            
print(len(antinodes))