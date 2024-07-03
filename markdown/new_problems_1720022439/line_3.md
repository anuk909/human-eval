# Task ID: hard/1

## Topics

['Memoization', 'Maximum Flow Problem', "Kruskal's Algorithm"]

## Cover Story

['boat', 'enchanted garden']

## Prompt

```python
def enchanted_garden(grid, start, enchanted_trees):
    """
    You are on a quest as a Captain sailing on an enchanted lake represented by a 2D grid. Each cell in the grid can be a patch of water (0), your boat (1), or an enchanted tree (2). The grid dimensions are M x N and the grid values are input as a list of lists, where each inner list represents a row.

    Your goal is to plant magical seeds around each enchanted tree to protect your boat. For each enchanted tree, determine the amount of water cells (0) within a 1-cell radius (including diagonals). These spells are cumulative; for overlapping regions around multiple trees, each overlapping cell should count for each tree.

    Furthermore, once the magical seeds are planted, the entire area becomes protected, and your boat should navigate a safe path, prioritizing the shortest path to explore further on the lake. You are to find the maximum flow of protected paths (where your boat can sail safely) from the starting point 'start' (given in (row, col) format) to all other reachable water cells in the grid.

    - The grid is a rectangle, and you can navigate up, down, left, and right to adjacent water cells from your current position. Diagonal movement is not allowed.

    Requirements:
    - Firstly, compute how many spells need to be placed around each enchanted tree.
    - Secondly, use this protected area to update the grid marking the maximum flow of protected paths that can be taken from the starting point.

    - The enchanted trees are given in a list of tuples (row_index, col_index).

    Example:
    Grid: [[0,0,2],[1,0,0],[0,2,0]],
    Start: (1,0),
    Enchanted Trees: [(0,2), (2,1)]
    - Around (0,2), there are 3 water cells.
    - Around (2,1), there are 4 water cells.
    - Resulting in a grid where some regions now allow for 7 water cells of maximum flow.
    """

```

## Cleaned Prompt

```python
def enchanted_garden(grid, start, enchanted_trees):
    """
    You're a Captain an enchanted lake, represented by a 2D grid where you must plant magical seeds around each enchanted tree to protect your boat. Use the grid to compute the number of spells needed around each tree and then calculate the maximum flow of protected paths from your starting point to all water cells. 
    - The grid cells can be water (0), the boat (1), or enchanted trees (2).
    - The enchanted trees are given as a list of (row_index, col_index) tuples.
    - You can only navigate up, down, left, and right to adjacent water cells.
    """

```

## Warnings

- Solution failed correctness check.
- 5, Unclear Problem Definition: The problem description mixes two possibly unrelated tasks – calculating the number of spells around each tree and determining the maximum flow of protected paths for navigation. These tasks are not clearly linked in the problem statement, which can confuse participants about the exact requirements and how the tasks relate.
- 5, Confusing Output Specification: The output or expected result after the computation is not clearly defined. While it mentions planting seeds around enchanted trees and navigating a boat using maximum protected paths, it does not specify what exactly needs to be returned by the function – whether it is the number of water cells counted around trees, the grid after marking, or the value of maximum flow of paths.
- 4, Overlapping Regions Calculation Ambiguity: It is stated that overlapping regions around multiple trees should each count for cell overlaps. However, there is no clear explanation or formula on how these overlaps should impact the count or flow calculations, which might lead to differing implementations and results based on participant interpretation.
- 4, Inconsistent Grid Update Mechanism: The problem suggests that after computing spells around trees, the grid is updated to reflect protected paths. The mechanism and rules for this update are not specified, specifically how spell counts or protected regions affect the allowed pathways for the boat, leading to potential confusion in implementation.
- 5, Vague Start and Reachability Explanation: The starting point's role and how the boat’s navigation is affected by the grid’s state after placing spells are vaguely explained. The process or algorithmic requirement to determine the path and handle various grid conditions (e.g., obstructed paths, boundaries) are not clarified, which could lead to different understandings of pathfinding and reachability.
- 5, Test Case and Expected Results Mismatch: The example results provided in the test case code section do not squarely align with the description in the problem statement. There seems to be an assumption about how results are derived (e.g., cumulative effects of overlapping spells), but these assumptions are not documented or explained within the prompt.
- 5, Terms and Definitions Inconsistency: The canonical function and prompt mention a 'maximum flow' concept, typically a graph theory term, but then use it in a way that appears to equate it with simply the highest number of localized water cells around trees. This misuse or redefinition of established theoretical terms can lead to misunderstandings unless explicitly redefined in the context of the problem.

## Canonical Solution

```python
    def max_flow(grid, start, enchnted_trees):
        def is_valid(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        def neighbors(i, j):
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if is_valid(i+dy, j+dx):
                    yield i+dy, j+dx

        # Mark the protected area
        for tree in enchanted_trees:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    ni, nj = tree[0]+dy, tree[1]+dx
                    if is_valid(ni, nj) and grid[ni][nj] == 0:
                        grid[ni][nj] += 1

        # Implement Maximum Flow from the starting point with newly protected paths
        # BFS with capacity tracking
        import queue
        q = queue.Queue()
        q.put((start, float('inf')))
        max_flow = 0
        while not q.empty():
            curr, flow = q.get()
            max_flow = max(max_flow, flow)
            for n in neighbors(*curr):
                if grid[n[0]][n[1]] > 0:
                    q.put((n, min(flow, grid[n[0]][n[1]])))
        return max_flow
```

## Test Cases

```python
def check(candidate):
    assert candidate([[0,0,2],[1,0,0],[0,2,0]], (1,0), [(0,2), (2,1)]) == 7
    assert candidate([[0,2,0],[1,0,2],[0,0,0]], (0,0), [(0,1), (1,2)]) == 5
    assert candidate([[2,0,0],[0,0,0],[0,0,2]], (2,1), [(0,0), (2,2)]) == 3
    assert candidate([[0,2,2],[1,0,0],[0,0,0]], (1,1), [(0,1), (0,2)]) == 8
    assert candidate([[0,0,0],[2,1,2],[0,0,0]], (1,1), [(1,0), (1,2)]) == 8
```

## Entry Point

`enchanted_garden`

