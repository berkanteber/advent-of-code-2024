from __future__ import annotations

import os
import re


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


RE_BUTTON = re.compile(r'Button (A|B): X\+(?P<x>\d+), Y\+(?P<y>\d+)')
RE_PRIZE = re.compile(r'Prize: X=(?P<x>\d+), Y=(?P<y>\d+)')


def _cost(machine: tuple[tuple[int, int], tuple[int, int], tuple[int, int]]) -> int:
    (x1, y1), (x2, y2), (x, y) = machine

    costs = []
    for i in range(101):
        for j in range(101):
            if x1 * i + x2 * j == x and y1 * i + y2 * j == y:
                costs.append(3 * i + j)

    return min(costs) if costs else 0


def solve(data: str) -> int:
    machines = []
    for machine_data in data.split('\n\n'):
        l1, l2, l3 = machine_data.splitlines()

        m1 = RE_BUTTON.fullmatch(l1)
        m2 = RE_BUTTON.fullmatch(l2)
        m3 = RE_PRIZE.fullmatch(l3)
        assert m1 and m2 and m3

        x1, y1 = map(int, m1.groups()[1:])
        x2, y2 = map(int, m2.groups()[1:])
        x, y = map(int, m3.groups())

        machines.append(((x1, y1), (x2, y2), (x, y)))

    total = 0
    for machine in machines:
        total += _cost(machine)

    return total


TEST_DATA = """\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

assert solve(TEST_DATA) == 480

print(solve(INPUT_DATA))  # 36838
