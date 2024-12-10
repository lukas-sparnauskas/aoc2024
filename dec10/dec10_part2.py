# https://adventofcode.com/2024/day/10

file_path = 'input.txt'

data = []

# Read the input file
with open(file_path, 'r') as file:
    for line in file:
        data.append([int(x) if x != '.' else -1 for x in [*line.replace('\n', ''),]])

# Solve
zeros = [(i, j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == 0]
trailheads = dict()

def check_direction(i, j, direction):
    match direction:
        case 'up':
            if 0 <= i - 1 <= len(data) - 1 and data[i][j] + 1 == data[i - 1][j]:
                return True
        case 'down':
            if 0 <= i + 1 <= len(data) - 1 and data[i][j] + 1 == data[i + 1][j]:
                return True
        case 'left':
            if 0 <= j - 1 <= len(data[0]) - 1 and data[i][j] + 1 == data[i][j - 1]:
                return True
        case 'right':
            if 0 <= j + 1 <= len(data[0]) - 1 and data[i][j] + 1 == data[i][j + 1]:
                return True
    return False

def check_trail(trail, current_point):
    i = current_point[0]
    j = current_point[1]

    if data[i][j] == 9:
        if trail[0] in trailheads:
            trailheads[trail[0]].append(trail)
        else:
            trailheads[trail[0]] = [trail]
        return

    if check_direction(i, j, 'up'):
        check_trail([*trail, (i, j)], (i - 1, j))
    if check_direction(i, j, 'down'):
        check_trail([*trail, (i, j)], (i + 1, j))
    if check_direction(i, j, 'left'):
        check_trail([*trail, (i, j)], (i, j - 1))
    if check_direction(i, j, 'right'):
        check_trail([*trail, (i, j)], (i, j + 1))

# Check each 0 if it is a valid trailhead
for th in zeros:
    check_trail([th], th)

print(sum([len(trailheads[point]) for point in trailheads]))