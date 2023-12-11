lines = [line.rstrip('\n') for line in open("input", "r").readlines()]
data = []

head_map = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


def list_to_count_value(l):
    res = dict(map(lambda x: (x, 0), set(l)))
    for e in l:
        res[e] += 1
    return res


for line in lines:
    separate = line.split(" ")
    data.append({
        "hand": sorted(
            list_to_count_value([int(c) if c.isdigit() else head_map[c] for c in separate[0]]).items(),
            key=lambda x: (-x[1], -x[0])
        ),
        "bid": int(separate[1])
    })


def get_score_for_hand(hand):
    # Five of a kind
    if len(hand) == 1:
        return 60_000_000_000 + hand[0][0]

    # Four of a kind
    elif len(hand) == 2 and hand[0][1] == 4:
        return 50_000_000_000 + hand[0][0] * 100 + hand[1][0]

    # Full house
    elif len(hand) == 2 and hand[0][1] == 3 and hand[1][1] == 2:
        return 40_000_000_000 + hand[0][0] * 100 + hand[1][0]

    # Three of a kind
    elif len(hand) == 3 and hand[0][1] == 3:
        return 30_000_000_000 + hand[0][0] * 10_000 + hand[1][0] * 100 + hand[2][0]

    # Two pair
    elif len(hand) == 3 and hand[0][1] == 2 and hand[1][1] == 2:
        return 20_000_000_000 + hand[0][0] * 10_000 + hand[1][0] * 100 + hand[2][0]

    # One pair
    elif len(hand) == 4:
        return 10_000_000_000 + hand[0][0] * 1_000_000 + hand[1][0] * 10_000 + hand[2][0] * 100 + hand[3][0]

    # High card
    elif len(hand) == 5:
        return hand[0][0] * 100_000_000 + hand[1][0] * 1_000_000 + hand[2][0] * 10_000 + hand[3][0] * 100 + hand[4][0]


for game in data:
    game["score"] = get_score_for_hand(game["hand"])

data.sort(key=lambda x: x['score'])

final = 0
for i, game in enumerate(data):
    final += (i+1) * game['bid']

print(final)