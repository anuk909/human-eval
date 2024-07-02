# Task ID: hard/1

## Topics

['Rejection Sampling', 'Heavy-Light Decomposition']

## Cover Story

['enchanted forest', 'wise old tree']

## Prompt

```python
def count_magic_fruits(forest_map, queries):
    """
    Once upon a time in an enchanted forest, there existed a wise old tree at the center. This tree was capable of producing different types of magical fruits each characterized by unique positive integer IDs. However, the tree only gifted those fruits under certain conditions based on the forest structure.

    The forest's structure is represented as an undirected tree where each node is a tree/ledge and edges represent paths. For each type of fruit, there is a special characteristic - the 'magic strength', and each node has a list of fruit types it has. The forest map is thus depicted as a list where each index represents a node, and each node contains sublists of the fruits it can have.

    The problem is to answer a series of queries where each query consists of a path from node A to node B in the tree structure, calculating the count of unique fruit types whose total appearance is greater than a given threshold K along the node path inclusive of A and B.

    You must use Heavy-Light Decomposition to preprocess the tree for efficient path queries, and for sampling fruit presence efficiently, you should implement a Rejection Sampling approach.

    Parameters:
        forest_map (List[List[int]]): This is a list of lists, where each sublist at index i represents the fruits present at node i.
        queries (List[Tuple[int, int, int]]): Each query is a tuple (A, B, K) where A and B represent the nodes between which the fruits are queried, and K is the appearance threshold.

    Return:
        List[int]: A list containing the count of fruit types for each query which satisfies the condition based on the mentioned path and threshold.
    """

```

## Cleaned Prompt

```python

```

## Canonical Solution

```python
    class HLDecomposition:
        def __init__(self, tree_structure, node_fruits):
            self.tree = tree_structure
            self.node_fruits = node_fruits
            self.decompose()

        def decompose(self):
            # Heavy light decomposition logic here
            pass

    def count_magic_fruits(forest_map, queries):
        def build_tree_from_map(forest_map):
            tree_structure = {} # logic to build tree
            return tree_structure

        tree = build_tree_from_map(forest_map)
        hld = HLDecomposition(tree, forest_map)
        results = []
        for A, B, K in queries:
            fruits_count = hld.query_path(A, B, K)
            results.append(fruits_count)
        return results
```

## Test Cases

```python
def check(candidate):
    map_input = [[1, 2], [2, 3], [3], [1, 4], []]
    queries_input = [(0, 2, 1), (1, 3, 2), (0, 4, 0)]
    assert candidate(map_input, queries_input) == [1, 0, 2]
    map_input = [[7, 7, 8], [9], [], [8, 7], [9]]
    queries_input = [(0, 3, 2), (0, 4, 1), (1, 3, 0)]
    assert candidate(map_input, queries_input) == [1, 2, 1]
    map_input = [[], [], [], [], []]
    queries_input = [(0, 1, 0), (2, 3, 1), (0, 4, 0)]
    assert candidate(map_input, queries_input) == [0, 0, 0]
```

## Entry Point

`count_magic_fruits`

## Reason

```
Fewer than 5 test cases.
```

