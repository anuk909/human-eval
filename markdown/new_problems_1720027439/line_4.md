# Task ID: hard/3

## Topics

['Minimum Spanning Tree', 'Edmonds-Karp Algorithm']

## Cover Story

['underwater', 'medieval castle']

## Prompt

```python
def coral_castle_reconstruction(plan_map, threshold):
    """
    In a medieval underwater world, an ancient castle known as the 'Coral Castle' has been devastated by a monstrous sea creature. The castle consists of rooms connected by corridors, each with a security level. The king wishes to rebuild the castle by reconnecting all the rooms with the minimum security risk, adhering to a constraint that no corridor's security level exceeds a given threshold due to the potential risk of future attacks.

    The historical data and architecture of Coral Castle are stored in a grayscale 'plan_map' where each pixel represents potential corridors and rooms. The intensity of a pixel indicates the security level of that potential corridor:
    - A higher intensity indicates a greater security risk.
    - Intensities lower or equal to the threshold are considered feasible corridors.

    - Rooms are represented as clusters of 0-intensity pixels surrounded by feasible corridors.
    - The objective is to rebuild the castle by establishing the minimum spanning tree (MST) of feasible corridors, ensuring all rooms are connected without any standalone components.

    This function assumes 4-connectivity (a pixel is connected to its four orthogonal neighboring pixels) for corridors, despite the 8-connectivity used for determining neighboring rooms or areas through all eight surrounding pixels.

    Implement a function that takes 'plan_map' (as a 2D list representing grayscale intensities), and a 'threshold' as inputs, and returns the total security risk (sum of the selected corridors' intensities) of the rebuilt minimum spanning tree or returns -1 if it's not feasible to connect all rooms in a single component.

    Note:
    - All input intensities are non-negative integers.
    """

```

## Cleaned Prompt

```python
Given a 2D list of grayscale intensities representing a map and a threshold, create a function that calculates the minimum spanning tree of feasible corridors (where feasible corridors are defined by having an intensity less than or equal to the threshold). Each room is marked as a pixel with intensity 0 surrounded by feasible corridors. Calculate the total risk (sum of intensities) of the minimum spanning tree connecting all rooms without exceeding the threshold, or return -1 if it's not possible.
```

## Warnings

- Solution failed correctness check.
- 4, Ambiguity in connection between feasible corridors and rooms: The problem dictates that rooms are clusters of 0-intensity pixels and that corridors are pixels with intensities less than or equal to a threshold. However, the problem does not specify how corridors (with intensity greater than 0) connect to the rooms directly, leading to potential discrepancies in understanding how corridors contribute to the Minimum Spanning Tree (MST) around these rooms.
- 5, No precise criteria for hallway determination: It is unclear how feasible corridors are identified and utilized to connect rooms when they exist on the edge or among higher-intensity pixels that exceed the threshold. This lack of clarity can result in different interpretations and implementations of the algorithm to determine connected components.
- 5, No definition for unreachable rooms scenario: The prompt does not distinctly explain whether the entire region of connected zero-intensity pixels (rooms) should be reachable from other similar regions to satisfy the condition of a 'connected' ensemble suitable for an MST. There could be situations where rooms are completely isolated by high-intensity corridors, rendering them unreachable under the stated conditions. Hence, further guidance is necessary to handle this case programmatically.

## Canonical Solution

```python
    import heapq
    def find(parent, i):
        if parent[i] == i:
            return i
        else:
            return find(parent, parent[i])

    def union(parent, rank, x, y):
        xroot = find(parent, x)
        yroot = find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def rebuilt_castle(plan_map, threshold):
        rows, cols = len(plan_map), len(plan_map[0])
        edges = []
        node_id = {}
        node_count = 0
        for r in range(rows):
            for c in range(cols):
                if plan_map[r][c] <= threshold:
                    node_id[(r, c)] = node_count
                    node_count += 1
                    if r > 0 and plan_map[r - 1][c] <= threshold:
                        edges.append((plan_map[r][c] + plan_map[r - 1][c], node_id[(r, c)], node_id[(r - 1, c)]))
                    if c > 0 and plan_map[r][c - 1] <= threshold:
                        edges.append((plan_map[r][c] + plan_map[r][c - 1], node_id[(r, c)], node_id[(r, c - 1)]))
        edges.sort()
        parent = list(range(node_count))
        rank = [0] * node_count
        result = 0
        for edge in edges:
            weight, u, v = edge
            if find(parent, u) != find(parent, v):
                union(parent, rank, u, v)
                result += weight
        if not all(find(parent, i) == find(parent, 0) for i in range(node_count)):
            return -1
        return result // 2
```

## Test Cases

```python
def check(candidate):
    assert candidate([[0, 10, 0], [10, 0, 10], [0, 10, 0]], 10) == 30
    assert candidate([[0, 255, 0], [10, 0, 255], [0, 10, 0]], 10) == -1
    assert candidate([[0, 10, 0], [10, 0, 10], [0, 10, 0]], 5) == -1
    assert candidate([[0, 5, 0], [5, 0, 5], [0, 5, 0]], 5) == 20
    assert candidate([[0, 8, 0], [8, 0, 8], [0, 8, 0], [8, 0, 8], [0, 8, 0]], 8) == 56
```

## Entry Point

`coral_castle_reconstruction`

