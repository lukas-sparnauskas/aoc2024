# https://adventofcode.com/2024/day/11

file_path = 'input.txt'

data = []

# Read the input file
with open(file_path, 'r') as file:
    line = file.readline()
    data = [int(x) for x in line.replace('\n', '').split()]

# Solve
blinks = 75

size_map = dict()

num_stones = 0
def get_length(curr_blink, stone):
    if curr_blink == blinks:
        return 1
    
    if (curr_blink, stone) in size_map:
        return size_map[(curr_blink, stone)]
    
    if stone == 0:
        length = get_length(curr_blink + 1, 1)
        size_map[(curr_blink, stone)] = length
        return length
    
    if len(str(stone)) % 2 == 0:
        num1 = int(str(stone)[:len(str(stone)) // 2])
        num2 = int(str(stone)[len(str(stone)) // 2:])
        length = get_length(curr_blink + 1, num1) + get_length(curr_blink + 1, num2)
        size_map[(curr_blink, stone)] = length
        return length
    
    length = get_length(curr_blink + 1, stone * 2024)
    size_map[(curr_blink, stone)] = length
    return length

for stone in data:
    num_stones += get_length(0, stone)
        
print(num_stones)