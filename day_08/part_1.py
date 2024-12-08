from __future__ import annotations

import itertools
import os
import string
from collections import defaultdict


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def solve(data: str) -> int:
    map_ = {
        (r, c): cell
        for r, row in enumerate(data.splitlines(), 1)
        for c, cell in enumerate(row, 1)
    }

    freqs = defaultdict(list)
    for coord, cell in map_.items():
        if cell in string.ascii_letters + string.digits:
            freqs[cell].append(coord)

    antinodes = set()
    for freq_coords in freqs.values():
        for (r1, c1), (r2, c2) in itertools.permutations(freq_coords, 2):
            antinode = (2 * r2 - r1, 2 * c2 - c1)
            if antinode in map_:
                antinodes.add(antinode)

    return len(antinodes)


TEST_DATA = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

assert solve(TEST_DATA) == 14

print(solve(INPUT_DATA))  # 371
