# Task ID: hard/4

## Topics

['Stack', 'Set Matrix Zeroes', 'Sliding Window']

## Cover Story

['teleporter', 'magic wand']

## Prompt

```python
def teleporter_magic(matrix, operations):
    """
    In a mystical land, a teleporter is represented as an NxM matrix where some cells contain enchanted stones ('S') and others contain mundane rocks ('R'). You have a magic wand that can perform a series of magical operations to manipulate this teleporter in order to optimize energy flow.

    The magic wand can perform the following operations represented in the list of strings 'operations':
    - 'row X': convert all stones ('S') in row X to rocks ('R').
    - 'col Y': convert all stones ('S') in column Y to rocks ('R').
    - 'orient magic': switch the matrix orientation from rows to columns, meaning transposing the matrix.

    After each operation, if any row or column contains only rocks ('R'), it should be filled entirely with stones ('S'). This process can reverse effects of earlier operations in certain cases and is essential to maintain the teleporter's balance.

    Return the matrix state after applying all the operations.

    Example:
    Input: matrix = [['S', 'S', 'R'], ['R', 'S', 'S']], operations = ['col 2', 'orient magic']
    Output: [['S', 'S'], ['S', 'R'], ['S', 'S']]

    Example:
    Input: matrix = [['S', 'R'], ['R', 'S']], operations = ['row 0', 'col 1', 'orient magic', 'row 1']
    Output: [['S', 'S'], ['S', 'R']]

    Note:
    Each 'row X' or 'col Y' operation is 0-indexed. The operations list can be empty, meaning the matrix should be returned as is. 
    """

```

## Cleaned Prompt

```python
Write a function that manipulates a matrix (NxM) depicting a teleporter with different operations. If a matrix row or column turns entirely into 'R' after an operation, it should be inverted to all 'S'. The operations include setting entire rows or columns to 'R', or transposing the matrix. Return the final state of the matrix after all operations.
```

## Warnings

- Solution failed correctness check.
- 4, Ambiguous operation description: The operation "orient magic" described as "switch the matrix orientation from rows to columns" implies a matrix transpose, but the term "orientation" could be confusing. It should be clarified that "orient magic" specifically means to transpose the matrix.

## Canonical Solution

```python
def teleporter_magic(matrix, operations):
    def transpose(mat):
        return [list(row) for row in zip(*mat)]

    def flip_row(mat, r):
        for c in range(len(mat[0])):
            if mat[r][c] == 'S':
                mat[r][c] = 'R'
        if mat[r].count('R') == len(mat[0]):
            mat[r] = ['S'] * len(mat[0])

    def flip_col(mat, col):
        for r in range(len(mat)):
            if mat[r][col] == 'S':
                mat[r][col] = 'R'
        if all(mat[r][col] == 'R' for r in range(len(mat))):
            for r in range(len(mat)):
                mat[r][col] = 'S'

    for op in operations:
        parts = op.split()
        if parts[0] == 'row':
            flip_row(matrix, int(parts[1]))
        elif parts[0] == 'col':
            flip_col(matrix, int(parts[1]))
        elif parts[0] == 'orient magic':
            matrix = transpose(matrix)

    return matrix
```

## Test Cases

```python
def check(candidate):
    assert candidate([['S', 'S', 'R'], ['R', 'S', 'S']], ['col 2', 'orient magic']) == [['S', 'S'], ['S', 'R'], ['S', 'S']]
    assert candidate([['S', 'R'], ['R', 'S']], ['row 0', 'col 1', 'orient magic', 'row 1']) == [['S', 'S'], ['S', 'R']]
    assert candidate([['S', 'S'], ['S', 'S']], []) == [['S', 'S'], ['S', 'S']]
    assert candidate([['R', 'S'], ['R', 'R']], ['row 0', 'row 1', 'col 0']) == [['S', 'S'], ['S', 'R']]
    assert candidate([['S', 'R'], ['S', 'R']], ['orient magic', 'col 1']) == [['S', 'S'], ['R', 'S']]
    assert candidate([['S', 'S'], ['R', 'R']], ['row 1', 'col 0', 'orient magic', 'col 0']) == [['S', 'R'], ['S', 'S']]
```

## Entry Point

`teleporter_magic`

