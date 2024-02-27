#!/usr/bin/python3
""" Script for Making Change."""


def makeChange(coins, total):
    """ Function to determine the fewest number of coins needed to
    meet a given amount total in a pile of coins of different values,"""

    if total < 0:
        return 0
    x = [float('inf')] * (total + 1)
    x[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            x[i] = min(x[i], x[i - coin] + 1)
    return x[total] if x[total] != float('inf') else -1
