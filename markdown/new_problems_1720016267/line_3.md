# Task ID: hard/5

## Topics

["Kosaraju's Algorithm", 'Binary Search']

## Cover Story

['time-bending clock', 'aliens']

## Prompt

```python
def time_bending_clock(edges, queries):
    """
    Imagine an alien civilization that uses a time-bending clock to manage interconnected times. Each temporal connection between two periods of time has an interval value which can increase or decrease as you move between them. These intervals and connections can be visualized as a directed graph where each vertex represents a period of time and each directed edge represents a connection with an interval value as its weight.

    You need to answer queries about the shortest paths in this 'time-bending clock'. However, not only are you interested in the minimum distance, but also in strengthening the connectivity between these time periods using the concept of Strongly Connected Components (SCC) and exploring if the source and target are in the same SCC before finding the shortest path.

    Tasks:
    1. Determine which vertices (time periods) belong to the same Strongly Connected Component using Kosaraju's algorithm.
    2. For each query, if the source and target vertices are in the same SCC, perform a Dijkstra's algorithm to find the shortest path. If they aren't in the same SCC or if there's no path, return -1.
    
    Each edge in the edges list is represented as (u, v, w), where u->v is a directed edge with weight w. 

    Queries is a list of tuples (src, trg), where you need to check if there's a path from src to trg and determine the shortest path if possible.

    Notes:
    - Assume the vertices are numbered from 0 to the maximum vertex found in the edges list.
    - Graph might not be fully connected.
    """
```

## Cleaned Prompt

```python
Write a function that processes a directed weighted graph to find the shortest paths for specified queries using Strongly Connected Components (SCC) separation and Dijkstra's shortest path algorithm. If source and target are not in the same SCC or no path exists, return -1.
```

## Canonical Solution

```python
    def time_bending_clock(edges, queries):
        from collections import defaultdict, deque
        import heapq

        def kosaraju(n, edges):
            graph = defaultdict(list)
            rgraph = defaultdict(list)
            for u, v, w in edges:
                graph[u].append((v, w))
                rgraph[v].append((u, w))

            order, visited = deque(), set()
            def dfs(v):
                visited.add(v)
                for nei, _ in graph[v]:
                    if nei not in visited:
                        dfs(nei)
                order.appendleft(v)

            for v in range(n):
                if v not in visited:
                    dfs(v)

            scc, visited = [], set()
            def rev_dfs(v, component):
                visited.add(v)
                component.append(v)
                for nei, _ in rgraph[v]:
                    if nei not in visited:
                        rev_dfs(nei, component)

            for v in order:
                if v not in visited:
                    component = []
                    rev_dfs(v, component)
                    scc.append(component)

            return scc

        def dijkstra(src, trg, graph):
            min_heap = [(0, src)]
            dist = {src: 0}
            while min_heap:
                d, node = heapq.heappop(min_heap)
                if node == trg:
                    return d
                for nei, weight in graph[node]:
                    if nei not in dist or dist[nei] > d + weight:
                        dist[nei] = d + weight
                        heapq.heappush(min_heap, (dist[nei], nei))
            return -1

        n = max(max(u, v) for u, v, _ in edges) + 1
        scc = kosaraju(n, edges)
        idx_map = {node: idx for idx, component in enumerate(scc) for node in component}
        graph = defaultdict(list)
        for u, v, w in edges:
            if idx_map[u] == idx_map[v]:
                graph[u].append((v, w))

        results = []
        for src, trg in queries:
            if idx_map[src] == idx_map[trg]:
                res = dijkstra(src, trg, graph)
                results.append(res)
            else:
                results.append(-1)
        return results
```

## Test Cases

```python
def check(candidate):
    assert candidate([(0, 1, 1), (1, 2, 2), (2, 0, 3)], [(0, 2), (2, 1)]) == [3, -1], 'Test case 1 failed'
    assert candidate([(0, 1, 5), (1, 2, 6), (2, 3, 7), (3, 1, 8)], [(0, 3), (3, 0)]) == [-1, -1], 'Test case 2 failed'
    assert candidate([(0, 1, 2), (1, 0, 3), (2, 3, 4), (3, 2, 5)], [(0, 1), (2, 3)]) == [2, 4], 'Test case 3 failed'
    assert candidate([(0, 1, 3), (1, 2, 4), (2, 3, 5), (3, 0, 1), (2, 1, 1)], [(0, 3), (1, 0)]) == [9, 2], 'Test case 4 failed'
    assert candidate([(0, 1, 1), (1, 2, 1), (0, 3, 5), (3, 2, 1), (2, 0, 10)], [(0, 2), (3, 0), (1, 3)]) == [2, 16, 6], 'Test case 5 failed'
```

## Entry Point

`time_bending_clock`

## Warnings

- Solution failed correctness check.
- 4, Problem Specification Inaccuracy: The problem description indicates the requirement of using Kosaraju's Algorithm explicitly, which is a specific method for finding Strongly Connected Components (SCC), but it does not specify how dealing with the graph's connectivity affects the shortest path calculations clearly. This may lead to ambiguities in implementing Dijkstra's algorithm regarding handling nodes that are not interconnected through SCCs.
- 4, Incorrect Algorithm Constraint: The canonical solution provided uses Dijkstra's algorithm for finding the shortest path. However, Dijkstra's algorithm is typically used for graphs with non-negative weights. Although the prompt doesn't explicitly mention negative weights, it includes terms like "increase or decrease," which might suggest interval adjustments that could be negative. This requires clarification, or an alternative approach like the Bellman-Ford algorithm should be suggested if negative weights are possible.

