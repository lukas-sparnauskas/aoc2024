# https://adventofcode.com/2024/day/6

file_path = 'input.txt'

data = []

# Read the input file
with open(file_path, 'r') as file:
    for line in file:
        data.append([*line.replace('\n', ''),])

# Solve
def get_next_direction(direction):
    match direction:
        case '^':
            return '>'
        case 'v':
            return '<'
        case '<':
            return '^'
        case '>':
            return 'v'

# Find the guard
guard = (0, 0)
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '^':
            guard = (i, j)
            break

is_trapped = False
visited = set()
direction = '^'
while not is_trapped:
    current_pos = guard
    
    # Check if the guard is trapped
    if guard[0] - 1 < 0 or guard[0] + 1 >= len(data) or guard[1] - 1 < 0 or guard[1] + 1 >= len(data[0]):
        data[current_pos[0]][current_pos[1]] = 'X'
        visited.add(current_pos)
        is_trapped = True
        break
    
    # Move
    match direction:
        case '^':
            guard = (guard[0] - 1, guard[1])
        case 'v':
            guard = (guard[0] + 1, guard[1])
        case '<':
            guard = (guard[0], guard[1] - 1)
        case '>':
            guard = (guard[0], guard[1] + 1)
            
    # Detect collision
    if data[guard[0]][guard[1]] == '#':
        guard = current_pos
        direction = get_next_direction(direction)
    else:    
        data[current_pos[0]][current_pos[1]] = 'X'
        visited.add(current_pos)
        
    data[guard[0]][guard[1]] = direction
        
print(len(visited))