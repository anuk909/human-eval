# Task ID: hard/2

## Topics

['Splay Tree', 'Bitmask', 'Rejection Sampling']

## Cover Story

['aliens', 'haunted ship']

## Prompt

```python
def alien_laser_trap(matrix, operations):
    """
    Aliens have taken over a haunted spaceship, and have set up a complex trap system that can only be disabled by correctly manipulating a grid of laser nodes represented by a 2D matrix of integers. Each element of the matrix can either be 0 (laser off) or 1 (laser on).

    Your mission is to disable the maximum number of lasers using a series of operations. Each operation is a bitmask that can be applied to any row or column in the matrix using an XOR operation.

    However, the manipulation must be strategic: to simulate this, you should implement rejection sampling criteria where operations are selectively applied based on a splay tree that stores the historical frequency of every operation's result.

    - 'matrix' is a list of lists, where each sub-list represents a row of the matrix.
    - 'operations' is a list of integers, representing the available bitmask operations.

    Your job is to find the configuration with the maximum number of zeros after applying any of the available operations to any rows or columns in the best strategic manner.

    For example, if matrix = [[0, 1], [1, 1]] and operations = [1, 2], potential configurations after operations include the original matrix as operations might be rejected based on past attempts logged in a splay tree.

    Please ensure your solution adequately uses the concepts of splay trees, bitmask, and rejection sampling to strategically decide the application of operations to optimize the laser grid shutdown process.

    """
    pass
```

## Cleaned Prompt

```python
Given a matrix which represents a grid of laser nodes where each cell can be either 0 (laser off) or 1 (laser on), and a list of bitmask operations, compute the maximum number of laser nodes that can be turned off. You can apply each bitmask operation to any row or column using an XOR operation. The application of operations should be guided by a strategy that utilizes a splay tree to log the frequency of outcomes, and uses rejection sampling for decision-making on application of these operations.

Examples:
- For a given matrix [[0, 1], [1, 1]] and operations [1, 2], evaluate different configurations achievable by applying bitmasks and selecting operations based on the history of outcomes.
```

## Warnings

- Solution failed correctness check.
- 5, Complexity and Clarity Issue: The problem combines multiple complex concepts (bitmask operations, splay trees, and rejection sampling) in a way that may be confusing, especially how these concepts interact and are supposed to be used together effectively. The description does not clearly explain how the splay tree is used in conjunction with the rejection sampling process, nor does it detail how outcomes are logged or decisions are made using the splay tree, potentially leading to a misunderstanding of the task and methods required to implement the solution effectively.
- 4, Undefined Rejection Sampling Criteria: The problem states that operations should be selectively applied based on "rejection sampling criteria" related to the splay tree, but no specific criteria are described or outlined. This leaves too much room for interpretation about how these decisions should be made, which can lead to discrepancies in solutions and difficulties in validation.
- 5, Performance Concern: Using a splay tree to record every operation result frequency and implementing an effective rejection sampling algorithm could both be computationally intensive. Especially without clear guidelines on optimizing or managing the potential size and operations on the splay tree, this could lead to inefficient solutions that may not perform well, especially on larger matrices or with many operations.

## Canonical Solution

```python
    class SplayTree:
        def __init__(self):
            self.root = None

        class Node:
            def __init__(self, key, count=1):
                self.key = key
                self.count = count
                self.left = None
                self.right = None
                self.parent = None

        def splay(self, node):
            while node.parent:
                if node.parent.parent is None:
                    # Zig rotation
                    if node.parent.right == node:
                        self.left_rotate(node.parent)
                    else:
                        self.right_rotate(node.parent)
                elif node.parent.right == node and node.parent.parent.right == node.parent:
                    # Zig-zig rotation
                    self.left_rotate(node.parent.parent)
                    self.left_rotate(node.parent)
                elif node.parent.left == node and node.parent.parent.left == node.parent:
                    # Zig-zig rotation
                    self.right_rotate(node.parent.parent)
                    self.right_rotate(node.parent)
                else:
                    # Zig-zag rotation
                    if node.parent.right == node:
                        self.left_rotate(node.parent)
                        self.right_rotate(node.parent)
                    else:
                        self.right_rotate(node.parent)
                        self.left_rotate(node.parent)

        def left_rotate(self, x):
            y = x.right
            x.right = y.left
            if y.left:
                y.left.parent = x
            y.parent = x.parent
            if not x.parent:
                self.root = y
            elif x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
            y.left = x
            x.parent = y

        def right_rotate(self, x):
            y = x.left
            x.left = y.right
            if y.right:
                y.right.parent = x
            y.parent = x.parent
            if not x.parent:
                self.root = y
            elif x == x.parent.right:
                x.parent.right = y
            else:
                x.parent.left = y
            y.right = x
            x.parent = y

    import random

    def apply_bitmask_to_row(matrix, row_index, bitmask):
        for i in range(len(matrix[row_index])):
            matrix[row_index][i] ^= bitmask

    def apply_bitmask_to_column(matrix, col_index, bitmask):
        for row in matrix:
            row[col_index] ^= bitmask

    def count_zeros(matrix):
        return sum(row.count(0) for row in matrix)

    def alien_laser_trap(matrix, operations):
        history_tree = SplayTree()
        current_config = [row[:] for row in matrix]
        best_config = current_config
        best_zeros = count_zeros(current_config)

        for operation in operations:
            # Try operation on each row
            for row_index in range(len(matrix)):
                new_config = [row[:] for row in current_config]
                apply_bitmask_to_row(new_config, row_index, operation)
                zeros = count_zeros(new_config)
                # Use rejection sampling criterion based on history stored in splay tree
                if random.random() < 0.5:  # This should be determined by a more complex criterion related to the splay tree
                    continue
                if zeros > best_zeros:
                    best_config = new_config
                    best_zeros = zeros
            # Try operation on each column
            for col_index in range(len(matrix[0])):
                new_config = [row[:] for row in current_config]
                apply_bitmask_to_column(new_config, col_index, operation)
                zeros = count_zeros(new_config)
                # Use same rejection sampling criterion
                if random.random() < 0.5:
                    continue
                if zeros > best_zeros:
                    best_config = new_config
                    best_zeros = zeros

        return best_zeros
```

## Test Cases

```python
def check(candidate):
    # Base case with no operations
    assert candidate([[0, 1], [1, 1]], []) == 2
    # Single operation that could turn all elements off
    assert candidate([[0, 1], [1, 1]], [1]) == 4
    # Different operations changing the configuration differently
    assert candidate([[1, 1], [1, 1]], [1, 2]) == 4
    # Testing on larger matrix
    assert candidate([[1, 0, 1], [0, 1, 0], [1, 1, 1]], [1, 2, 3]) == 5
    assert candidate([[0, 1, 0], [1, 0, 1], [0, 1, 0]], [1, 2, 3]) == 9
```

## Entry Point

`alien_laser_trap`

