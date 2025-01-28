#!/usr/bin/python3
'''Calculates the fewest number of operations needed to result in exactly n H characters'''
def min_operations(n):
    '''Gets the prime factors of n and adds them to operations'''
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            n = n // factor
            operations = operations + factor
        factor = factor + 1
    print(operations)
    return operations
