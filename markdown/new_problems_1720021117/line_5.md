# Task ID: hard/1

## Topics

['Minimum Spanning Tree', 'Radix Sort', 'Union Find']

## Cover Story

['ancient civilization', 'dragons']

## Prompt

```python
def dragon_network(N, roads):
    """
    Long ago, there existed an ancient civilization consisting of N distinct islands. The inhabitants of these islands were dragon tamers. Each dragon can be used to traverse between two islands, creating a network of dragon-flown paths.
    The dragon paths are given as a list 'roads'. Each road is represented as a tuple (x, y, weight), where x and y are the indices of the islands connected by the road and weight is the cost of using that dragon path due to the dragon's energy consumption.

    Your task is to design an efficient network of dragons such that all islands are connected with the minimal possible energy cost using the dragons. In other words, find the Minimum Spanning Tree (MST) of this network.

    However, there is a complexity. The dragons are mysterious creatures and the roads between islands can only be traversed in a specific order, defined by the energy cost. You must use Radix Sort to sort the dragon paths based on their energy weights before determining the MST using the Union-Find algorithm.

    Input:
    - N: an integer representing the number of islands (1 <= N <= 10^4).
    - roads: a list of tuples where each tuple contains three integers (x, y, weight), representing the island indices (0 <= x, y < N) and the dragon's energy cost (0 <= weight <= 10^5).

    Output:
    Return the minimum cost of energy needed to connect all the islands.

    Example:
    - If N = 4 and roads = [(0, 1, 5), (1, 2, 4), (2, 3, 7), (0, 2, 6), (1, 3, 2)], then output should be 11 (minimum spanning tree will include edges with weights 2, 4, 5).

    Note:
    - If no MST can be formed (i.e., the islands can't be fully connected), return -1.
    """
    pass
```

## Cleaned Prompt

```python
Given an integer N representing number of islands and a list of tuples roads representing possible dragon paths between islands with their energy consumption cost, find the minimum cost of energy needed to connect all the islands using these paths. Sort the paths using Radix Sort on their energy cost and then apply the Union-Find algorithm to determine the Minimum Spanning Tree (MST) cost to connect all islands.
```

## Warnings

- Solution failed correctness check.
- 5, Unnecessary complexity: The requirement to use Radix Sort for sorting weights before constructing the MST adds an unnecessary complexity to the problem. Given that typical MST algorithms like Kruskal's naturally involve sorting and efficiently handle this with comparison-based sorts, insisting on Radix Sort does not provide any algorithmic or educational benefit, and might confuse participants about the best practices in choosing sorting algorithms based on data characteristics.
- 4, Incorrect edge case handling: The example test case "assert candidate(5, [(0, 1, 10), (1, 2, 20), (2, 3, 30), (3, 4, 40), (4, 0, 5)]) == 95" assumes a cycle including all nodes represents a valid MST, which it does (total weight = 105, not 95). However, this type of error in specifying correct outputs could lead to misconceptions about the properties of MSTs (an MST with 5 nodes should have 4 edges, not 5 as implied by the test case summing weights to 95).

## Canonical Solution

```python
    def dragon_network(N, roads):
        def radix_sort(arr):
            max_value = max(arr, key=lambda x: x[2])[2]
            exp = 1
            while max_value / exp > 1:
                count_sort(arr, exp)
                exp *= 10

        def count_sort(arr, exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10
            for i in range(n):
                index = arr[i][2] // exp
                count[index % 10] += 1
            for i in range(1, 10):
                count[i] += count[i - 1]
            i = n - 1
            while i >= 0:
                index = arr[i][2] // exp
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1
                i -= 1
            for i in range(n):
                arr[i] = output[i]

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

        radix_sort(roads)
        parent = list(range(N))
        rank = [0] * N
        result = 0
        e = 0
        i = 0
        while e < N - 1 and i < len(roads):
            (u, v, w) = roads[i]
            i = i + 1
            x = find(parent, u)
            y = find(parent, v)
            if x != y:
                e = e + 1
                result += w
                union(parent, rank, x, y)

        if e != N - 1:
            return -1
        return result
```

## Test Cases

```python
def check(candidate):
    assert candidate(4, [(0, 1, 5), (1, 2, 4), (2, 3, 7), (0, 2, 6), (1, 3, 2)]) == 11
    assert candidate(1, []) == 0
    assert candidate(2, [(0, 1, 1), (0, 1, 2)]) == 1
    assert candidate(3, [(0, 1, 100000), (1, 2, 50000)]) == -1
    assert candidate(5, [(0, 1, 10), (1, 2, 20), (2, 3, 30), (3, 4, 40), (4, 0, 5)]) == 95
    assert candidate(4, [(0, 1, 7), (1, 2, 8), (0, 2, 6)]) == -1
```

## Entry Point

`dragon_network`

