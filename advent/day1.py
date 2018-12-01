DAY = 1

def frequency(changes):
    freq = 0
    for change in changes:
        freq += int(change)
    return freq

def firstduplicatefreq(changes):
    changes_list = [int(c) for c in changes]
    size = len(changes_list)
    freq = 0
    index = 0
    seen_freqs = set([freq])
    while True:
        change = changes_list[index % size]
        freq += change
        if freq in seen_freqs:
            return freq
        seen_freqs.add(freq)
        index += 1

def solve1(filename):
    with open(filename) as f:
        return frequency(f)

def solve2(filename):
    with open(filename) as f:
        return firstduplicatefreq(f)