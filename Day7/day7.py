from itertools import product
from more_itertools import locate

IS_PART2 = True

lines = [line.rstrip('\n') for line in open("input", "r").readlines()]
data = []

head_map = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

if IS_PART2:
    head_map["J"] = 1


def list_to_count_value(l):
    res = dict(map(lambda x: (x, 0), set(l)))
    for e in l:
        res[e] += 1
    return res


for line in lines:
    separate = line.split(" ")
    data.append({
        "hand": [int(c) if c.isdigit() else head_map[c] for c in separate[0]],
        "bid": int(separate[1])
    })


def hand_order_computation(hand_order):
    return hand_order[0] * 100_000_000 + hand_order[1] * 1_000_000 + hand_order[2] * 10_000 + hand_order[3] * 100 + \
        hand_order[4]


def find_type(hand):
    joker_idxs = list(locate(hand, lambda x: x == 1))
    if not IS_PART2 or len(joker_idxs) == 0:
        return get_type_score(hand)
    card_range = list(range(2, 15))
    all_combs = product(card_range, repeat=len(joker_idxs))
    res = 0
    for comb in all_combs:
        hand_list = hand.copy()
        for i, idx in enumerate(joker_idxs):
            hand_list[idx] = comb[i]

        res = max(res, get_type_score(hand_list))
    return res


def get_type_score(hand_keep_order):
    hand = sorted(
        list_to_count_value(hand_keep_order).items(),
        key=lambda x: (-x[1], -x[0])
    )

    # Five of a kind
    if len(hand) == 1:
        return 60_000_000_000

    # Four of a kind
    elif len(hand) == 2 and hand[0][1] == 4:
        return 50_000_000_000

    # Full house
    elif len(hand) == 2 and hand[0][1] == 3 and hand[1][1] == 2:
        return 40_000_000_000

    # Three of a kind
    elif len(hand) == 3 and hand[0][1] == 3:
        return 30_000_000_000

    # Two pair
    elif len(hand) == 3 and hand[0][1] == 2 and hand[1][1] == 2:
        return 20_000_000_000

    # One pair
    elif len(hand) == 4:
        return 10_000_000_000

    # High card
    elif len(hand) == 5:
        return 0


for game in data:
    mhand = game["hand"]
    game["score"] = find_type(mhand) + hand_order_computation(mhand)

data.sort(key=lambda x: x['score'])

final = 0
for i, game in enumerate(data):
    final += (i + 1) * game['bid']
    print(f"{game['hand']} {game['score']:0>11}")

print(final)
