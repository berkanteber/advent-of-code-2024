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
    sides_h: defaultdict[int, list[tuple[float, float, float]]] = defaultdict(list)
    sides_v: defaultdict[int, list[tuple[float, float, float]]] = defaultdict(list)
    for pos, region in regions.items():
        areas[region] += 1

        r, c = pos

        # below (3x + nx) / 4 means this: put middle line closer to the region
        # this solves the problem in `TEST_DATA_2`

        for next_pos in ((r + 1, c), (r - 1, c)):
            if regions.get(next_pos, -1) != region:
                nr, nc = next_pos
                sides_h[region].append(((3 * r + nr) / 4, c - .5, c + .5))
        for next_pos in ((r, c + 1), (r, c - 1)):
            if regions.get(next_pos, -1) != region:
                nr, nc = next_pos
                sides_v[region].append(((3 * c + nc) / 4, r - .5, r + .5))

    total = 0
    for region in set(regions.values()):
        region_sides_h = sorted(sides_h[region])
        final_region_sides_h = [region_sides_h[0]]
        for r2, c21, c22 in region_sides_h[1:]:
            r1, c11, c12 = final_region_sides_h[-1]
            if r1 == r2 and c12 == c21:
                final_region_sides_h[-1] = (r1, c11, c22)
            else:
                final_region_sides_h.append((r2, c21, c22))

        region_sides_v = sorted(sides_v[region])
        final_region_sides_v = [region_sides_v[0]]
        for c2, r21, r22 in region_sides_v[1:]:
            c1, r11, r12 = final_region_sides_v[-1]
            if c1 == c2 and r12 == r21:
                final_region_sides_v[-1] = (c1, r11, r22)
            else:
                final_region_sides_v.append((c2, r21, r22))

        total += areas[region] * (len(final_region_sides_h) + len(final_region_sides_v))

    return total


TEST_DATA_1 = """\
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""

assert solve(TEST_DATA_1) == 436

TEST_DATA_2 = """\
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
"""

assert solve(TEST_DATA_2) == 368

TEST_DATA_3 = """\
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

assert solve(TEST_DATA_3) == 1206

print(solve(INPUT_DATA))  # 863366
