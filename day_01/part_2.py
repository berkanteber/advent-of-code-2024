from __future__ import annotations

import os
from collections import Counter


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def solve(data: str) -> int:
    l1, l2 = [], []
    for line in data.splitlines():
        left, right = map(int, line.split())
        l1.append(left)
        l2.append(right)

    counter = Counter(l2)

    return sum(left * counter.get(left, 0) for left in l1)


TEST_DATA = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""

assert solve(TEST_DATA) == 31

print(solve(INPUT_DATA))  # 21024792
