# Task ID: hard/1

## Topics

['Jarvis March', 'Bellman-Ford Algorithm']

## Cover Story

['cloud city', 'haunted ship']

## Prompt

```python
def shortest_path_to_ogre_city(weights, paths):
    """
    In a fantasy world, there's a ship that sails through an ever-changing labyrinth of floating islands, headed towards the mysterious Ogre City. The ship's journey is represented as a graph where nodes are the islands and the ship's sailing routes between them are directed edges with associated weights. These weights could be positive (indicating ease of travel) or negative (indicating obstacles or challenges).

    Your task is to implement the Bellman-Ford Algorithm to determine the minimum weight path from the starting node (Ship Dock) to the destination node (Ogre City). Each tuple in the paths list represents a directed edge from one node to another, and the corresponding weight for each path is provided in the weights list with matching indices.

    If a negative weight cycle is reachable from the source, making the shortest path problem unsolvable, the function should return -1. If there's no valid path from the start to the destination, also return -1.
    
    Inputs:
    weights: List of integers where each weight corresponds to the path of the same index in the paths list.
    paths: List of tuples where each tuple represents a directed edge from one node to another in the form (from, to).

    Returns:
    int: The minimum weight path sum from the starting node (Ship Dock) to the last node (Ogre City).

    Examples:
    weights = [3, -2, 5, 1]
    paths = [(0, 1), (1, 2), (2, 3)]

    Output:
    7 which is the sum calculated by navigating from node 0 through 1, 2 to 3.
    """

```

## Cleaned Prompt

```python
Given a list of weights and paths of edges, determine the minimum weight path sum from starting node to last node using Bellman-Ford Algorithm. Consider weights positive for ease and negative for challenges. If no valid path exists, return -1.

Examples:
weights = [3, -2, 5, 1]
paths = [(0, 1), (1, 2), (2, 3)]
Output: 7
```

## Warnings

- Solution failed correctness check.
- 5, Incorrect Problem Description: The description of the problem wrongly includes the Jarvis March technique alongside the Bellman-Ford Algorithm, which are unrelated concepts. The Jarvis March is associated with finding the convex hull of a point set, while Bellman-Ford is a graph shortest path algorithm. Mixing these can confuse participants and is misleading regarding the problem's requirements.
- 4, Misalignment in Canonical Solution and Description: The canonical solution references edge weights incorrectly as `weights[u][v]` which mismatches the specified format where weights are provided as a list with corresponding indices to a separate list of edge tuples (paths). The actual usage should correctly access weights based on edge indices to prevent confusion and potential errors in implementations.
- 4, Unclear Edge-Weight Mapping: The problem description does not clearly describe how the weights list and the paths list of tuples are interrelated, except through matching indices. This could potentially confuse participants, leading to difficulties in understanding the mapping of weights to their respective edges, which is crucial for implementing the Bellman-Ford Algorithm correctly.
- 4, Error Handling Inadequacy: The error handling in the problem description versus the practical implementation has discrepancies. It mentions returning -1 for no valid paths, but there isn't a clear strategy or example illustrating how to correctly identify and handle cases where no path from the source to the destination exists, potentially leading to incomplete or erroneous solution implementations.

## Canonical Solution

```python
def bellman_ford(n, edges, weights):
    dist = [float('inf')] * n
    dist[0] = 0
    for _ in range(n - 1):
        for i, (u, v) in enumerate(edges):
            if dist[u] != float('inf') and dist[u] + weights[i] < dist[v]:
                dist[v] = dist[u] + weights[i]
    for i, (u, v) in enumerate(edges):
        if dist[u] != float('inf') and dist[u] + weights[i] < dist[v]:
            return -1  # Negative weight cycle is detected
    return dist[-1] if dist[-1] != float('inf') else -1

n = max(max(u, v) for u, v in paths) + 1
return bellman_ford(n, paths, weights)
```

## Test Cases

```python
def check(candidate):
    assert candidate([3, -2, 5, 1], [(0, 1), (1, 2), (2, 3)]) == 7
    assert candidate([1, 2, 3, 4], [(0, 1), (1, 2), (1, 3)]) == 6
    assert candidate([-1, 2, 3, -4, 5], [(0, 1), (1, 2), (2, 3), (3, 4)]) == 5
    assert candidate([-1, -1, -1], [(0, 1), (1, 2)]) == -3
    assert candidate([10, 20, -5, 2], [(0, 1), (1, 2), (2, 3), (0, 3)]) == 7
```

## Entry Point

`shortest_path_to_ogre_city`

