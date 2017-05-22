"""
CP1404/CP5632 Practical
Recursion
"""


def calc_blocks_needed(rows):
    if rows <= 0:
        return 0
    return rows + calc_blocks_needed(rows - 1)


print(calc_blocks_needed(6))
