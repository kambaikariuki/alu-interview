#!/usr/bin/python3
'''Calculates least operations needed to result in exactly n H characters'''


def minOperations(n):
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
    return operations
