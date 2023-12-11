from functools import reduce

lines = [line.rstrip('\n') for line in open("input", "r").readlines()]
times = [int(e) for e in filter(lambda x: x, lines[0].split(': ')[1].split(' '))]
distances = [int(e) for e in filter(lambda x: x, lines[1].split(': ')[1].split(' '))]

data = []
for i in range(len(times)):
    data.append((times[i], distances[i]))

res = []
for race_duration, race_distance in data:
    winner_races = 0
    for button_hold_time in range(1, race_duration):
        lasting_duration = race_duration - button_hold_time
        boat_distance = lasting_duration * button_hold_time
        if boat_distance > race_distance:
            winner_races += 1
    res.append(winner_races)
print(res)
print(reduce(lambda x, y: x * y, res))
