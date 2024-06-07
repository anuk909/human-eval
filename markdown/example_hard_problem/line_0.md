# Task ID: hard/0

## Prompt

```python
def product_of_primes(numbers):
    """
    Write a function that takes a list of integers and returns the product of all the prime numbers in the list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    For example, if the input is [2, 3, 4, 5, 6, 7, 8, 9, 10], the output should be 210 because the prime numbers in the list are 2, 3, 5, and 7, and their product is 2 * 3 * 5 * 7 = 210.

    Note:
    - If the input list is empty, return 1 (the product of an empty set of numbers is 1).
    - The input list may contain duplicate numbers, but you should only consider each unique number once.
    """

```

## Canonical Solution

```python
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [n for n in set(numbers) if is_prime(n)]
    result = 1
    for p in primes:
        result *= p
    return result
```

## Test Cases

```python
def check(candidate):
    assert candidate([2, 3, 4, 5, 6, 7, 8, 9, 10]) == 210
    assert candidate([]) == 1
    assert candidate([3, 4, 5, 6, 7, 8, 9, 10, 11]) == 1155
    assert candidate([2, 4, 6, 8, 10]) == 2
    assert candidate([3, 7, 2, 4]) == 42
```

## Entry Point

`product_of_primes`

