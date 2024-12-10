# https://adventofcode.com/2024/day/1

file_path = 'input.txt'

column1 = []
column2 = []

# Read the input file
with open(file_path, 'r') as file:
    for line in file:
        values = line.split()
        column1.append(int(values[0]))
        column2.append(int(values[1]))

# Solve  
score = 0
column2_count = dict()

# Calculate how many times each number appears in the second list
for i in column2:
    if i in column2_count:
        column2_count[i] += 1
    else:
        column2_count[i] = 1

# Calculate the score
for i in range(len(column1)):
    score += column1[i] * column2_count.get(column1[i], 0)
    
print(score)