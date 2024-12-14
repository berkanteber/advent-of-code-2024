from __future__ import annotations

import os


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def parse(data: str) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    positions = []
    velocities = []
    for line in data.splitlines():
        loc_s, v_s = line.split()
        x, y = map(int, loc_s[2:].split(','))
        vx, vy = map(int, v_s[2:].split(','))

        positions.append((x, y))
        velocities.append((vx, vy))

    return positions, velocities


def print_map(
    positions: list[tuple[int, int]],
    velocities: list[tuple[int, int]],
    steps: int,
    max_avg_entropy: float,
) -> bool:
    len_x, len_y = 101, 103

    final_positions = set()
    for robot, (vx, vy) in enumerate(velocities):
        x, y = positions[robot]
        final_positions.add(((x + steps * vx) % len_x, (y + steps * vy) % len_y))

    entropy = 0.
    for fx, fy in final_positions:
        for nf in (
            (fx + 1, fy), (fx - 1, fy), (fx, fy + 1), (fx, fy - 1),
            (fx + 1, fy + 1), (fx + 1, fy - 1), (fx - 1, fy + 1), (fx - 1, fy - 1),
        ):
            if nf not in final_positions:
                entropy += 1 / 8

    avg_entropy = entropy / len(final_positions)

    if avg_entropy > max_avg_entropy:
        return False

    print(avg_entropy)

    if steps < 10:
        sep = ' '.join([str(steps)] * 60)
    elif steps < 100:
        sep = ' '.join([str(steps)] * 40)
    elif steps < 1000:
        sep = ' '.join([str(steps)] * 30)
    elif steps < 10000:
        sep = ' '.join([str(steps)] * 24)
    elif steps < 100000:
        sep = ' '.join([str(steps)] * 20)
    else:
        raise AssertionError

    print(sep)
    for j in range(len_y):
        print(' ' * 10, end='')
        for i in range(len_x):
            print('*' if (i, j) in final_positions else ' ', end='')
        print()
    print(sep)

    return True


positions, velocities = parse(INPUT_DATA)

steps = 0
while True:
    while True:
        printed = print_map(positions, velocities, steps, .9)
        steps += 1
        if printed:
            break
    input()

# 7659
