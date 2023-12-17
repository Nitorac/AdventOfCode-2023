from heapq import heappush, heappop, heapify

IS_PART2 = True

data = [[int(c) for c in line] for line in open('input', 'r').read().splitlines()]


def is_valid(i, j, grid):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def min_cost_dijkstra(grid, start, end, min_dir, max_dir):
    queue = [
        (grid[start[0] + 1][start[1]], start[0] + 1, start[1], 1, 0, 1),
        (grid[start[0]][start[1] + 1], start[0], start[1] + 1, 0, 1, 1)
    ]
    loop_protector = set([])
    heapify(queue)
    while len(queue) > 0:
        loss, i, j, dir_i, dir_j, steps = heappop(queue)
        if i == end[0] and j == end[1] and steps >= min_dir:
            return loss

        if (i, j, dir_i, dir_j, steps) in loop_protector:
            continue
        loop_protector.add((i, j, dir_i, dir_j, steps))

        for direction in [(dir_i, dir_j), (-dir_j, dir_i), (dir_j, -dir_i)]:
            next_e = (i + direction[0], j + direction[1])
            if is_valid(next_e[0], next_e[1], grid):
                if dir_i == direction[0] and dir_j == direction[1] and steps >= max_dir:
                    continue
                if (dir_i != direction[0] or dir_j != direction[1]) and steps < min_dir:
                    continue
                heappush(queue, (
                    loss + grid[next_e[0]][next_e[1]],
                    next_e[0],
                    next_e[1],
                    direction[0],
                    direction[1],
                    steps + 1 if dir_i == direction[0] and dir_j == direction[1] else 1
                ))
    raise Exception("No solution found")


min_direction = 4 if IS_PART2 else 0
max_direction = 10 if IS_PART2 else 3

print(min_cost_dijkstra(data, (0, 0), (len(data) - 1, len(data[0]) - 1), min_direction, max_direction))
