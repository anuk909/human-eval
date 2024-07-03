# Task ID: hard/3

## Topics

['Miller-Rabin Primality Test', 'Euclidean Algorithm']

## Cover Story

['spaceship', 'wizards']

## Prompt

```python
def spaceship_wizard_magic(image, spells):
    """
    In a futuristic world, spaceships are powered by magical spells cast by wizards. The power of each spell is determined by the number of visible stars in a specific region (rectangle) of the galaxy captured in a nighttime image. The wizard's powerful magic requires prime spells, and spells interact through the greatest common denominator of their powers in accordance with ancient wizardry laws.

    Given a binary image (2D list) where 1 represents a star and 0 represents empty space, and a list of rectangle coordinates that denote specific regions in the image, compute and return:
    - The prime power spell for each region.
    - The greatest common denominator of all prime power spells computed.

    The prime power spell of a region is defined as the sum of stars (1's) calculated for that region of the image and must itself be a prime number. If a region's sum is not prime, it should be substituted with the next largest prime number.

    Use the Miller-Rabin primality test to identify prime numbers and the Euclidean algorithm to calculate the greatest common denominator (GCD).

    Consider only unique regions, i.e., identical coordinate tuples should be considered once. The regions are defined by tuples (row_start, row_end, col_start, col_end), 0-indexed and inclusive.

    Example input image, spells and output are illustrated in the problems below.

    Note:
    - The image is of size NxM, and regions can cover any part without exceeding the image bounds.
    - Process the output in the format: {'spells': [list_of_prime_powers], 'gcd': gcd_of_prime_powers}
    """
```

## Canonical Solution

```python
    from random import randrange
    def is_prime(n, k=5):  # Miller-Rabin
        if n <= 1: return False
        if n <= 3: return True
        if n % 2 == 0: return False
        d = n - 1
        while d % 2 == 0: d //= 2
        for _ in range(k):
            a = randrange(2, n - 1)
            x = pow(a, d, n)
            if x == 1 or x == n - 1: continue
            while d != n - 1:
                x = (x * x) % n
                d *= 2
                if x == 1: return False
                if x == n - 1: break
            else: return False
        return True
    def next_prime(n):
        temp = n + 1
        while not is_prime(temp): temp += 1
        return temp
    def gcd(x, y):
        while y != 0: (x, y) = (y, x % y)
        return x
    def calculate_region_sum(image, sr, er, sc, ec):
        return sum(sum(row[sc:ec+1]) for row in image[sr:er+1])
    def spaceship_wizard_magic(image, spells):
        unique_spells = list(set(spells))
        prime_spells = []
        for (sr, er, sc, ec) in unique_spells:
            region_sum = calculate_region_sum(image, sr, er, sc, ec)
            if not is_prime(region_sum):
                region_sum = next_prime(region_sum)
            prime_spells.append(region_sum)
        all_gcd = prime_spells[0]
        for spell_power in prime_spells[1:]:
            all_gcd = gcd(all_gcd, spell_power)
        return {'spells': prime_spells, 'gcd': all_gcd}
```

## Test Cases

```python
def check(candidate):
    image = [[1, 0, 0], [0, 1, 1], [1, 0, 1]]
    spells = [(0, 2, 0, 2), (1, 2, 1, 2)]
    assert candidate(image, spells) == {'spells': [5, 3], 'gcd': 1}
    image2 = [[1, 0], [1, 1]]
    spells2 = [(0, 1, 0, 1)]
    assert candidate(image2, spells2) == {'spells': [3], 'gcd': 3}
    image3 = [[1]*10]*10
    spells3 = [(0, 9, 0, 9), (0, 9, 0, 9)]  # unique handling
    assert candidate(image3, spells3) == {'spells': [101], 'gcd': 101}
    image4 = [[0]*5]*5
    spells4 = [(0, 4, 0, 4)]
    assert candidate(image4, spells4) == {'spells': [2], 'gcd': 2}
    image5 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    spells5 = [(0, 0, 0, 2), (1, 1, 1, 1), (2, 2, 0, 2)]
    assert candidate(image5, spells5) == {'spells': [3, 2, 3], 'gcd': 1}
```

## Entry Point

`spaceship_wizard_magic`

