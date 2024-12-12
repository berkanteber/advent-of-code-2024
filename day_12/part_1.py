from __future__ import annotations

import os
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
    regions = {pos: 0 for pos in map_}
    region_idx = 0

    while True:
        try:
            pos = next(pos for pos, region in regions.items() if region == 0)
        except StopIteration:
            break

        cell = map_[pos]

        region_idx += 1
        regions[pos] = region_idx

        to_do = {pos}
        while to_do:
            current_pos = to_do.pop()

            cr, cc = current_pos
            for next_pos in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                if regions.get(next_pos, -1) == 0 and map_[next_pos] == cell:
                    regions[next_pos] = region_idx
                    to_do.add(next_pos)

    areas: defaultdict[int, int] = defaultdict(int)
    perimeters: defaultdict[int, int] = defaultdict(int)
    for pos, region in regions.items():
        areas[region] += 1

        r, c = pos
        for next_pos in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if regions.get(next_pos, -1) != region:
                perimeters[region] += 1

    total = 0
    for region in set(regions.values()):
        total += areas[region] * perimeters[region]

    return total


TEST_DATA = """\
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

assert solve(TEST_DATA) == 1930

print(solve(INPUT_DATA))  # 1471452
