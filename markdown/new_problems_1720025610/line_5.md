# Task ID: hard/5

## Topics

['Database', 'Geometry']

## Cover Story

['floating island', 'wizards']

## Prompt

```python
def locate_gems(map_image, queries):
    """
    Imagine a magical world filled with floating islands where wizards diligently practice their arcane arts. Each of these floating islands contains precious magic gems, essential for spell casting, embedded within the land. However, the exact locations of these gems are often shrouded in mystery, concealed within ancient map images portrayed as a 2D matrix.

    Your task is to assist wizards by creating a function that discovers all valid areas containing gems based on specific queries. Each query defines criteria for gem groupings that must be explored: a maximum search area ('max_search_area') and a minimum number of gems ('min_gems_count'). The function should analyze the map, a 2D matrix of 0s and 1s (where 0 signifies an empty spot and 1 indicates a gem), and identify all regions where the size of the contiguous group of gems is strictly smaller than 'max_search_area' and contains at least 'min_gems_count' gems. Your function must return a list of lists, where each inner list contains the coordinates (row, column) of gems for every valid area found, corresponding to each query.

    For detecting regions, implement a flood-fill algorithm considering 8-connectivity (gems are connected vertically, horizontally, or diagonally).

    Example:
    map_image = [[0, 1, 0, 0],[0, 1, 1, 0],[0, 0, 1, 0],[1, 0, 0, 0]]
    queries = [(5, 3), (4, 2)]
    output should be [[[0, 1], [1, 1], [1, 2], [2, 2]], [[0, 1], [1, 1]]]

    """
```

## Cleaned Prompt

```python
def locate_gems(map_image, queries):
    """
    The function should process a 2D map image consisting of '0's (empty) and '1's (gems), returning regions of contiguous gems that match each query's criteria for maximum area and minimum gem count. Implement flood-fill for region finding, considering 8-connectivity of gems.
    """
```

## Warnings

- Only 4 test cases found. Minimum recommended is 5.
- Solution failed correctness check.

## Canonical Solution

```python
def locate_gems(map_image, queries):
    def is_within_bounds(x, y):
        return 0 <= x < len(map_image) and 0 <= y < len(map_image[0])

    def search_area(x, y, visited):
        stack = [(x, y)]
        area = []
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            area.append([cx, cy])
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = cx + dx, cy + dy
                    if is_within_bounds(nx, ny) and map_image[nx][ny] == 1 and (nx, ny) not in visited:
                        stack.append((nx, ny))
        return area

    results = []
    for max_area, min_gems in queries:
        valid_areas = []
        visited = set()
        for x in range(len(map_image)):
            for y in range(len(map_image[0])):
                if map_image[x][y] == 1 and (x, y) not in visited:
                    area = search_area(x, y, visited)
                    if min_gems <= len(area) < max_area:
                        valid_areas.append(area)
        results.append(valid_areas)
    return results
```

## Test Cases

```python
def check(candidate):
    map_image1 = [[0, 1, 0, 0],[0, 1, 1, 0],[0, 0, 1, 0],[1, 0, 0, 0]]
    queries1 = [(5, 3), (4, 2)]
    assert candidate(map_image1, queries1) == [[[0, 1], [1, 1], [1, 2], [2, 2]], [[0, 1], [1, 1]]]

    map_image2 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    queries2 = [(9, 5), (5, 4)]
    assert candidate(map_image2, queries2) == [[], []]

    map_image3 = [[0]]
    queries3 = [(1, 1)]
    assert candidate(map_image3, queries3) == [[]]

    map_image4 = [[1, 1, 1, 0], [1, 0, 0, 1], [0, 0, 1, 1]]
    queries4 = [(6, 2)]
    assert candidate(map_image4, queries4) == [[[0, 0], [0, 1], [0, 2], [1, 0]]]
```

## Entry Point

`locate_gems`

