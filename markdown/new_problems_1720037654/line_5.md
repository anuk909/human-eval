# Task ID: hard/4

## Topics

['Bellman-Ford Algorithm', 'Rejection Sampling']

## Cover Story

['bicycle', 'mysterious cave']

## Prompt

```python
def shortest_safe_path(grid, start, end):
    """
    Imagine a cyclist who wants to traverse through a mysterious cave. The cave is represented as a grid where each cell has a light intensity value. Darker cells (with lower values) are considered more dangerous than brighter ones due to their greater likelihood of hiding obstacles or hazards.

    The task is to find the shortest path from the `start` to the `end` point on this grid while ensuring the path avoids highly dangerous areas. For this, you are required to ignore the darkest 10% of the cells during path calculation. The grid cells are 0-indexed and contain integers where a higher value represents a brighter (safer) area.

    You will use a modified Bellman-Ford Algorithm that incorporates rejection sampling to repeatedly discard paths that include the darkest 10% of cells, until a viable path is found or it is determined that no such path exists. There should be checks to ensure the algorithm does not loop endlessly in case no path is possible, terminating if all paths through permissible cells have been exhausted.

    Use the following movement directions: UP, DOWN, LEFT, and RIGHT. Diagonal movements are not allowed.

    The function should handle complex test cases efficiently and should explicitly avoid paths through highly dangerous zones determined by pixel intensity.

    Example:
    grid = [
      [1, 10, 10],
      [1, 20, 10],
      [1, 50, 30]
    ]
    start = (0, 0)
    end = (2, 2)
    # The output should be a path represented as a list of coordinates from start to end, avoiding the darkest 10% of cells if a path is available. If no safe path is found, return None.
    """

```

## Cleaned Prompt

```python
Create a function that finds the shortest path in a grid from a start point to an end point while avoiding the dimmest 10% of grid cells (measured by their values). Use only vertical and horizontal movements, and employ a modified Bellman-Ford algorithm including rejection sampling to exclude unwanted paths. The grid cells' values represent the light intensity, with higher values indicating brighter and safer areas.
```

## Warnings

- Solution failed correctness check.
- 5, Inconsistent algorithm application: The problem statement mentions the use of a modified Bellman-Ford Algorithm with rejection sampling, but the provided canonical solution implements a straightforward pathfinding approach without including any rejection sampling steps. This lack of consistency between the problem description and the solution can lead to confusion and incorrect implementations.
- 5, Endless looping potential: The task setup and the canonical solution lack mechanisms to effectively handle scenarios where no path is possible due to the constraints of avoiding the darkest 10% of cells. Without proper termination checks, this can lead to endless loops or excessive computation times, making the problem unsolvable for some inputs without a definite or correct stopping condition.
- 4, Ambiguous problem constraints: The description to avoid the "darkest 10% of cells" is ambiguous without specifying the method of calculation for determining these cells. It is unclear whether this refers to the 10% of distinct value types or the overall distribution of all cell values. This ambiguity can result in different interpretations and solutions, affecting the consistency of solution implementations.
- 4, Incorrect or incomplete test cases: The provided test cases in the prompt fail to cover boundary conditions such as very small grids or grids where the light intensity distribution might significantly affect path availability (e.g., all cells being in the darkest 10%). These cases are essential for thoroughly testing the robustness and correctness of the solution implementation.

## Canonical Solution

```python
def is_within_bounds(point, grid):
    x, y = point
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def get_neighbors(point):
    x, y = point
    return [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)] if is_within_bounds((x + dx, y + dy), grid)]

def is_dark(cell, threshold):
    return grid[cell[0]][cell[1]] < threshold

def calculate_intensity_threshold(grid):
    values = [cell for row in grid for cell in row]
    values.sort()
    return values[len(values) // 10]

def bellman_ford(grid, start, end):
    threshold = calculate_intensity_threshold(grid)
    queue = [start]
    visited = set()
    parents = {start: None}
    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]
        for neighbor in get_neighbors(current):
            if not is_dark(neighbor, threshold) and neighbor not in visited:
                queue.append(neighbor)
                parents[neighbor] = current
        visited.add(current)
    if start in visited and not end in visited:
        return None

return bellman_ford(grid, start, end)
```

## Test Cases

```python
def check(candidate):
    grid = [
        [1, 10, 10],
        [1, 20, 10],
        [1, 50, 30]
    ]
    assert candidate(grid, (0, 0), (2, 2)) == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
    grid2 = [
        [1, 0, 100],
        [1, 1, 100],
        [0, 0, 100]
    ]
    assert candidate(grid2, (0, 0), (2, 2)) == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]
    grid3 = [
        [10, 1, 1],
        [100, 1, 1],
        [100, 100, 10]
    ]
    assert candidate(grid3, (0, 0), (2, 2)) == None
    grid4 = [
        [30, 20, 24],
        [18, 19, 17],
        [15, 16, 14]
    ]
    assert candidate(grid4, (0, 0), (0, 2)) == [(0, 0), (0, 1), (0, 2)]
    grid5 = [[1]]
    assert candidate(grid5, (0, 0), (0, 0)) == [(0, 0)]
```

## Entry Point

`shortest_safe_path`

