# https://adventofcode.com/2024/day/3

file_path = 'input.txt'

data = []

# Read the input file
with open(file_path, 'r') as file:
    for line in file:
        data.append(line)

# Solve
total_sum = 0
do = True

for row in data:

    for i in range(len(row)):
        if not row[i].isdigit() and row[i] not in [*'don\'tmul(),',]:
            continue
        
        if row[i] == 'd':
            if row[i:i+7] == 'don\'t()':
                do = False
                continue
            if row[i:i+4] == 'do()':
                do = True
                continue
        
        if row[i:i+4] == 'mul(' and do:
            command = row[i:i+12] # 12 is the max length of the command
        
            x, y = '', ''
            corrupted = False
            for i in range(4, len(command)):
                if not command[i].isdigit() and command[i] not in [',', ')']:
                    corrupted = True
                    break
                if command[i] == ',':
                    x = command[4:i]
                if command[i] == ')':
                    y = command[command.index(',')+1:i]
                    break
        
            if corrupted or not x.isnumeric() or not y.isnumeric(): continue  
            total_sum += int(x) * int(y)
                
print(total_sum)