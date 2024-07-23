#!/usr/bin/python3
"""
Coin Change Algorithm - greedy algorithm
"""


def makeChange(coins, total) -> int:
    """Given a list of coins and a total amount,
    calculate the fewest number of coins needed to meet the total.
    Returns -1 if not possible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    total_clone = total
    c, coins_num = (0, 0)
    len_coins = len(coins)

    while(c < len_coins and total_clone > 0):
        if (total_clone - coins[c]) >= 0:
            total_clone -= coins[c]
            coins_num += 1
        else:
            c += 1

    validate = total_clone > 0 and coins_num > 0
    return -1 if validate or coins_num == 0 else coins_num
