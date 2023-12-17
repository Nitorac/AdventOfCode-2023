from enum import Enum
from collections import deque

IS_PART2 = True

data = [[c for c in line] for line in open('input', 'r').read().splitlines()]


# (i, j)
class Dir(Enum):
    TOP = (-1, 0)
    BOTTOM = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    def angle(self, angle_step):
        """
        :param direction:
        :param angle_step: +1 for each 90° clockwise step
        :return:
        """
        clockwise = [self.TOP, self.RIGHT, self.BOTTOM, self.LEFT]
        return clockwise[(clockwise.index(self) + angle_step) % 4]


def is_valid(i, j, grid):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def next_step(beam, grid):
    i, j, direction = beam
    next_i, next_j = i + direction.value[0], j + direction.value[1]
    if not is_valid(next_i, next_j, grid):
        return []
    step = grid[next_i][next_j]
    next_dirs = []
    match step:
        case '\\':
            match direction:
                case Dir.TOP | Dir.BOTTOM:
                    next_dirs.append(direction.angle(3))
                case Dir.LEFT | Dir.RIGHT:
                    next_dirs.append(direction.angle(1))
        case '/':
            match direction:
                case Dir.TOP | Dir.BOTTOM:
                    next_dirs.append(direction.angle(1))
                case Dir.LEFT | Dir.RIGHT:
                    next_dirs.append(direction.angle(3))
        case '-':
            match direction:
                case Dir.TOP | Dir.BOTTOM:
                    next_dirs.append(direction.angle(1))
                    next_dirs.append(direction.angle(3))
                case _:
                    next_dirs.append(direction)
        case '|':
            match direction:
                case Dir.RIGHT | Dir.LEFT:
                    next_dirs.append(direction.angle(1))
                    next_dirs.append(direction.angle(3))
                case _:
                    next_dirs.append(direction)
        case '.' | '#':
            next_dirs.append(direction)
    return list(map(lambda x: (next_i, next_j, x), next_dirs))


def count_energized(start_beam, grid):
    beams = deque(next_step(start_beam, grid))
    loop_protector = set([])
    path = set([])
    while len(beams) > 0:
        cur = beams.popleft()
        if cur in loop_protector:
            # Break loops
            continue
        loop_protector.add(cur)
        path.add((cur[0], cur[1]))
        nexts = next_step(cur, grid)
        beams.extend(nexts)
    return len(path)


total = 0
if IS_PART2:
    size_i = len(data)
    size_j = len(data[0])
    for i in range(size_i):
        total = max(total, count_energized((i, -1, Dir.RIGHT), data))
        total = max(total, count_energized((i, size_j, Dir.LEFT), data))
    for j in range(size_j):
        total = max(total, count_energized((-1, j, Dir.BOTTOM), data))
        total = max(total, count_energized((size_i, j, Dir.TOP), data))
else:
    total = count_energized((0, -1, Dir.RIGHT), data)

print(total)
