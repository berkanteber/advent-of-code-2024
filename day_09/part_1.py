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
    total_size = 0
    idx = 0
    file_idx = 0
    for size, space in itertools.batched(map(int, data), 2):
        blocks.append((idx, size, file_idx))
        if space:
            spaces.append((idx + size, space))

        total_size += size
        idx += size + space
        file_idx += 1

    ordered_blocks, unordered_blocks = [], []
    for block in blocks:
        idx, size, file_idx = block
        if idx + size <= total_size:
            ordered_blocks.append(block)
        elif idx >= total_size:
            unordered_blocks.append(block)
        else:
            ordered_blocks.append((idx, total_size - idx, file_idx))
            unordered_blocks.append((total_size, size - (total_size - idx), file_idx))

    spaces.sort(reverse=True)
    unordered_blocks.sort()
    while unordered_blocks:
        s_idx, s_size = spaces[-1]
        b_idx, b_size, b_file_idx = unordered_blocks[-1]

        if b_size < s_size:
            ordered_blocks.append((s_idx, b_size, b_file_idx))
            unordered_blocks.pop()
            spaces[-1] = (s_idx + b_size, s_size - b_size)
        elif b_size == s_size:
            ordered_blocks.append((s_idx, s_size, b_file_idx))
            unordered_blocks.pop()
            spaces.pop()
        else:
            ordered_blocks.append((s_idx, s_size, b_file_idx))
            unordered_blocks[-1] = (b_idx, b_size - s_size, b_file_idx)
            spaces.pop()

    checksum = 0
    for idx, size, file_idx in sorted(ordered_blocks):
        total = (idx + (idx + size - 1)) * size // 2
        checksum += total * file_idx

    return checksum


TEST_DATA = """\
2333133121414131402
"""

assert solve(TEST_DATA) == 1928

print(solve(INPUT_DATA))  # 6225730762521
