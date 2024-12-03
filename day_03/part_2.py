from __future__ import annotations

import os
import re


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def solve(data: str) -> int:
    real_data = ''
    while (i := data.find("don't()")) != -1:
        real_data += data[:i]
        data = data[i+7:]
        if (j := data.find("do()")) == -1:
            break

        data = data[j+4:]
    else:
        real_data += data

    return sum(
        int(first) * int(second)
        for first, second
        in re.findall(r'mul\((\d+),(\d+)\)', real_data)
    )


TEST_DATA = """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

assert solve(TEST_DATA) == 48

print(solve(INPUT_DATA))  # 95411583
