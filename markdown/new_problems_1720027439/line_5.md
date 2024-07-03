# Task ID: hard/5

## Topics

['Minimum Path Sum', 'Strongly Connected Component']

## Cover Story

['energy vortex', 'restaurant']

## Prompt

```python
def energy_paths(energy_grid, minimum_energy, layout):
    """
    In a futuristic restaurant, the tables are arranged in a grid-like layout and are powered by an energy system. Each cell in this grid layout may represent an energy node. The configuration of these nodes and their connectivity forms the basis of the restaurant's design. The scenario is defined with three grids of equal dimensions:

    - 'energy_grid': A 2D list with each cell containing a positive integer that represents the energy level at that position.
    - 'minimum_energy': A 2D list specifying the minimum energy threshold required for each node to be active.
    - 'layout': A grid consisting of '0's and '1's where '1' signifies an active area of the restaurant (i.e., an area that contains energy nodes which are considered for computation).

    Tasks:
    - Identify connected components of cells in the energy grid that meet or exceed their corresponding values in 'minimum_energy'. Each cell can connect orthogonally (up, down, left, right) to its adjacent neighbors.
    - Compute the shortest path from the top-left to the bottom-right of the identified largest connected component using the sum of energy values as path weights. Return -1 if no valid path exists.

    Note: Only cells marked as '1' in the layout are considered for determining connectivity and path computation.

    Example:
    energy_grid = [[5, 4], [6, 8]]
    minimum_energy = [[3, 4], [10, 8]]
    layout = [[1, 1], [1, 1]]
    Output: 24 (since the available path from top-left to bottom-right goes through cells meeting their energy thresholds).
    """

```

## Cleaned Prompt

```python
Write a function that takes three 2D lists, 'energy_grid', 'minimum_energy', and 'layout'. Each cell in 'energy_grid' represents the energy level in that cell. Each cell in 'minimum_energy' represents a threshold below which the energy is not sufficient. The 'layout' grid indicates which cells are part of the restaurant with '1', and '0' otherwise. You need to find the strongly connected components where all nodes have energy greater than or equal to the minimum threshold and are part of the restaurant layout. Within the largest such component, find the minimum energy path sum from the top-left to the bottom-right corner. If no valid path exists, return -1. Include examples to illustrate.
```

## Warnings

- Solution failed correctness check.
- 4, Ambiguity in Component Connectivity: The problem statement does not specify whether the largest connected component determination is based solely on the count of cells or if it should also consider the total energy levels of the cells. This ambiguity could lead to different interpretations of what constitutes the "largest" component, potentially affecting the outcome of the problem.

## Canonical Solution

```python
    def find_largest_connected_component_and_min_path(energy_grid, minimum_energy, layout):
        rows, cols = len(energy_grid), len(energy_grid[0])
        def is_within_bounds(x, y):
            return 0 <= x < rows and 0 <= y < cols

        # Check if the energy level meets the threshold and it is within layout
        def is_valid(x, y):
            return layout[x][y] == 1 and energy_grid[x][y] >= minimum_energy[x][y]

        # Use DFS to explore nodes, marking them and finding connected components
        def dfs(x, y, visit_mark):
            stack = [(x, y)]
            component = []
            while stack:
                cx, cy = stack.pop()
                if (cx, cy) not in visit_mark:
                    visit_mark.add((cx, cy))
                    component.append((cx, cy))
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = cx + dx, cy + dy
                        if is_within_bounds(nx, ny) and is_valid(nx, ny):
                            stack.append((nx, ny))
            return component

        # Discover all valid components
        all_components = []
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if is_valid(r, c) and (r, c) not in visited:
                    component = dfs(r, c, visited)
                    if component:
                        all_components.append(component)

        # Find the largest component based on length
        largest_component = max(all_components, key=len, default=[]) 
        if not largest_component:
            return -1  # No valid path exists

        # Find the minimum path sum from the top-left to the bottom-right within the largest component
        min_path_sum = [[float('inf')] * cols for _ in range(rows)]
        min_path_sum[0][0] = energy_grid[0][0] if is_valid(0, 0) else float('inf')
        queue = [(0, 0)]
        while queue:
            x, y = queue.pop(0)
            current_sum = min_path_sum[x][y]
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if is_within_bounds(nx, ny) and (nx, ny) in largest_component and current_sum + energy_grid[nx][ny] < min_path_sum[nx][ny]:
                    min_path_sum[nx][ny] = current_sum + energy_grid[nx][ny]
                    queue.append((nx, ny))

        # If the bottom-right is unreachable or not part of the component, return -1
        if min_path_sum[-1][-1] == float('inf'):
            return -1
        return min_path_sum[-1][-1]

    return find_largest_connected_component_and_min_path(energy_grid, minimum_energy, layout)

```

## Test Cases

```python
def check(candidate):
    # Example test cases
    assert candidate([[5, 4], [6, 8]], [[3, 4], [10, 8]], [[1, 1], [1, 1]]) == 24
    assert candidate([[10, 15], [20, 25]], [[12, 16], [18, 20]], [[1, 1], [1, 1]]) == 55
    assert candidate([[3, 6, 3], [5, 2, 5], [6, 1, 8]], [[4, 5, 6], [5, 3, 4], [3, 5, 6]], [[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == -1
    assert candidate([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 0, 0], [0, 0, 0], [0, 0, 1]]) == -1
    assert candidate([[5, 5], [5, 5]], [[3, 4], [4, 3]], [[1, 1], [1, 1]]) == 20

```

## Entry Point

`energy_paths`

