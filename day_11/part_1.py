from __future__ import annotations

import os


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def solve(data: str) -> int:
    nums = [int(x) for x in data.split()]
    for _ in range(25):
        next_nums = []
        for num in nums:
            if num == 0:
                next_nums.append(1)
                continue

            num_s = str(num)
            length = len(num_s)
            if length % 2 == 0:
                half_length = length // 2
                next_nums.append(int(num_s[:half_length]))
                next_nums.append(int(num_s[half_length:]))
                continue

            next_nums.append(num * 2024)

        nums = next_nums

    return len(nums)


TEST_DATA = """\
125 17
"""

assert solve(TEST_DATA) == 55312

print(solve(INPUT_DATA))  # 207683
