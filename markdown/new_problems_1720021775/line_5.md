# Task ID: hard/1

## Topics

['Monotonic Queue', 'Convex Hull', 'Design']

## Cover Story

['hidden lagoon', 'treasure']

## Prompt

```python
def find_min_risk_path(grid, start, finish):
    """
    Imagine a hidden lagoon filled with treasures varying on its danger level represented as a grid. Each cell in the grid contains a number representing the risk of passing through that cell. The task is to find the minimum risk path from the start to the finish point using a combination of a Monotonic Queue and Convex Hull design.

    The grid is a list of lists of integers where each integer represents the risk level. The goal is to go from the start (top-left, grid[0][0]) to the finish (bottom-right, grid[-1][-1]) position in the grid. You may only move right or down at any step.

    For instance, consider the following grid:
    [[1, 2, 3],
     [4, 5, 1],
     [1, 5, 1]]
    A good candidate path might be: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) with a risk level sum of 8.

    Note:
    - Use the concepts of a Monotonic Queue and Convex Hull to find the optimal path efficiently.
    - Enforce that your solution utilizes these data structures in your pathfinding algorithm to manage complexity.
    """

```

## Cleaned Prompt

```python
Write a function that finds the minimum risk path in a grid from the start position (top-left) to the finish position (bottom-right). You can only move right or down. Utilize the concepts of a Monotonic Queue and Convex Hull to efficiently determine the path.
```

## Warnings

- Solution failed correctness check.
- 5, Misleading Algorithm Requirement: The problem prompt requires the use of a "Monotonic Queue and Convex Hull" design, yet the essence and application of a Convex Hull are not applicable to this grid-based pathfinding context. Convex Hulls are predominantly used in computational geometry to solve problems related to the shape or structure of a dataset, not path minimization in grids where dynamic programming or Dijkstra's algorithm would suffice. This usage can confuse participants or lead to incorrect implementations.
- 4, Unclear Implementation Details: The prompt mentions using a Monotonic Queue which is relatively clear in its application for keeping minimum or maximum values in order. However, it does not provide any detailed reasoning or example on how the Convex Hull should be utilized in this grid pathfinding task, which might leave participants puzzled about the actual expectations.

## Canonical Solution

```python
from collections import deque

def is_valid_point(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def find_min_risk_path(grid, start, finish):
    if not grid or not grid[0]:
        return float('inf')
    m, n = len(grid), len(grid[0])
    risk = [[float('inf')] * n for _ in range(m)]
    risk[start[0]][start[1]] = grid[start[0]][start[1]]
    queue = deque([(start[0], start[1])])
    directions = [(0, 1), (1, 0)]
    while queue:
        x, y = queue.popleft()
        current_risk = risk[x][y]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_point(nx, ny, grid) and current_risk + grid[nx][ny] < risk[nx][ny]:
                risk[nx][ny] = current_risk + grid[nx][ny]
                if (dx, dy) == (0, 1):
                    # Monotonically increase the queue for horizontal move
                    while queue and risk[queue[-1][0]][queue[-1][1]] > risk[nx][ny]:
                        queue.pop()
                queue.append((nx, ny))
    return risk[finish[0]][finish[1]]
```

## Test Cases

```python
def check(candidate):
    # Test case for a simple risk grid
    assert candidate([[1, 2, 3], [4, 5, 1], [1, 5, 1]], (0, 0), (2, 2)) == 8
    # Test cases with increasing grid sizes and complexities
    assert candidate([[1, 100, 1, 100], [100, 1, 100, 1], [1, 100, 1, 100], [100, 1, 100, 1]], (0, 0), (3, 3)) == 4
    assert candidate([[1]], (0, 0), (0, 0)) == 1
    assert candidate([[10, 4, 3], [2, 1000, 6], [8, 9, 1]], (0, 0), (2, 2)) == 14
    # Edge case: large grid to test efficiency
    large_grid = [[1]*1000 for _ in range(1000)]
    assert candidate(large_grid, (0, 0), (999, 999)) == 1998
```

## Entry Point

`find_min_risk_path`

