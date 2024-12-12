from __future__ import annotations

import os
from collections import defaultdict


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def solve(data: str, steps: int = 75) -> int:
    nums = [(int(x), 1) for x in data.split()]
    for _ in range(steps):
        next_nums = []
        for num, count in nums:
            if num == 0:
                next_nums.append((1, count))
                continue

            num_s = str(num)
            length = len(num_s)
            if length % 2 == 0:
                half_length = length // 2
                next_nums.append((int(num_s[:half_length]), count))
                next_nums.append((int(num_s[half_length:]), count))
                continue

            next_nums.append((num * 2024, count))

        next_nums_d: defaultdict[int, int] = defaultdict(int)
        for num, count in next_nums:
            next_nums_d[num] += count

        nums = list(next_nums_d.items())

    return sum(count for _, count in nums)


TEST_DATA = """\
125 17
"""

assert solve(TEST_DATA, 25) == 55312

print(solve(INPUT_DATA))  # 244782991106220
