# Task ID: hard/3

## Topics

['Treap', 'Detect Cycle in Graph']

## Cover Story

['spaceship', 'energy vortex']

## Prompt

```python
def optimal_energy_path(command_centers, connections):
    """
    As the head engineer of a fleet's energy distribution system in a network of command centers, you are required to design an algorithm that determines the optimal paths for energy transfer between these command centers while ensuring no cycles are formed (the network should form a tree-like structure). Each center and their direct connections are given as unique integers and a list of tuples respectively.

    Your function should accept two parameters: an array of integers representing command centers and a list of tuples representing the bidirectional connections between these command centers. The aim is to select connections that form a tree rooted at the command center with the smallest number appearing most frequently in the connections, optimizing for minimal path cost based on a predefined metric like latency.

    Define a function to calculate the path cost and ensure that your tree minimizes this cost. The focus should be on solving the problem algorithmically without the need for visualization tools or external libraries.

    Example:
    Given the command centers [1, 2, 3, 4, 5] and the connections [(1, 2), (1, 3), (2, 3), (3, 4), (5, 1)], your function should return an optimal tree structure as a list of tuples representing the connections, like [(1, 2), (1, 3), (3, 4), (5, 1)].

    Notes:
    - Ensure there are no cycles in the output configuration.
    - Handle the case where not all command centers are initially interconnected.
    - Duplicate links might be present and should be managed accordingly.
    """

```

## Cleaned Prompt

```python
Implement a system to manage and find optimal paths for energy transfer between command centers to form a non-cyclic structure, maintaining a tree-like property (treap) for minimizing a cost function. You should also be able to visualize the computed structure.
```

## Warnings

- Solution failed correctness check.
- 5, Undefined Metric: The problem statement lacks a clear definition of the "predefined metric like latency" used for calculating the path costs, leading to ambiguity in understanding how to optimize the tree.
- 5, No Clear Instructions on Handling Duplicates: Although the problem mentions that duplicate links might be present and should be managed accordingly, it provides no specific guidance or method on how duplicates should be handled, affecting the stability and predictability of the function's output.
- 5, Ambiguous Root Selection Criteria: The problem specifies that the tree should be rooted at the command center with the smallest number appearing most frequently in the connections, yet no tie-breaking rules or further explanation is provided on how to select the root in scenarios where multiple centers meet this criterion equally.
- 4, Incomplete Function Definition: The function signature and description do not specify the return type clearly. Although the examples imply the return should be a list of tuples representing connections, this is not explicitly stated in the function signature or description.

## Canonical Solution

```python
    # Define key functions for handling tree operations and optimizing paths

    class TreeNode:
            def __init__(self, value):
                self.value = value
                self.connections = []

        def min_cost_tree(command_centers, connections):
            # Implement cycle detection, tree construction and optimization considering path costs

        def calculate_path_cost(...):
            # Defines how to calculate cost between nodes

        # Process the command centers and connections to build an optimized tree
    
```

## Test Cases

```python
def check(candidate):
    assert candidate([1, 2, 3, 4, 5], [(1, 2), (1, 3), (2, 3), (3, 4), (5, 1)]) == [(1, 2), (1, 3), (3, 4), (5, 1)]
    assert candidate([1, 2, 3, 4], [(1, 2), (2, 3), (3, 1), (4, 2)]) == [(1, 2), (2, 3), (4, 2)]
    assert candidate([1, 2], [(1, 2), (2, 1)]) == [(1, 2)]
    assert candidate([1, 2, 3, 4, 5], []) == []
    assert candidate([1], []) == []

```

## Entry Point

`optimal_energy_path`

