# https://adventofcode.com/2024/day/13

file_path = 'input.txt'

machines = []

# Read the input file
with open(file_path, 'r') as file:
    lines = file.readlines()
    length = len(lines)
    i = 0
    while i < length:
        buttonA = (int(lines[i][lines[i].index('X+') + 2:].split(',')[0]), int(lines[i][lines[i].index('Y+') + 2:].split('\n')[0]))
        buttonB = (int(lines[i + 1][lines[i + 1].index('X+') + 2:].split(',')[0]), int(lines[i + 1][lines[i + 1].index('Y+') + 2:].split('\n')[0]))
        prize = (int(lines[i + 2][lines[i + 2].index('X=') + 2:].split(',')[0]), int(lines[i + 2][lines[i + 2].index('Y=') + 2:].split('\n')[0]))
        machines.append((buttonA, buttonB, prize))
        i += 4

# Solve
machine_index = 0
prices = dict()

for machine_index in range(len(machines)):
    buttonA, buttonB, prize = machines[machine_index]
    # xA + yB = prize | with A being the buttonA value and B being the buttonB value and x and y being the number of times the buttons are pressed
    # x = (prize - yB) / A
    # y = (prize - xA) / B
    for i in range(101):
        x = (prize[0] - i * buttonB[0]) / buttonA[0]
        if not x.is_integer() or x < 0:
            continue
        
        y = (prize[1] - x * buttonA[1]) / buttonB[1]
        if not x * buttonA[0] + y * buttonB[0] == prize[0] or not x * buttonA[1] + y * buttonB[1] == prize[1]:
            continue
        
        if y.is_integer() and y >= 0 and machine_index not in prices:
            prices[machine_index] = [3 * int(x) + int(y)]
        elif y.is_integer() and y >= 0:
            prices[machine_index].append(3 * int(x) + int(y))

num_tokens = 0
# Find the cheapest prices
for machine_index in prices.keys():
    num_tokens += min(prices[machine_index])
    
print(num_tokens)