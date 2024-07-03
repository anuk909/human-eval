# Task ID: hard/3

## Topics

['Binary Tree Level Order Traversal', 'Ternary Search', 'Two-Sum Problem']

## Cover Story

['haunted ship', 'wizard school']

## Prompt

```python
def haunted_ship_vision(tree, darkness_val, target_val):
    """
    At the World's End Wizarding School, there's a legend about a haunted ship that appears on full moon nights. This ship is visible only through enchanted trees that grow in the school's courtyard. These trees are no ordinary trees but are represented as binary trees where each node holds a visibility value.

    The visibility of the ship through these trees depends on two main factors:
    - 'darkness_val': a certain darkness value which represents how dark the night is when observing the ship; the darker, the easier to observe if nodes' values are higher.
    - 'target_val': the illumination value required to actually spot the ship.

    Your task is to:
    1. Perform a level order traversal on the binary tree and retrieve the visibility values.
    2. Adjust these visibility values based on the 'darkness_val' by applying a ternary search to optimize and find an 'adjusted_visibility_factor' which maximizes the visibility values in a way that as many nodes as possible are equal or exceed the 'target_val'.
    3. Determine if there are any two unique nodes at the same level of the tree whose visibility values sum up to exactly 'target_val' (similar to two-sum problem).

    The function should return a tuple (is_spot_possible, list_levels) where:
    - 'is_spot_possible': is a boolean that indicates if it's possible to spot the ship by finding two nodes at any level whose adjusted values sum up to 'target_val'.
    - 'list_levels': is a list of lists, with each sublist representing visibility values of nodes at each level after adjusting with the 'optimal_visibility_factor'.

    Example:
    # Binary Tree Structure
    #        5
    #       / \ 
    #      3   8
    #     /|   |
    #    2 4   7
    # Binary tree represented as a simple example. The actual tree will be more complex.
    
    The output for a case where darkness_val = 2, target_val=15 would typically involve an optimal adjustment of visibility values and checking pairs for the two-sum problem.

    """

```

## Cleaned Prompt

```python
Define a function that takes a binary tree and two integers, darkness_val and target_val as inputs. Perform a level order traversal on the binary tree and iteratively adjust the node values using a ternary search to maximize the number of nodes exceeding target_val. Afterwards, check at each level if two unique node values summed equal target_val. Return a tuple, with the first element indicating if a sum matching target_val was found, and the second element listing the adjusted node values for each level.
```

## Warnings

- Solution failed correctness check.
- 5, Undefined functionality: The problem statement mentions the use of "ternary search to optimize and find an 'adjusted_visibility_factor' which maximizes the visibility values", but it doesn't define how to perform this ternary search in relation to the provided tree values, darkness_val, and target_val. This leaves a critical part of the task undefined, making the problem unsolvable as specified.
- 4, Complexity of multiple tasks: The problem simultaneously requires a level-order traversal, an application of an undefined ternary search technique, and a check for two unique nodes whose values sum to a specific target. Combining these distinct tasks into a single function makes the problem overly complex and potentially confusing.

## Canonical Solution

```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

def is_possible_to_sum_to_target(values, target):
    needed = set()
    for value in values:
        if (target - value) in needed:
            return True
        needed.add(value)
    return False

def haunted_ship_vision(tree, darkness_val, target_val):
    if not tree:
        return (False, [])

    queue = deque([tree])
    list_levels = []
    is_spot_possible = False

    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            node = queue.popleft()
            adjusted_value = ternary_search_optimization(node.val, darkness_val, target_val) # Placeholder for the ternary search implementation
            level_nodes.append(adjusted_value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        list_levels.append(level_nodes)
        if not is_spot_possible:
            is_spot_possible = is_possible_to_sum_to_target(level_nodes, target_val)

    return (is_spot_possible, list_levels)
```

## Test Cases

```python
def check(candidate):
    # Define the tree as per the earlier example
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)

    # Assume ternary_search_optimization is a correct implementation
    is_spot_possible, levels = candidate(root, 2, 15)
    assert is_spot_possible == False  # Dependent on ternary search optimization working and tree setup
    assert levels == [[10], [6, 16], [4, 8, 14]]  # The expected adjusted levels

    # Test with different darkness_val
    is_spot_possible, levels = candidate(root, 1, 9)
    assert is_spot_possible == True  # Should find pairs now after adjustment
    assert levels == [[5], [3, 8], [2, 4, 7]]  # Based on darkness_val

    # Test with empty tree
    is_spot_possible, levels = candidate(None, 2, 5)
    assert is_spot_possible == False
    assert levels == []
```

## Entry Point

`haunted_ship_vision`

