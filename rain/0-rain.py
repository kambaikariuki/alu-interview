#!/usr/bin/python3
'''Rain function'''


def rain(walls):
    if not walls:
        return 0

    left, right = 0, len(walls) - 1
    left_max, right_max = walls[left], walls[right]
    water_trapped = 0

    while left < right:
        if walls[left] < walls[right]:
            if walls[left] >= left_max:
                left_max = walls[left]
            else:
                water_trapped += left_max - walls[left]
            left += 1
        else:
            if walls[right] >= right_max:
                right_max = walls[right]
            else:
                water_trapped += right_max - walls[right]
            right -= 1

    return water_trapped
