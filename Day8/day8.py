import math

lines = [line.rstrip('\n') for line in open("input", "r").readlines()]
original_path = [0 if c == 'L' else 1 for c in lines[0]]

data = {}

for line in lines[2:]:
    equ = line.split(' = (')
    points = equ[1].split(", ")
    data[equ[0]] = [points[0], points[1].replace(')', '')]

curr_points = [k for k in data.keys() if k.endswith('A')]
ghosts = [0] * len(curr_points)
path_idx = 0
while any(map(lambda x: x == 0, ghosts)):
    turn = original_path[path_idx % len(original_path)]
    for i in range(len(curr_points)):
        curr_points[i] = data[curr_points[i]][turn]
        if curr_points[i].endswith('Z'):
            ghosts[i] = path_idx + 1
    path_idx += 1

print(math.lcm(*ghosts))