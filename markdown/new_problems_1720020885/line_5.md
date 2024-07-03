# Task ID: hard/1

## Topics

['Matrix', 'Find Median from Data Stream', 'Hash Function']

## Cover Story

['cyberpunk', 'museum']

## Prompt

```python
def museum_security(grid):
    """
    In a cyberpunk future, museums have implemented a high-tech grid-based security system. Each room in the grid receives a security rating. You are given a matrix 'grid' that represents the museum's layout where each cell corresponds to a room and contains the security rating (an integer) of that room.

    However, the user interface only displays the median security rating of all rooms currently visible. The visibility of rooms changes dynamically based on certain conditions, and the guard needs to see the updated median quickly.

    Write a program that provides an efficient way to compute the median of the security ratings in the matrix dynamically if the matrix could be updated repeatedly. Assume that initially, the whole matrix is visible, but over time updates to individual room's ratings may happen.

    - When the rating of a particular room changes, the matrix should be updated, and the median should be recalculated.
    - Assume the matrix can be as large as 100x100 and updates often.
    - The matrix 'grid' contains integers representing security ratings.
    """

```

## Cleaned Prompt

```python
Write a function that provides an efficient way to compute the median of the security ratings in a matrix dynamically as the matrix gets updated repeatedly. Initially, the whole matrix is visible, and the median of all its ratings is needed. Subsequent updates to individual room ratings should be handled, with the median recalculated efficiently
```

## Warnings

- Solution failed correctness check.
- 5, IncompleteUpdateMechanism: The proposed solution does not correctly handle updates to the matrix in a way that maintains accurate information for median calculation. While the canonical solution suggests adding new values with `finder.add_num(new_value)`, it does not remove or adjust the old values that are being replaced in the grid by these updates. This will lead to incorrect median values since the data structure will contain outdated or irrelevant numbers.
- 4, UndefinedBehaviorForUpdates: The problem statement and test descriptions mention that the matrix can be updated, but the pseudocode and canonical implementation do not clearly demonstrate how these updates should be processed beyond simply adding a new number to the data structure. This lack of clarity and explicit handling for updating the Grid's actual entries before recalculating the median could lead to ambiguity and incorrect implementation in a real-world scenario.

## Canonical Solution

```python
    import bisect
    class MedianFinder:
        def __init__(self):
            self.data = []

        def add_num(self, num):
            bisect.insort_left(self.data, num)

        def find_median(self):
            n = len(self.data)
            if n % 2 == 0:
                return (self.data[n//2-1] + self.data[n//2]) / 2.0
            else:
                return self.data[n//2]

    def museum_security(grid):
        finder = MedianFinder()
        for row in grid:
            for value in row:
                finder.add_num(value)
        median = finder.find_median()

        # For updates to grid, the following code should be used:
        # Example of update: grid[x][y] = new_value; finder.add_num(new_value); median = finder.find_median()

        return median

```

## Test Cases

```python
def check(candidate):
    initial_grid = [
        [1, 3, 2],
        [8, 7, 6],
        [5, 9, 4]
    ]
    assert candidate(initial_grid) == 5.0, 'Initial median wrong'

    # Update room at position (2, 2) to 10
    initial_grid[2][2] = 10
    assert candidate(initial_grid) == 5.5, 'Median after first update wrong'

    # Update room at position (0, 0) to 5
    initial_grid[0][0] = 5
    assert candidate(initial_grid) == 5.5, 'Median after second update wrong'

    # Update one more time
    initial_grid[1][0] = 5
    assert candidate(initial_grid) == 5.5, 'Median after third update wrong'

    # Large uniform matrix
    large_grid = [[5]*100 for _ in range(100)]
    assert candidate(large_grid) == 5.0, 'Large uniform matrix median incorrect'
    
    large_grid[0][0] = 100
    assert candidate(large_grid) == 5.0, 'Median after change in large grid incorrect'

```

## Entry Point

`museum_security`

