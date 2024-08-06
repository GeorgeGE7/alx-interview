#!/usr/bin/python3
"""Prime game winner determination"""


def isWinner(x, nums):
    """Prime game winner determination"""
    if x < 1 or not nums:
        return None

    ben_wins_count = 0
    maria_wins_count = 0

    # generate a list of prime number based on the max numbers in num
    max_nums = max(nums)
    all_primes = [True] * (max_nums + 1)
    all_primes[0] = all_primes[1] = False

    for x in range(2, int(max_nums**0.5) + 1):
        if all_primes[x]:
            for y in range(x**2, max_nums + 1, x):
                all_primes[y] = False

    # count the no of pm less than n i nums
    for max_nums in nums:
        all_count = sum(all_primes[2:max_nums+1])
        maria_wins_count += all_count % 2 == 1
        ben_wins_count += all_count % 2 == 0

    if ben_wins_count == maria_wins_count:
        return None

    return 'Ben' if maria_wins_count < ben_wins_count else 'Maria'
