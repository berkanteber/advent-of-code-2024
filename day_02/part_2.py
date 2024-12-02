from __future__ import annotations

import itertools
import os


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def _safe(report: list[int]) -> bool:
    if len(report) <= 2:
        return True

    first, second = report[:2]
    inc = second > first

    for first, second in itertools.pairwise(report):
        if (second > first) != inc:
            return False
        if not (1 <= abs(second - first) <= 3):
            return False

    return True


def solve(data: str) -> int:
    reports = [list(map(int, line.split())) for line in data.splitlines()]

    safe = 0
    for report in reports:
        if _safe(report):
            safe += 1
            continue

        for i in range(len(report)):
            if _safe(report[:i] + report[i+1:]):
                safe += 1
                break

    return safe


TEST_DATA = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

assert solve(TEST_DATA) == 4

print(solve(INPUT_DATA))  # 634
