from __future__ import annotations

import itertools
import os


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def solve(data: str) -> int:
    data = data.strip()
    if len(data) % 2:
        data += '0'

    blocks = []
    spaces = []
    idx = 0
    for size, space in itertools.batched(map(int, data), 2):
        blocks.append((idx, size))
        if space:
            spaces.append((idx + size, space))
        idx += size + space

    try_idx = len(blocks) - 1
    while spaces:
        max_space = max(ss for si, ss in spaces)

        i = try_idx
        while i >= 0:
            try_idx -= 1

            b_idx, b_size = blocks[i]
            if b_size <= max_space:
                break

            i = try_idx
        else:
            break

        for j, s in enumerate(spaces):  # noqa: B007 (`j` not used in loop body)
            s_idx, s_size = s
            if s_size >= b_size:
                break
        else:
            raise AssertionError

        if s_idx > b_idx:
            continue

        blocks[i] = (s_idx, b_size)
        if b_size == s_size:
            spaces.pop(j)
        else:
            spaces[j] = (s_idx + b_size, s_size - b_size)
        spaces.sort()

    checksum = 0
    for file_idx, (idx, size) in enumerate(blocks):
        total = (idx + (idx + size - 1)) * size // 2
        checksum += total * file_idx

    return checksum


TEST_DATA = """\
2333133121414131402
"""

assert solve(TEST_DATA) == 2858

print(solve(INPUT_DATA))  # 6250605700557
