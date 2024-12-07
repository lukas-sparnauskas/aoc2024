# https://adventofcode.com/2024/day/4

file_path = 'input.txt'

data = []

# Read the input file
with open(file_path, 'r') as file:
    for line in file:
        data.append(line)

# Solve
xmas_count = 0

# Horizontal check
for i in range(len(data[0]) - 3):
    for j in range(len(data)):
        if data[j][i] == 'X' and data[j][i+1] == 'M' and data[j][i+2] == 'A' and data[j][i+3] == 'S':
            xmas_count += 1
        if data[j][i] == 'S' and data[j][i+1] == 'A' and data[j][i+2] == 'M' and data[j][i+3] == 'X':
            xmas_count += 1
            
# Vertical check
for i in range(len(data[0])):
    for j in range(len(data) - 3):
        if data[j][i] == 'X' and data[j+1][i] == 'M' and data[j+2][i] == 'A' and data[j+3][i] == 'S':
            xmas_count += 1
        if data[j][i] == 'S' and data[j+1][i] == 'A' and data[j+2][i] == 'M' and data[j+3][i] == 'X':
            xmas_count += 1
            
# Diagonal check
for i in range(len(data) - 3):
    for j in range(len(data[0]) - 3):
        if data[i][j] == 'X' and data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and data[i+3][j+3] == 'S':
            xmas_count += 1
        if data[i][j+3] == 'X' and data[i+1][j+2] == 'M' and data[i+2][j+1] == 'A' and data[i+3][j] == 'S':
            xmas_count += 1
        if data[i][j] == 'S' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'M' and data[i+3][j+3] == 'X':
            xmas_count += 1
        if data[i][j+3] == 'S' and data[i+1][j+2] == 'A' and data[i+2][j+1] == 'M' and data[i+3][j] == 'X':
            xmas_count += 1
            
print(xmas_count)