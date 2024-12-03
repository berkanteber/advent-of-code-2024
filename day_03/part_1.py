from __future__ import annotations

import os
import re


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def solve(data: str) -> int:
    return sum(
        int(first) * int(second)
        for first, second
        in re.findall(r'mul\((\d+),(\d+)\)', data)
    )


TEST_DATA = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

assert solve(TEST_DATA) == 161

print(solve(INPUT_DATA))  # 180233229
