# Task ID: hard/3

## Topics

['Find Median from Data Stream', 'Geometry', 'Bucket Sort']

## Cover Story

['dragons', 'robotic theme park']

## Prompt

```python
def dragon_sightings_median(operations):
    """
    A robotic theme park filled with dragons has a special system to track the spotting of dragons. Each dragon sighting is marked with its X-coordinate on a 1D stretch of the park which ranges from 0 to 2000 units.
    Since it's hard to calculate the median on the fly as the sightings are continuously monitored, you are tasked to develop a system to track and provide the median sighting position effectively after each operation.

    The operations will be provided as a list of tuples where each tuple can be either:
    - ('add', X), meaning a new sighting is added at point X, or
    - ('get_median',), which requests the current median of all sightings added until then.

    The median is the middle value in an array of numbers. If there are an even number of numbers, the median is taken as the average of the two middle numbers.

    Note):
    - Use bucket sort-like techniques, given the limited range of possible sighting positions (0 to 2000).
    - Ensure efficient operations for both adding sightings and retrieving the median.

    Examples:
    - If operations = [('add', 1000), ('get_median',)] -> returns [1000.0]
    - If operations = [('add', 500), ('add', 1500), ('get_median',)] -> returns [1500.0]

    Return a list of the results for all 'get_median' operations in the order they are requested.
    """

```

## Cleaned Prompt

```python
Write a function that simulates tracking dragon sightings in a robotic theme park. It takes a list of operations about additions of sightings and requests for the median sighting position, processing them effectively.

Example:
- operations = [('add', 1000), ('get_median',)]: return [1000.0]
- operations = [('add', 500), ('add', 1500), ('get_median',)]: return [1000.0]

Each sighting is reported with an X-coordinate ranging from 0 to 2000. Use bucket sort to handle sightings and efficiently compute the median as requested.
```

## Warnings

- Solution failed correctness check.
- 5, Inconsistent Result Examples: The provided example results in the problem description do not match the outcomes specified in the testing assertions. This discrepancy creates confusion about what the correct output should be. For instance, the problem statement example [('add', 500), ('add', 1500), ('get_median',)] suggests a result of [1500.0], whereas the test asserts it should be [1000.0]. Similarly, the example for operations with values 50, 50, 80, 100 does not align well with both expected and asserted medians.
- 4, Ambiguous Problem Statement: The problem statement implies the use of bucket sort for performance efficiency but does not clearly define how to handle large numbers of operations efficiently, especially with frequent median calculations. While it mentions a range limitation (0 to 2000), it does not provide a clear directive or suggestion on how to manage or optimize multiple 'add' operations followed by 'get_median' operations without causing performance degradation.

## Canonical Solution

```python
    def dragon_sightings_median(operations):
        limits = 2001
        buf = [0] * limits
        count = 0

        def add(val):
            buf[val] += 1
            nonlocal count
            count += 1

        def get_median():
            mid_index = (count + 1) // 2
            current = 0
            for i in range(limits):
                current += buf[i]
                if count % 2 == 1:
                    if current >= mid_index:
                        return float(i)
                else:
                    if current == mid_index:
                        for j in range(i + 1, limits):
                            if buf[j] > 0:
                                return (i + j) / 2.0
                    elif current > mid_index:
                        if current - buf[i] < mid_index:
                            return float(i)
                        
        result = []
        for operation in operations:
            if operation[0] == 'add':
                add(operation[1])
            elif operation[0] == 'get_median':
                result.append(get_median())
        return result
```

## Test Cases

```python
def check(candidate):
    assert candidate([('add', 1000), ('get_median',)]) == [1000.0]
    assert candidate([('add', 500), ('add', 1500), ('get_median',)]) == [1000.0]
    assert candidate([('add', 0), ('add', 0), ('add', 2000), ('add', 2000), ('get_median',)]) == [1000.0]
    assert candidate([('add', 50), ('add', 50), ('add', 80), ('get_median',), ('add', 100), ('get_median',)]) == [60.0, 65.0]
    assert candidate([('add', 100), ('add', 700), ('add', 800), ('add', 900), ('add', 1600), ('get_median',)]) == [800.0]
```

## Entry Point

`dragon_sightings_median`

