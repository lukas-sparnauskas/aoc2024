# https://adventofcode.com/2024/day/6

from copy import deepcopy

file_path = 'input.txt'

original_data = []

# Read the input file
with open(file_path, 'r') as file:
    for line in file:
        original_data.append([*line.replace('\n', ''),])

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

def run_board(data, return_visited=False):
    
    def check_guard_trapped(pos):
        if pos[0] < 0 or pos[0] >= len(data) or pos[1] < 0 or pos[1] >= len(data[0]):
            return True
        return False
    
    # Find the guard
    guard = (0, 0)
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '^':
                guard = (i, j)
                break

    is_trapped = False
    visited = set()
    visited_obs = set()
    direction = '^'
    while not is_trapped:
        
        current_pos = guard
        
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
                
        # Check if the guard is trapped
        if check_guard_trapped(guard):
            data[current_pos[0]][current_pos[1]] = 'X'
            visited.add(current_pos)
            is_trapped = True
            break
                
        # Detect collision
        if data[guard[0]][guard[1]] == '#':
            guard = current_pos

            if (guard[0], guard[1], direction) in visited_obs:
                # Infinite loop
                return True
            visited_obs.add((guard[0], guard[1], direction))
                
            direction = get_next_direction(direction)
        else:    
            data[current_pos[0]][current_pos[1]] = 'X'
            visited.add(current_pos)
            
        data[guard[0]][guard[1]] = direction

    if return_visited:
        return visited
    
    # No infinite loop
    return False

obs = 0
curr_check = 0
data = deepcopy(original_data)

# Get all visited points and only try to replace them, as other ones are never reached
all_visited = run_board(data, True)
total_checks = len(all_visited)
for i, j in all_visited:
    curr_check += 1
    print(f'Checking {curr_check}/{total_checks} ({curr_check/total_checks*100:.2f}%)')
    data = deepcopy(original_data)
    if data[i][j] == '#' or data[i][j] == '^':
        continue
    else:
        data[i][j] = '#'
        if run_board(data):
            obs += 1
                
print(obs)