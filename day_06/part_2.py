from __future__ import annotations

import os


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def _check(map_: dict[tuple[int, int], str]) -> tuple[set[tuple[int, int]], bool]:
    guard_pos, guard_dir = next(
        (pos, dir_)
        for pos, dir_ in map_.items()
        if dir_ in '^v<>'
    )

    visited_with_dir = set()
    cycled = False
    while True:
        pos_with_dir = guard_pos, guard_dir
        if pos_with_dir in visited_with_dir:
            cycled = True
            break
        visited_with_dir.add(pos_with_dir)

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

    return {pos for pos, _ in visited_with_dir}, cycled


def solve(data: str) -> int:
    map_ = {
        (r, c): cell
        for r, row in enumerate(data.splitlines(), 1)
        for c, cell in enumerate(row, 1)

    }

    visited, cycled = _check(map_)
    assert not cycled

    total = 0
    for pos in visited:
        if map_[pos] in '^v<>':
            continue

        _, cycled = _check({**map_, pos: '#'})
        if cycled:
            total += 1

    return total


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

assert solve(TEST_DATA) == 6

print(solve(INPUT_DATA))  # 1309
