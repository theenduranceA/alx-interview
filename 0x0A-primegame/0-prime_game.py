#!/usr/bin/python3
""" A script for Prime Game. """


def isWinner(x, nums):
    """Function to determine the winner in a prime game between two players."""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def count_primes_up_to_n(n):
        count = sum(1 for i in range(2, n + 1) if is_prime(i))
        return count

    maria_wins, ben_wins = 0, 0

    for n in nums:
        prime_count = count_primes_up_to_n(n)
        ben_wins += prime_count % 2 == 0
        maria_wins += prime_count % 2 == 1

    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
