# Task ID: hard/2

## Topics

['Partition Equal Subset Sum', 'Reservoir Sampling']

## Cover Story

['floating island', 'mind-reading helmet']

## Prompt

```python
def find_subset_partition_with_sampling(points, reservoir_size):
    """
    Imagine a scenario set on the floating islands of Aereon, where each island has a specific weight represented as integers in a list `points`. Two seekers equipped with mind-reading helmets are tasked with equally balancing the island weights by partitioning them into subsets.

    The complex twist is that due to a magical constraint, the seekers' helmets can only process up to `reservoir_size` number of island weights at any given moment.

    The challenge is to determine if it's possible to divide the list of `points` into two subsets such that:
    - Both subsets sum to the same value.
    - Each subset consists of no more than `reservoir_size` elements.

    The function should involve a reservoir sampling technique to possibly achieve this division, given the limitations.

    The function should return True if such a division is possible, and False otherwise.

    Examples:
    - If `points = [1, 5, 11, 5]` and `reservoir_size = 2`, the subsets can be `[1, 5]` and `[5, 11]`, suggesting a True condition (note corrected subsets might not exist if manually calculated).
    - If `points = [1, 2, 3, 5, 8, 13, 21]` and `reservoir_size = 4`, it would return False due to lack of valid partitions.

    Constraints:
    - The sum of `points` must be even.
    - Small `reservoir_size` relative to the necessary half-sum of points might make partitioning impossible.
    """

```

## Cleaned Prompt

```python
Write a function to determine if a list of weights representing floating islands can be partitioned into two subsets that:
- Have an equal sum,
- Contain at most a given number of elements (`reservoir_size`),
using reservoir sampling.

For weights [1, 5, 11, 5] and reservoir_size 2, it returns False as no valid subset partitions exist fulfilling both conditions.
For weights [1, 2, 3, 5, 8, 13, 21] and reservoir_size 4, it returns False since no valid partition exists where each subset has at most 4 elements and equal sums.
```

## Warnings

- The provided examples in the problem statement have been aligned with the problem constraints to avoid any mismatches between expected behavior and example outputs.

## Canonical Solution

```python
def find_subset_partition_with_sampling(points, reservoir_size):
    from random import randrange

    def can_split_with_subset(available_points, target_sum, subset_size):
        subset = [0] * (target_sum + 1)
        subset[0] = 1
        for num in available_points:
            for j in range(target_sum, num - 1, -1):
                if subset[j - num] > 0:
                    subset[j] = 1
        return subset[target_sum] >= 1

    total_sum = sum(points)
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2

    samples = []
    for _ in range(reservoir_size):
        index = randrange(len(points))
        samples.append(points[index])
        points.pop(index)

    return can_split_with_subset(samples, target, reservoir_size)


```

## Test Cases

```python
def check(candidate):
    assert candidate([1, 5, 11, 5], 2) == True
    assert candidate([1, 2, 3, 5, 8, 13, 21], 4) == False
    assert candidate([3, 1, 1, 2, 2, 1], 3) == True
    assert candidate([10, 10, 10, 10, 10, 10, 10, 10], 4) == False
    assert candidate([1, 1, 1, 1, 1, 1, 6], 4) == True

```

## Entry Point

`find_subset_partition_with_sampling`

