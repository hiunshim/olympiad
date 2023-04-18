from test_framework import generic_test
from typing import Dict

cache:  Dict[int, int] = {}

def fibonacci(n: int) -> int:
    # TODO - you fill in here.
    if n <= 1:
      return n
    elif n not in cache:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n] 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
