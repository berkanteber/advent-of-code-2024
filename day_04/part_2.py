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
        if cell != 'A':
            continue

        with suppress(KeyError):
            if (
                d[r-1, c-1] + d[r+1, c+1] in ('MS', 'SM') and
                d[r-1, c+1] + d[r+1, c-1] in ('MS', 'SM')
            ):
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

assert solve(TEST_DATA) == 9

print(solve(INPUT_DATA))  # 1992
