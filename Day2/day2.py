import pprint
import functools

IS_PART2 = True

QUESTION_PART1 = {"red": 12, "green": 13, "blue": 14}

# Parsing file into data structure
games = {}
for line in open("input", "r").readlines():
    main_split = line.rstrip('\n').split(': ')
    game_id = int(main_split[0].split(' ')[1])
    games[game_id] = []

    for set in main_split[1].split('; '):
        obj = {}
        for cubes in set.split(', '):
            keyval = cubes.split(' ')
            obj[keyval[1]] = int(keyval[0])
        games[game_id].append(obj)


# Checking valid games

def is_valid_game_part1(mgame):
    for mcubes in mgame:
        if (
                mcubes.get("red", 0) > QUESTION_PART1["red"] or
                mcubes.get("blue", 0) > QUESTION_PART1["blue"] or
                mcubes.get("green", 0) > QUESTION_PART1["green"]
        ):
            return False
    return True


def get_power_game_part2(mgame):
    res = {
        "red": 0,
        "blue": 0,
        "green": 0,
    }
    for msets in mgame:
        for k, v in msets.items():
            res[k] = max(res[k], v)
    return functools.reduce(lambda a, b: a * b, res.values())


msum = 0
for i, game in games.items():
    if IS_PART2:
        msum += get_power_game_part2(game)
    else:
        msum += i if is_valid_game_part1(game) else 0

print(msum)
