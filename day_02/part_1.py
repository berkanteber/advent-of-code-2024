from __future__ import annotations

import itertools
import os


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def solve(data: str) -> int:
    reports = [list(map(int, line.split())) for line in data.splitlines()]

    safe = 0
    for report in reports:
        if len(report) <= 2:
            safe += 1
            continue

        first, second = report[:2]
        inc = second > first

        for first, second in itertools.pairwise(report):
            if (second > first) != inc:
                break
            if not (1 <= abs(second - first) <= 3):
                break
        else:
            safe += 1

    return safe


TEST_DATA = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

assert solve(TEST_DATA) == 2

print(solve(INPUT_DATA))  # 598
