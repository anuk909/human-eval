# Task ID: hard/2

## Topics

["Prim's Algorithm", 'Math']

## Cover Story

['mischievous fairies', 'bioluminescent ocean']

## Prompt

```python
def minimum_light_spanning_tree(points, connections, light_intensity):
    """
    There exists an enchanted bioluminescent ocean where mischievous fairies have placed luminous orbs to light their nighttime revels. Each orb has a distinct light intensity and can connect to certain other orbs. You need to ensure that all orbs are connected using the minimum number of connections while maximizing the overall light intensity.

    Each connection between two orbs, also has a 'cost' associated with it which represents the amount of magic needed to keep that connection active. The lower the cost, the better.

    Write a function that, given a list of points representing orbs, a list corresponding matrix of connections representing the cost to connect each pair of points (or float('inf') if they cannot be connected directly), and a list of light intensities of each orb, returns the maximum light intensity of the minimum spanning tree that connects all orbs using Prim's Algorithm.

    Constraints:
    - The number of orbs will be at least 1 and at most 1000.
    - Each entry in connections will be either a positive integer or float('inf').
    - Light intensity is represented as an integer.

    Example:
    points = ['A', 'B', 'C', 'D']
    connections = [
        [0, 10, float('inf'), 30],
        [10, 0, 50, float('inf')],
        [float('inf'), 50, 0, 20],
        [30, float('inf'), 20, 0]
    ]
    light_intensity = [5, 20, 15, 10]

    The required function would return 45 as the maximum light intensity of the minimum spanning tree which would consist of connections A-B, A-D, D-C with corresponding orbs of intensities 20, 10, and 15 respectively.
    """

```

## Cleaned Prompt

```python
Given a list of points (orbs), a corresponding matrix of connections representing the cost to connect each pair of points, and a list of light intensities of each orb, implement a function to return the maximum light intensity of the minimum spanning tree that connects all orbs using Prim's Algorithm.
```

## Canonical Solution

```python
    import heapq

    def maximum_intensity_orb_prims(connections, light_intensity):
        n = len(connections)
        max_intensity = [0] * n
        in_mst = [False] * n
        heap = [(0, 0)]  # Use light intensity instead of costs for Prim's to prioritize high light

        while heap:
            intensity, node = heapq.heappop(heap)
            if in_mst[node]:
                continue

            max_intensity[node] = intensity
            in_mst[node] = True

            for adj_node, cost in enumerate(connections[node]):
                if not in_mst[adj_node] and connections[node][adj_node] != float('inf'):
                    heapq.heappush(heap, (-light_intensity[adj_node], adj_node))

        return sum(light_intensity[i] for i, included in enumerate(in_mst) if included)

```

## Test Cases

```python
def check(candidate):
    assert candidate(['A', 'B', 'C', 'D'], [[0, 10, float('inf'), 30],[10, 0, 50, float('inf')],[float('inf'), 50, 0, 20], [30, float('inf'), 20, 0]], [5, 20, 15, 10]) == 45
    assert candidate(['W', 'X', 'Y', 'Z'], [[0, 1, float('inf'), float('inf')], [1, 0, 1, float('inf')], [float('inf'), 1, 0, 2], [float('inf'), float('inf'), 2, 0]], [3, 2, 8, 10]) == 18
    assert candidate(['A'], [[0]], [7]) == 7
    assert candidate(['A', 'B'], [[0, float('inf')], [float('inf'), 0]], [20, 10]) == 20
    assert candidate(['R', 'S'], [[0, 2], [2, 0]], [10, 15]) == 15
```

## Entry Point

`minimum_light_spanning_tree`

## Warnings

- Solution failed correctness check.
- 4, Incorrect Algorithm Description: The problem requirement is to find a spanning tree that minimizes the number of connections (i.e., uses the minimum spanning tree approach) while simultaneously maximizing the overall light intensity. However, Prim's algorithm as described in the problem statement and as it's typically used, focuses on minimizing the connection costs, not maximizing the attributes of the nodes (orbs in this case). The canonical solution provided applies Prim’s algorithm prioritizing high light intensity directly which doesn't ensure a minimum spanning tree based on connection costs. There needs to be a balance or a method to account both connection costs and light intensities to satisfy both conditions, which this setup fails to address clearly.

