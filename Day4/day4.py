from collections import deque
from math import floor

IS_PART2 = True

cards = {}

for line in [line.rstrip('\n') for line in open("input", "r").readlines()]:
    main_split = line.split(': ')
    # ID part
    card_id = int(main_split[0].split(' ')[-1])
    # Nums
    num_split = main_split[1].split(' | ')
    # Winning numbers
    win_nums = list(map(lambda x: int(x), filter(lambda x: x.strip() != '', num_split[0].split(' '))))
    # Got numbers
    got_nums = list(map(lambda x: int(x), filter(lambda x: x.strip() != '', num_split[1].split(' '))))

    # Ensure there is no duplicate got nums
    assert len(got_nums) == len(set(got_nums))

    cards[card_id] = {
        "win": set(win_nums),
        "got": set(got_nums)
    }

if not IS_PART2:
    score = 0
    for card in cards.values():
        matches = card['got'] - (card['got'] - card['win'])
        score += floor((2 ** (len(matches) - 1)))

    print(score)
    exit(0)

# Real shit

scratchcards_to_process = deque(cards.items())
scratchcards_used = 0

while len(scratchcards_to_process) > 0:
    card_id, card = scratchcards_to_process.pop()
    scratchcards_used += 1
    matches = card['got'] - (card['got'] - card['win'])
    for i in range(len(matches)):
        m_id = card_id + i + 1
        scratchcards_to_process.append((m_id, cards[m_id]))

print(scratchcards_used)