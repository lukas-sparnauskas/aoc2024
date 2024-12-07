# https://adventofcode.com/2024/day/4

file_path = 'input.txt'

data = []

# Read the input file
with open(file_path, 'r') as file:
    for line in file:
        data.append(line.replace('\n', ''))

# Solve
xmas_count = 0

for i in range(len(data) - 2):
    for j in range(len(data[0]) - 2):
        if data[i][j] == 'M' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'S' and data[i+2][j] == 'M' and data[i][j+2] == 'S':
            xmas_count += 1
        if data[i][j] == 'S' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'M' and data[i+2][j] == 'S' and data[i][j+2] == 'M':
            xmas_count += 1
            
        if data[i][j] == 'M' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'S' and data[i][j+2] == 'M' and data[i+2][j] == 'S':
            xmas_count += 1
        if data[i][j] == 'S' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'M' and data[i][j+2] == 'S' and data[i+2][j] == 'M':
            xmas_count += 1
  
print(xmas_count)