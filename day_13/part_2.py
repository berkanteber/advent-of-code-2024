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

    # same slope (vertical)
    if x1 == x2 == 0:
        if x != 0:
            return 0

        costs = []
        if y % y1 == 0:
            costs.append(int(y / y1) * 3)
        if y % y2 == 0:
            costs.append(int(y / y2))

        return min(costs) if costs else 0

    # same slope (horizontal)
    if y1 == y2 == 0:
        if y != 0:
            return 0

        costs = []
        if x % x1 == 0:
            costs.append(int(x / x1) * 3)
        if x % x2 == 0:
            costs.append(int(x / x2))

        return min(costs) if costs else 0

    # same slope
    if y1 / x1 == y2 / x2:
        if y / x != y1 / x1:
            return 0

        costs = []
        if x % x1 == 0 and y % y1 == 0:
            costs.append(int(x / x1) * 3)
        if x % x2 == 0 and y % y2 == 0:
            costs.append(int(x / x2))

        return min(costs) if costs else 0

    # other: single answer
    # x1 * i + x2 * j = x -> j = (x - x1 * i) / x2
    # y1 * i + y2 * j = y -> j = (y - y1 * i) / y2
    # (x - x1 * i) / x2 = (y - y1 * i) / y2
    i = (x * y2 - y * x2) / (x1 * y2 - y1 * x2)
    j = (x - x1 * i) / x2

    return int(3 * i + j) if i == int(i) >= 0 and j == int(j) >= 0 else 0


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

        x += 10000000000000
        y += 10000000000000

        machines.append(((x1, y1), (x2, y2), (x, y)))

    total = 0
    for machine in machines:
        total += _cost(machine)

    return total


print(solve(INPUT_DATA))  # 83029436920891
