from __future__ import annotations

import os


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def _count(map_: dict[tuple[int, int], int], initial_pos: tuple[int, int]) -> int:
    done = set()
    to_do = {initial_pos}
    while to_do:
        pos = to_do.pop()
        h = map_[pos]

        r, c = pos
        for next_pos in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if next_pos not in done:
                if map_.get(next_pos, 0) == h + 1:
                    to_do.add(next_pos)

        done.add(pos)

    return sum(1 for pos in done if map_[pos] == 9)


def solve(data: str) -> int:
    map_ = {
        (r, c): int(cell)
        for r, row in enumerate(data.splitlines(), 1)
        for c, cell in enumerate(row, 1)
    }

    total = 0
    zeros = [pos for pos, h in map_.items() if h == 0]
    for zero in zeros:
        total += _count(map_, zero)

    return total


TEST_DATA = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

assert solve(TEST_DATA) == 36

print(solve(INPUT_DATA))  # 548
