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
def find_next_free_space(start_id, disk):
    for i in range(start_id, len(disk)):
        if disk[i] == '.':
            return i
    return -1

def find_next_file(start_id, disk):
    for i in reversed(range(start_id + 1)):
        if disk[i] != '.':
            return i
    return -1

currect_free_space_id = find_next_free_space(0, disk)
current_file_id = find_next_file(len(disk) - 1, disk)

while currect_free_space_id < current_file_id:
    disk[currect_free_space_id] = disk[current_file_id]
    disk[current_file_id] = '.'
    currect_free_space_id = find_next_free_space(currect_free_space_id, disk)
    current_file_id = find_next_file(current_file_id, disk)
    
# Calculate checksum
checksum = 0

for i in range(len(disk)):
    if disk[i] == '.':
        break
    checksum += i * disk[i]

print(checksum)