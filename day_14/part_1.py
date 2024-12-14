from __future__ import annotations

import os


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def solve(data: str, size: tuple[int, int] = (101, 103)) -> int:
    positions = {}
    velocities = {}
    for i, line in enumerate(data.splitlines(), 1):
        loc_s, v_s = line.split()
        x, y = map(int, loc_s[2:].split(','))
        vx, vy = map(int, v_s[2:].split(','))

        positions[i] = x, y
        velocities[i] = vx, vy

    len_x, len_y = size
    for robot, (vx, vy) in velocities.items():
        x, y = positions[robot]
        positions[robot] = (x + 100 * vx) % len_x, (y + 100 * vy) % len_y

    assert len_x % 2 == 1 and len_y % 2 == 1
    hx, hy = int(len_x / 2), int(len_y / 2)

    quads = {'tl': 0, 'tr': 0, 'bl': 0, 'br': 0}
    for x, y in positions.values():
        if x < hx and y < hy:
            quads['tl'] += 1
        elif x > hx and y < hy:
            quads['tr'] += 1
        elif x < hx and y > hy:
            quads['bl'] += 1
        elif x > hx and y > hy:
            quads['br'] += 1

    return quads['tl'] * quads['tr'] * quads['bl'] * quads['br']


TEST_DATA = """\
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""

assert solve(TEST_DATA, (11, 7)) == 12

print(solve(INPUT_DATA))  # 232589280
