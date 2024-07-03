# Task ID: hard/3

## Topics

['Divide and Conquer', 'Tree']

## Cover Story

['parallel universe', 'hot air balloon']

## Prompt

```python
def maximum_balloon_visibility(data_matrix):
    """
    In a parallel universe, researchers are studying visibility patterns of hot air balloons from their labs which are structured in a tree-form matrix.

    Design a function that takes as input a 2D matrix (list of lists) where each cell contains a tuple. The first element of the tuple represents the height of a lab and the second element represents the number of hot air balloons visible from that lab. The structure of the 2D matrix represents a quad-tree: every cell (lab) can have four children, corresponding to the cells immediately to the right (East), immediately below (South), bottom-right (Southeast), and bottom-left (Southwest) within its own sub-matrix if such cells exist.

    The goal is to find out the maximum number of hot air balloons visible from any lab in the matrix. Use a 'divide and conquer' approach efficiently, applying recursion suitable for processing tree-structured data.

    For example, if the input matrix is:
    [
        [(3, 2), (1, 5)],
        [(7, 1), (2, 3)]
    ]
    The output should be 5, which is the maximum number of balloons seen (from the lab with height 1).

    Constraints:
    - The height of a lab does not affect the visibility of balloons.
    - The matrix will always be of a size 2^n x 2^n.
    - The elements of the matrix represent (height, balloons), where both are integers.
    """
```

## Cleaned Prompt

```python
def maximum_balloon_visibility(data_matrix):
    """
    Input: a 2D matrix (list of lists) where each cell contains a tuple. Each tuple's first element represents the height of a lab, and the second element represents the number of hot air balloons visible. The matrix represents a quad-tree. Find the maximum number of hot air balloons visible from any lab using a 'divide and conquer' approach.

    Each lab's tuple is of form (height, balloons) where both are integers, and the matrix is always size 2^n x 2^n.
    """
```

## Canonical Solution

```python
    def max_balloons(matrix):
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0][1]

        mid = len(matrix) // 2
        top_left = [row[:mid] for row in matrix[:mid]]
        top_right = [row[mid:] for row in matrix[:mid]]
        bottom_left = [row[:mid] for row in matrix[mid:]]
        bottom_right = [row[mid:] for row in matrix[mid:]]

        return max(max_balloons(top_left), max_balloons(top_right), max_balloons(bottom_left), max_balloons(bottom_right))

    return max_balloons(data_matrix)
```

## Test Cases

```python
def check(candidate):
    assert candidate([[(3, 2), (1, 5)], [(7, 1), (2, 3)]]) == 5
    assert candidate([[(3, 2)],[ (7, 1)] ]) == 2
    assert candidate([[(10, 8)],[(20, 3)]]) == 8
    assert candidate([[ (5, 1), (4, 4)], [ (7, 5), (8, 6)], [(2, 3), (3, 2)], [(1, 4), (9, 7)]]) == 6
    assert candidate([[ (12, 12)], [(23, 11)]]) == 12
```

## Entry Point

`maximum_balloon_visibility`

## Warnings

- Solution failed correctness check.
- 4, Inconsistency in matrix size handling: The problem statement specifies that the input matrix will always be of size 2^n x 2^n, but tests include matrices that are not of this size, for example, a matrix of size 1x2. This inconsistency can lead to confusion or errors when implementing the solution, as the provided solution assumes a square matrix of size corresponding to powers of two.
- 4, Canonical solution implementation missing entry-point function: The canonical solution provides the logic inside a function named "max_balloons" which is locally defined within another function not provided in the text but assumed to be "maximum_balloon_visibility". The entire solution should be enclosed correctly in the function that matches the entry point specified in the prompt to ensure clarity and correctness.

