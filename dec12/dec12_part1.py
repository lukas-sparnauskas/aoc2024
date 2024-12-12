# https://adventofcode.com/2024/day/12

file_path = 'input.txt'

data = []

# Read the input file
with open(file_path, 'r') as file:
    for line in file:
        data.append([x for x in [*line.replace('\n', ''),]])

# Solve
regions = []

def get_point_region(region, i, j):
    # Check if region continues to the left
    if j > 0 and data[i][j - 1] == data[i][j] and (i, j - 1) not in region:
        region.add((i, j - 1))
        region = get_point_region(region, i, j - 1)
    # Check if region continues to the right
    if j < len(data[i]) - 1 and data[i][j + 1] == data[i][j] and (i, j + 1) not in region:
        region.add((i, j + 1))
        region = get_point_region(region, i, j + 1)
    # Check if region continues up
    if i > 0 and data[i - 1][j] == data[i][j] and (i - 1, j) not in region:
        region.add((i - 1, j))
        region = get_point_region(region, i - 1, j)
    # Check if region continues down
    if i < len(data) - 1 and data[i + 1][j] == data[i][j] and (i + 1, j) not in region:
        region.add((i + 1, j))
        region = get_point_region(region, i + 1, j)
    
    return region

def is_point_in_any_region(i, j):
    for region in regions:
        if (i, j) in region:
            return True
    return False

def get_region_perimeter(region):
    perimeter = 0
    for i, j in region:
        if i == 0 or (i - 1, j) not in region:
            perimeter += 1
        if i == len(data) - 1 or (i + 1, j) not in region:
            perimeter += 1
        if j == 0 or (i, j - 1) not in region:
            perimeter += 1
        if j == len(data[i]) - 1 or (i, j + 1) not in region:
            perimeter += 1
    return perimeter

# Get all regions
for i in range(len(data)):
    for j in range(len(data[i])):
        if not is_point_in_any_region(i, j):
            region = set()
            region.add((i, j))
            region = get_point_region(region, i, j)
            regions.append(region)

# Get price
price = 0
for region in regions:
    price += len(region) * get_region_perimeter(region)
            
print(price)
