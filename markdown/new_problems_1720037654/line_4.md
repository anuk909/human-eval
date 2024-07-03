# Task ID: hard/5

## Topics

['Matrix Chain Multiplication', 'Combinatorics']

## Cover Story

['car', 'treasure']

## Prompt

```python
def max_treasure_value(maps, distances):
    """
    A treasure hunter uses a car to traverse through a matrix map where each cell contains either a treasure value (as an integer) or is blocked (denoted by -1). Each individual map in the 'maps' list has its unique movement constraints defined in the 'distances' list, which denotes how far in terms of steps the hunter can move starting from the top-left corner of each respective map. The task is to calculate the maximum treasure value the hunter can collect from each map considering the movement restrictions.

    The hunter can move up, down, left, or right, but cannot pass through blocked cells and cannot move outside the boundaries of the map. If a distance in 'distances' is 0, this represents a scenario where the hunter cannot move from the initial position, and the treasure calculation for that map should return 0, even if the initial cell contains some treasure. Also, if the starting cell (top-left corner) is blocked (value of -1), the resulting treasure for that map should be 0 since no movement is possible.

    The solution must handle and return a list of maximum possible treasure values for each map considering the given constraints, without modifying the original map structure or values during computation.

    Each map in 'maps' will have the same size but they're not necessarily square. A sample map with a distance limit might look like this:
    Map Example: [[0,1,-1,3], [2,3,-1,1], [0,-1,-1,4]]
    Distance Limit: 5
    Expected Output: the maximum treasure found by traversing at most 5 cells starting from the non-blocked top left corner and considering blocked paths.

    Note:
    - -1 indicates a blockage in the map and is impassible.
    - Return 0 in cases where the start is blocked or no movement is allowed.
    - Each unique path up to the given distance limit should be considered to compute the maximum possible treasure from starting position without modifying the map.
    """

```

## Cleaned Prompt

```python
Write a function that, given a list of 2D matrix maps where each cell contains a treasure value or is blocked, and a corresponding list of maximum distances the treasure hunter can move from the top-left corner, returns the maximum treasure the hunter can gather from each map considering the movement limitations. A cell value of -1 indicates a blockage, and treasure collection starts with zero. If the start position is blocked, return zero treasure for that map.
```

## Warnings

- Solution failed correctness check.
- 5, Start position assumption: The problem assumes that the treasure hunter always starts from the top-left corner without checking if it is blocked. This assumption can make certain maps unusable and the corresponding test ineffective. For these cases, if the starting cell is blocked, it should directly return a treasure value of 0 without trying to explore the map.
- 4, Output for no movement allowed: The problem states that if no movement is allowed (distance limit is 0), the function appears to return the value of the treasure at the starting position if not blocked, rather than 0. This could lead to confusion, as no movement implies no treasure should be collected. The function needs to account for this, ensuring that a distance limit of 0 always returns 0 irrespective of the starting cell's treasure value.
- 4, Array boundary checks in solution: The provided candidate solution might modify the map matrix during exploration by setting the cell value to -1 temporarily. This alters the input matrix, which is generally undesirable as it might affect subsequent operations or tests. Additionally, this strategy could lead potentially to incorrect paths if calls overlap in recursive depth-first search due to altered cell values.

## Canonical Solution

```python
def max_treasure_value(maps, distances):
    def dfs(map, x, y, remaining_steps, current_value):
        if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]) or map[x][y] == -1 or remaining_steps < 0:
            return current_value
        result = max(dfs(map, x+1, y, remaining_steps - 1, current_value + map[x][y]),
                     dfs(map, x-1, y, remaining_steps - 1, current_value + map[x][y]),
                     dfs(map, x, y+1, remaining_steps - 1, current_value + map[x][y]),
                     dfs(map, x, y-1, remaining_steps - 1, current_value + map[x][y]))
        return result

    results = []
    for idx, map in enumerate(maps):
        if map[0][0] == -1 or distances[idx] == 0:
            results.append(0)
        else:
            results.append(dfs(map, 0, 0, distances[idx], 0))
    return results
```

## Test Cases

```python
def check(candidate):
    assert candidate([[[0,1,-1,3], [2,3,-1,1], [0,-1,-1,4]]], [5]) == [6]
    assert candidate([[[0,1,-1], [-1,3,1]]], [3]) == [4]  # can move right and then down
    assert candidate([[[0]]], [0]) == [0]  # no steps allowed, should return 0 even though it starts at a treasure
    assert candidate([[[0,-1,5], [2,3,-1], [4,-1,-1]]], [10]) == [9]  # can explore all non-blocked cells
    assert candidate([[[5, -1, 0], [-1, 2, 1], [-1, -1, 3]], [[1, -1, 4], [0, 3, -1], [2, -1, 0]]], [7, 3]) == [5, 0]  # Second case must return 0 due to a blocked start
```

## Entry Point

`max_treasure_value`

