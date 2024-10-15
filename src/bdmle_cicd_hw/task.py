from typing import List
import math
import random

def is_prime(x: int) -> bool:
    if x <= 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True

def get_primes(m: int, n: int) -> List[int]:
    res = []
    
    for i in range(m, n + 1):
        if is_prime(i):
            res.append(i)

    return res

def get_primes_fast(m: int, n: int) -> List[int]:
    primes = get_primes(2, int(math.sqrt(n)))

    res = []
    for i in range(2, n + 1):
        is_prime = True
        for prime in primes:
            if i == prime:
                break
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            res.append(i)

    return res

def primes(count: int) -> List[int]:
    prime_numbers = get_primes_fast(2, 100000)

    return prime_numbers[:count]

def checksum(x: List[int]) -> int:
    current_checksum = 0

    for value in x:
        current_checksum += value    
        current_checksum *= 113
        current_checksum %= 10_000_007

    return current_checksum

def pipeline() -> int:
    prime_numbers = primes(1000)

    random.seed(100)
    random.shuffle(prime_numbers)

    return checksum(prime_numbers)