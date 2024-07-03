# Task ID: hard/4

## Topics

['Subsets', 'Rolling Hash', 'Shell']

## Cover Story

['haunted ship', 'energetic lightning']

## Prompt

```python
def haunted_ship_signals(n_signals, strike_times, energy_levels):
    """
    The legendary haunted ship 'Ghostly Galleon' emerges every century. Legends say it harnesses the power of energetic lightning strikes, generating signals in a mysterious pattern. Being a part of a research team, you're tasked to analyze these signals in order to predict the next emergence.

    The ship's signals can be described as a sequence of n_signals unique natural numbers. Each signal corresponds to a particular lightning strike, marked by its time since the beginning of the storm and its energy level.

    Every subset of these signals can potentially form a pattern. Your task is to determine the product of the most powerful subset-pattern.
    A subset is considered powerful based on the product of the unique energy levels within it, multiplied by the product of the unique times within it, modulo 1_000_000_007.

    Given this, you must find:
    - the maximal product of any subset of signals using the described criteria.

    Example:
    - n_signals=3
    - strike_times=[1, 10, 100]
    - energy_levels=[5, 10, 5]
    The possible subset-pattern products are computed for each subset. The subset [1, 10, 100] with energies [5, 10, 5] results in a pattern-product of 5 (unique energies) * 110 (unique times) = 550, which would be modulated as 550 % 1_000_000_007.

    Note:
    - Strike times and energy levels are provided as lists of the same length, corresponding to n_signals.
    - There might be overlapping times or energies in different signals, therefore, consider the unique elements when calculating the pattern product.

    Constraints:
    - 1 <= n_signals <= 50
    - 1 <= strike_times[i], energy_levels[i] <= 10^9
    """
```

## Cleaned Prompt

```python
Write a function to determine the maximal product of subsets from lists of strike times and energy levels of signals. The product of a subset is defined as the product of unique strike times multiplied by the product of unique energy levels, mod 1,000,000,007.
```

## Warnings

- Solution failed correctness check.
- 5, Problem Inconsistency with Modulus: The example provided in the prompt states the maximum product subset result modulo 1_000_000_007, yet the test case results do not align with this convention. The test cases do not apply the modulus operation to the results, which contradicts the specification outlined in the prompt. This inaccuracy might lead to incorrect implementation or testing.
- 5, Misleading Test Case: The test case assertion `assert candidate(3, [1, 10, 100], [5, 10, 5]) == 550` explicitly provides a result of 550, which should be incorrect if the modulus operation as per the problem statement were correctly applied. This could confuse participants about the expected output format and the operational definition, leading to failed implementations despite following prompt guidelines.
- 4, Complexity and Performance Issue: The proposed solution's methodology of computing powersets using combinations from the `itertools` module without any optimizations can lead to severe efficiency issues as the number of signals increases. The potential size of the powerset grows exponentially with `n_signals`, which can severely degrade performance especially since `n_signals` can go up to 50, making the approach practically unusable.

## Canonical Solution

```python
def haunted_ship_signals(n_signals, strike_times, energy_levels):
    from itertools import combinations
    mod = 1_000_000_007

    def prod(items):
        result = 1
        for item in items:
            result = (result * item) % mod
        return result

    max_product = 0
    indices = list(range(n_signals))

    for subset_size in range(1, n_signals + 1):
        for subset_indices in combinations(indices, subset_size):
            unique_times = set(strike_times[i] for i in subset_indices)
            unique_energies = set(energy_levels[i] for i in subset_indices)
            subset_product = prod(unique_times) * prod(unique_energies) % mod
            max_product = max(max_product, subset_product)

    return max_product
```

## Test Cases

```python
def check(candidate):
    assert candidate(3, [1, 10, 100], [5, 10, 5]) == 550
    assert candidate(3, [50, 50, 100], [20, 20, 30]) == 3000
    assert candidate(4, [1, 2, 3, 4], [1, 2, 3, 4]) == 288
    assert candidate(5, [100, 200, 300, 400, 500], [1, 2, 3, 4, 5]) == 12000000
    assert candidate(6, [1, 1, 1, 2, 2, 2], [2, 3, 4, 5, 6, 7]) == 56
```

## Entry Point

`haunted_ship_signals`

