from __future__ import annotations

import itertools
import os


INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(INPUT_PATH) as f:
    INPUT_DATA = f.read()


def solve(data: str) -> int:
    rules_data, updates_data = data.split('\n\n')

    rules = {
        tuple(map(int, line.split('|')))
        for line in rules_data.splitlines()
    }

    updates = [
        tuple(map(int, line.split(',')))
        for line in updates_data.splitlines()
    ]
    incorrect_updates = [
        update for update in updates
        if any(
            (num2, num1) in rules
            for num1, num2 in itertools.pairwise(update)
        )
    ]

    total = 0
    for update in incorrect_updates:
        sorted_update = []
        update_rules = {
            (lower, higher)
            for lower, higher in rules
            if lower in update and higher in update
        }
        while update_rules:
            lowers = {lower for lower, _ in update_rules}
            highers = {higher for _, higher in update_rules}

            sorted_update.append((lowers - highers).pop())
            update_rules = {
                (lower, higher)
                for lower, higher in update_rules
                if lower != sorted_update[-1]
            }

        total += sorted_update[len(sorted_update) // 2]

    return total


TEST_DATA = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

assert solve(TEST_DATA) == 123

print(solve(INPUT_DATA))  # 6204
