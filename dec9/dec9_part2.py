# https://adventofcode.com/2024/day/9

file_path = 'input.txt'

data = []

# Read the input file
with open(file_path, 'r') as file:
    line = file.readline()
    data = [int(x) for x in [*line.replace('\n', ''),]]

# Solve
id = 0
disk = []
is_file = True

# Create the disk array
for i in data:
    if is_file:
        for _ in range(i): disk.append(id)
        is_file = False
        id += 1
    else:
        for _ in range(i): disk.append('.')
        is_file = True

# Defrag
defragged_ids = set()

def find_next_free_space(size, max_id, disk):
    for i in range(max_id + 1):
        if disk[i] == '.' and size == 1:
                return i
        elif disk[i] == '.' and size > 1:
            curr_size = 0
            for j in range(i, max_id + 1):
                if disk[j] == '.':
                    curr_size += 1
                    if curr_size == size:
                        return i
                else:
                    break
    return -1

def find_next_file(start_id, disk, defragged_ids):
    for i in reversed(range(start_id + 1)):
        if disk[i] != '.' and disk[i] not in defragged_ids:
            size = 0
            for j in reversed(range(i + 1)):
                if disk[j] == disk[i]:
                    size += 1
                else:
                    break
            return (i, size, disk[i])
    return (-1, -1, -1)

current_file = find_next_file(len(disk) - 1, disk, defragged_ids) # Tuple: (id, size, file_id)

# While there are file ids to check
while current_file[2] >= 0:
    currect_free_space_id = find_next_free_space(current_file[1], current_file[0] - current_file[1], disk)
    
    # If there is no free space for current file, find the next file and calculate free space
    if currect_free_space_id == -1:
        current_file = find_next_file(current_file[0] - current_file[1], disk, defragged_ids)
        continue
    
    for _ in range(current_file[1]):
        disk[currect_free_space_id] = disk[current_file[0]]
        disk[current_file[0]] = '.'
        currect_free_space_id += 1
        current_file = (current_file[0] - 1, current_file[1], current_file[2])
        
    defragged_ids.add(current_file[2])
    current_file = find_next_file(current_file[0], disk, defragged_ids)
    
# Calculate checksum
checksum = 0

for i in range(len(disk)):
    if disk[i] == '.':
        continue
    checksum += i * disk[i]

print(checksum)