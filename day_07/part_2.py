from __future__ import annotations

import os


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def _check(val: int, nums: list[int]) -> bool:
    if len(nums) == 0:
        return val == 0

    if len(nums) == 1:
        return nums[0] == val

    if nums[0] > val:
        return False

    return any((
        _check(val, [int(str(nums[0]) + str(nums[1]))] + nums[2:]),
        _check(val, [nums[0] * nums[1]] + nums[2:]),
        _check(val, [nums[0] + nums[1]] + nums[2:]),
    ))


def solve(data: str) -> int:
    equations = {}
    for line in data.splitlines():
        value_part, nums_part = line.split(': ')
        value = int(value_part)
        nums = [int(num_s) for num_s in nums_part.split()]

        assert all(num > 0 for num in nums)
        equations[value] = nums

    total = 0
    for val, nums in equations.items():
        if _check(val, nums):
            total += val

    return total


TEST_DATA = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

assert solve(TEST_DATA) == 11387

print(solve(INPUT_DATA))  # 500335179214836
