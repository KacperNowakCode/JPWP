def _is_prime_trial(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


def find_primes_trial_division(input_list):

    n = len(input_list)
    primes = []
    for number in range(2, n + 1):
        if _is_prime_trial(number):
            primes.append(number)
    return primes


def find_primes_sieve(input_list):
    n = len(input_list)
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while (p * p <= n):
        if (sieve[p] == True):
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1

    primes = [p for p in range(n + 1) if sieve[p]]
    return primes