# Task ID: hard/1

## Topics

Math, Prim's Algorithm

## Cover Story

['fairy tale', 'enchanted lab']

## Prompt

```python
def enchanted_connections(points, max_cost):
    """
    In a whimsical fairy tale land, imagine a lab populated with enchanted machines spread over a 2D space, represented as integer coordinates.
    The king wants to connect these machines with wires so that each machine can communicate with at least another, but he wishes to minimize the cost.
    The cost of connecting two machines located at points (x1, y1) and (x2, y2) is defined as the square of the Euclidean distance between them.

    Given a list of points coordinates where each point is a tuple (x, y) representing a machine, compute the minimum cost needed to connect all the machines such that no wire used exceed the max_cost. If it's impossible to meet the condition, return -1.

    The cost to connect machines (x1, y1) and (x2, y2) is given by (x1 - x2)**2 + (y1 - y2)**2.

    Note: Use Prim's algorithm effectively for a minimum spanning tree (MST) construction considering a max_cost constraint.
    """
```

## Cleaned Prompt

```python
def enchanted_connections(points, max_cost):
    """
    Given a list of points (x, y) on a 2D space, calculate the minimum cost to connect all points to form communication links where each point is linked to at least one other point. The connection cost between two points (x1, y1) and (x2, y2) is (x1 - x2)**2 + (y1 - y2)**2. Implement the solution to not exceed max_cost for any wire used. Use Prim's algorithm to find a minimal cost setup. Return the total cost or -1 if the configuration is not possible.
    """
```

## Canonical Solution

```python
        import heapq

        def square_distance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        def enchanted_connections(points, max_cost):
            if not points:
                return -1

            N = len(points)
            min_cost = 0
            in_mst = [False] * N
            min_edge = [(float('inf'), None) for _ in range(N)]
            min_edge[0] = (0, 0)
            min_heap = [(0, 0)]

            while min_heap:
                cost, u = heapq.heappop(min_heap)
                if in_mst[u]:
                    continue
                in_mst[u] = True
                min_cost += cost

                for v in range(N):
                    if not in_mst[v]:
                        edge_cost = square_distance(points[u], points[v])
                        if edge_cost <= max_cost and edge_cost < min_edge[v][0]:
                            min_edge[v] = (edge_cost, u)
                            heapq.heappush(min_heap, (edge_cost, v))

            if all(in_mst):
                return min_cost

            return -1
```

## Test Cases

```python
def check(candidate):
    assert candidate([(0, 0), (2, 2), (3, 5)], 25) == 29
    assert candidate([(0, 0)], 2) == 0
    assert candidate([(0, 0), (1, 1)], 1) == -1
    assert candidate([(0, 0), (2, 2), (4, 4)], 8) == 16
    assert candidate([(1, 1), (4, 4), (8, 8)], 20) == -1
    assert candidate([], 5) == -1
```

## Entry Point

`enchanted_connections`

## Reason

```
Solution failed correctness check.
```

