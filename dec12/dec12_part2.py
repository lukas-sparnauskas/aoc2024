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
        region.append((i, j - 1))
        region = get_point_region(region, i, j - 1)
    # Check if region continues to the right
    if j < len(data[i]) - 1 and data[i][j + 1] == data[i][j] and (i, j + 1) not in region:
        region.append((i, j + 1))
        region = get_point_region(region, i, j + 1)
    # Check if region continues up
    if i > 0 and data[i - 1][j] == data[i][j] and (i - 1, j) not in region:
        region.append((i - 1, j))
        region = get_point_region(region, i - 1, j)
    # Check if region continues down
    if i < len(data) - 1 and data[i + 1][j] == data[i][j] and (i + 1, j) not in region:
        region.append((i + 1, j))
        region = get_point_region(region, i + 1, j)
    
    return region

def is_point_in_any_region(i, j):
    for region in regions:
        if (i, j) in region:
            return True
    return False

def get_region_border_points(region):
    border_points = set()
    for i, j in region:
        if i == 0 or (i - 1, j) not in region:
            border_points.add((i, j, 'top'))
        if i == len(data) - 1 or (i + 1, j) not in region:
            border_points.add((i, j, 'bottom'))
        if j == 0 or (i, j - 1) not in region:
            border_points.add((i, j, 'left'))
        if j == len(data[i]) - 1 or (i, j + 1) not in region:
            border_points.add((i, j, 'right'))
    return border_points

def get_region_number_of_sides(region):
    # Get all the border points of the region
    border_points = get_region_border_points(region)
    sides = 0
    for i, j, direction in border_points:
        match direction:
            case 'top':
                # Check if the point to the right also has a top border
                if (i, j + 1, 'top') not in border_points:
                    sides += 1
            case 'right':
                # Check if the point below also has a right border
                if (i + 1, j, 'right') not in border_points:
                    sides += 1
            case 'bottom':
                # Check if the point to the left also has a bottom border
                if (i, j - 1, 'bottom') not in border_points:
                    sides += 1
            case 'left':
                # Check if the point above also has a left border
                if (i - 1, j, 'left') not in border_points:
                    sides += 1
    return sides

for i in range(len(data)):
    for j in range(len(data[i])):
        if not is_point_in_any_region(i, j):
            region = []
            region.append((i, j))
            region = get_point_region(region, i, j)
            regions.append(region)
            
sum_area_perimeter = 0
for region in regions:
    sum_area_perimeter += len(region) * get_region_number_of_sides(region)
            
print(sum_area_perimeter)