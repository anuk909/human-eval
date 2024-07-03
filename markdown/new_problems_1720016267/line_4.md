# Task ID: hard/4

## Topics

['Minimum Spanning Tree', 'Centroid Decomposition']

## Cover Story

['gemstone mine', 'crystal ball']

## Prompt

```python
def gemstone_mine_layout(mine_layout):
    """
    You are an expert gemstone miner and you are planning the layout for a new mine. The mine layout is represented as an undirected graph where each node is a possible gemstone deposit and each edge has a weight representing the cost to tunnel between two deposits.

    Your goal is to minimize the overall cost of connecting all deposits in such a way that there is a single connected component, whilst also ensuring that no part of the mine is overly difficult to reach in an emergency. You decide to use a two-phase approach:

    Phase 1: Use a Minimum Spanning Tree (MST) algorithm to connect all nodes with the minimal total edge weight.
    Phase 2: Apply Centroid Decomposition to the MST to find a central deposit (or deposits) such that removing this deposit (or these deposits) will split the mine graph into components where each component has at most half the nodes of the original MST.

    The function should return the IDs of the centroid deposits found in the second phase after constructing the MST in the first phase.

    Input:
        mine_layout: List of tuples (u, v, w) representing the edges of the graph where u and v are node IDs (0-indexed) and w is the weight of the edge between u and v.

    Output:
        A list of the node IDs that are centroids after decomposing the MST.

    Constraints:
    - The graph is connected.
    - The graph may contain up to 10,000 nodes and 20,000 edges.

    Examples:
        - If the input graph forms a path like [(0, 1, 5), (1, 2, 3), (2, 3, 4)], the MST is the same as the input graph and the centroid is [2].
        - For a star shaped graph [(0, 1, 2), (0, 2, 2), (0, 3, 2)], the resulting MST is the same and the centroid is [0].
    """
```

## Cleaned Prompt

```python
Write a function that takes a list of edges of a connected undirected graph where each edge has a weight, and returns the centroids after: 1) Constructing a Minimum Spanning Tree; 2) Applying Centroid Decomposition to the MST.
```

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
        else :
            parent[yroot] = xroot
            rank[xroot] += 1

    def mst_kruskal(nodes, edges):
        result = []
        i, e = 0, 0
        edges = sorted(edges, key=lambda item: item[2])
        parent, rank = [], []
        for node in range(nodes):
            parent.append(node)
            rank.append(0)
        while e < nodes - 1:
            u, v, w = edges[i]
            i = i + 1
            x = find(parent, u)
            y = find(parent, v)
            if x != y:
                e = e + 1
                result.append((u, v, w))
                union(parent, rank, x, y)
        return result

    def centroid_decomposition(tree, nodes):
        sub_size = [1] * nodes
        def dfs(node, parent):
            size = 1
            max_subtree = 0
            for neighbor in tree[node]:
                if neighbor != parent:
                    subtree_size = dfs(neighbor, node)
                    size += subtree_size
                    max_subtree = max(max_subtree, subtree_size)
            sub_size[node] = size
            return size
        root = 0
        dfs(root, -1)  # Arbitrary root for DFS
        min_subtree = nodes
        centroid = root
        for i in range(nodes):
            max_child_tree = max((sub_size[child] for child in tree[i] if sub_size[child] < sub_size[i]), default=0)
            largest_remainder = nodes - sub_size[i]
            if max(max_child_tree, largest_remainder) < min_subtree:
                min_subtree = max(max_child_tree, largest_remainder)
                centroid = i
        return [centroid]

    node_count = max(max(u, v) for u, v, w in mine_layout) + 1
    mst = mst_kruskal(node_count, mine_layout)
    tree = {i: [] for i in range(node_count)}
    for u, v, w in mst:
        tree[u].append(v)
        tree[v].append(u)
    centroids = centroid_decomposition(tree, node_count)
    return centroids
```

## Test Cases

```python
def check(candidate):
    assert candidate([(0, 1, 5), (1, 2, 3), (2, 3, 4)]) == [2]
    assert candidate([(0, 1, 2), (0, 2, 2), (0, 3, 2)]) == [0]
    assert candidate([(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 5, 5)]) == [3]
    assert candidate([(i, i+1, 1) for i in range(100)]) == [50, 51]
    assert candidate([(0, 2, 2), (0, 3, 2), (2, 3, 1), (2, 1, 1), (1, 3, 3)]) == [2]
```

## Entry Point

`gemstone_mine_layout`

## Warnings

- Solution failed correctness check.
- 5, Ambiguous Problem Definition: The problem statement does not specify whether the input graph could potentially contain cycles or self-loops, which could affect the construction of the Minimum Spanning Tree (MST).
- 5, Incomplete Canonical Solution: The provided canonical solution appears to assume that the centroid decomposition will always find one centroid, whereas, in practice, two centroids might be found for even-numbered nodes as seen in one of the test cases. The solution should generalize to handle multiple centroids, but it does not.
- 5, Incorrect Assumptions in Solution: The solution assumes a graph starting from node 0 to max ID, but the problem does not explicitly guarantee contiguous node IDs spanning from 0 to max ID. There could exist cases where nodes are non-contiguously numbered which the solution might not handle correctly.
- 5, Logical Error in Implementation: The centroid decomposition logic in the canonical solution might not function correctly for trees where the best centroid split involves a nuanced analysis of children and subtree sizes. The approach to find the centroid simplistically assumes only one pass of comparison will suffice.
- 5, Missing Edge Cases in Problem Statement: The problem statement and canonical solution don't discuss the expected behavior or output format clearly when there are multiple possible correct centroids, making it ambiguous how multiple solutions would be handled.

