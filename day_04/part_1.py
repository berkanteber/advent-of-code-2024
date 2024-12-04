from __future__ import annotations

import os
from contextlib import suppress


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def solve(data: str) -> int:
    d = {
        (r, c): cell
        for r, row in enumerate(data.splitlines(), 1)
        for c, cell in enumerate(row, 1)
    }

    count = 0
    for (r, c), cell in d.items():
        if cell != 'X':
            continue

        for first, second, third in (
            ((r-1, c), (r-2, c), (r-3, c)),
            ((r+1, c), (r+2, c), (r+3, c)),
            ((r, c-1), (r, c-2), (r, c-3)),
            ((r, c+1), (r, c+2), (r, c+3)),
            ((r-1, c-1), (r-2, c-2), (r-3, c-3)),
            ((r-1, c+1), (r-2, c+2), (r-3, c+3)),
            ((r+1, c-1), (r+2, c-2), (r+3, c-3)),
            ((r+1, c+1), (r+2, c+2), (r+3, c+3)),
        ):
            with suppress(KeyError):
                if d[first] == 'M' and d[second] == 'A' and d[third] == 'S':
                    count += 1

    return count


TEST_DATA = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

assert solve(TEST_DATA) == 18

print(solve(INPUT_DATA))  # 2571
