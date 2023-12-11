IS_PART2 = True

grid = []
for line in [line.rstrip('\n') for line in open("input", "r").readlines()]:
    grid.append([c for c in line])

NUM_LINES = len(grid)
NUM_COLS = len(grid[0])


def get_number_from_pos(a, b):
    start = b
    # Get back to the start of the number
    while start >= 0 and grid[a][start].isdigit():
        start -= 1
    start += 1
    # Return to the first digit
    end = start
    # Read the number
    while end < NUM_COLS and grid[a][end].isdigit():
        end += 1
    end -= 1
    return int(''.join(grid[a][start:end + 1]))


def get_part_numbers(a, b):
    parts = set([])

    if IS_PART2 and grid[a][b] != '*':
        return parts

    for i in range(a - 1, a + 2):
        for j in range(b - 1, b + 2):
            if i < 0 or i >= NUM_LINES or j < 0 or j >= NUM_COLS:
                continue
            if grid[i][j].isdigit():
                parts.add(get_number_from_pos(i, j))
    if IS_PART2:
        parts = {parts.pop() * parts.pop() if len(parts) == 2 else 0}
    return parts


res = 0
for i in range(NUM_LINES):
    for j in range(NUM_COLS):
        if not grid[i][j].isdigit() and not grid[i][j] == '.':
            parts = get_part_numbers(i, j)
            res += sum(parts)

print(res)
