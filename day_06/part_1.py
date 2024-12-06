from __future__ import annotations

import os


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def solve(data: str) -> int:
    map_ = {
        (r, c): cell
        for r, row in enumerate(data.splitlines(), 1)
        for c, cell in enumerate(row, 1)

    }

    guard_pos, guard_dir = next(
        (pos, dir_)
        for pos, dir_ in map_.items()
        if dir_ in '^v<>'
    )

    visited = set()
    while True:
        visited.add(guard_pos)

        r, c = guard_pos
        next_pos = {
            '^': (r-1, c),
            'v': (r+1, c),
            '<': (r, c-1),
            '>': (r, c+1),
        }[guard_dir]

        if next_pos not in map_:
            break

        if map_[next_pos] == '#':
            guard_dir = {
                '^': '>',
                'v': '<',
                '<': '^',
                '>': 'v',
            }[guard_dir]
        else:
            guard_pos = next_pos

    return len(visited)


TEST_DATA = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

assert solve(TEST_DATA) == 41

print(solve(INPUT_DATA))  # 4515
