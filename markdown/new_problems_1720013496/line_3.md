# Task ID: hard/2

## Topics

['Eulerian Circuit', 'Lowest Common Ancestor']

## Cover Story

['crystal ball', 'arctic']

## Prompt

```python
def arctic_crystal_path(magical_links, queries):
    """
    In the mystical land of Arcticopia, there exist a series of Magic Crystals connected by Magical Links. These Magic Crystals and their Magical Links form a unique magical network where every Magic Crystal (node) can be reached from any other through exactly one continuous path made of Magical Links (i.e., the network forms a Tree structure).

    A famous Arcticopian artifact is a Crystal Ball which has the power to show the path between any two Magic Crystals in the form of a Eulerian Circuit (a path visiting each Magical Link exactly once).

    Your job is to assist the Oracle of Arcticopia who uses the Crystal Ball, by calculating for each query the Lowest Common Ancestor (LCA) of two given Magic Crystals and also the length of the Basic Magical Path (the direct path between these two crystals not considering Eulerian circuit) between them.

    The network and queries will be specified as follows:
    - magical_links: A list of tuples where each tuple (u, v) specifies a Magical Link between Magic Crystals u and v.
    - queries: A list of pairs where each pair (u, v) specifies a query to find the LCA and the Basic Magical Path length between Magic Crystals u and v.

    The function will return a list of tuples, each containing (lca, path_length) for each query.

    Note:
    - Magic Crystals are numbered from 1 to the number of nodes and include all numbers in this range.
    - Treat the input links as undirected.
    - Ensure the function is optimized for multiple queries on possibly large-sized trees.
    """

```

## Cleaned Prompt

```python
Given a tree structure formed by nodes and edges, find the Lowest Common Ancestor (LCA) and the direct path length between given pairs of nodes.
```

## Canonical Solution

```python
    from collections import defaultdict, deque

    def build_tree(links):
        tree = defaultdict(list)
        for u, v in links:
            tree[u].append(v)
            tree[v].append(u)
        return tree

    def bfs_tree_properties(root, tree):
        depth = {root: 0}
        parent = {root: None}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            for neighbor in tree[node]:
                if neighbor not in depth:  # unvisited
                    depth[neighbor] = depth[node] + 1
                    parent[neighbor] = node
                    queue.append(neighbor)
        return parent, depth

    def lca(u, v, parent, depth):
        # Bring u and v to the same depth
        while depth[u] > depth[v]:
            u = parent[u]
        while depth[v] > depth[u]:
            v = parent[v]
        # Find the common ancestor
        while u != v:
            u = parent[u]
            v = parent[v]
        return u

    tree = build_tree(magical_links)
    parent, depth = bfs_tree_properties(1, tree)  # Assuming 1 is the root
    results = []
    for u, v in queries:
        common_ancestor = lca(u, v, parent, depth)
        path_length = depth[u] + depth[v] - 2 * depth[common_ancestor]
        results.append((common_ancestor, path_length))
    return results
```

## Test Cases

```python
def check(candidate):
    assert candidate([(1, 2), (1, 3), (2, 4), (2, 5)], [(4, 5), (4, 3)]) == [(2, 2), (1, 3)]
    assert candidate([(1, 2), (2, 3), (3, 4), (4, 5)], [(1, 5), (2, 4)]) == [(1, 4), (2, 2)]
    assert candidate([(1, 2), (1, 3)], [(2, 3)]) == [(1, 2)]
    assert candidate([(1, 2), (1, 3), (2, 4), (3, 5)], [(2, 5)]) == [(1, 3)]
    assert candidate([(1, 2), (2, 3), (3, 4)], [(1, 4)]) == [(1, 3)]
```

## Entry Point

`arctic_crystal_path`

## Warnings

- 4, Incorrect Problem Explanation: The problem prompt suggests that the solution should consider a Eulerian Circuit, which refers to a tour of a graph that visits every edge exactly once in a connected graph with all vertices of even degree. However, finding LCA or the Basic Magical Path between nodes does not require or involve a Eulerian Circuit as per the implemented solution and problem nature (tree-based). The mention of a Eulerian Circuit is misleading and irrelevant to the task of finding LCAs in trees.

