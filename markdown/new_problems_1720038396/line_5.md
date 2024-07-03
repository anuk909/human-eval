# Task ID: hard/2

## Topics

['Detect Cycle in Graph', 'Set Matrix Zeroes']

## Cover Story

["illusionist's theater", 'floating island']

## Prompt

```python
def set_the_stage(islands, bridges, illusions):
    """
    The world-renowned illusionist, Elandir, is setting up his next grand show on a collection of floating islands. Each island can be connected to others via magical bridges. Some islands contain powerful illusions that, when activated, alter the reality of directly connected islands via bridges.

    You're provided with three inputs:
      - 'islands': a list of integers representing the islands where each integer is unique.
      - 'bridges': a list of tuples where each tuple (i, j) represents a bidirectional magical bridge between island i and island j.
      - 'illusions': a list of tuples where each tuple (i, j) indicates that activating the illusion on island i should set all direct bridge-connected neighbor islands of island j to 0 in the adjacency matrix.

    Your task is to detect if there's a cycle in the bridge network and then apply the effects of the illusions using an adjacency matrix representation.

    Constraints:
      - islands are labeled from 1 to n (inclusive).
      - There are no multiple bridges between the same pair of islands and no self-loops.
      - Illusions only affect direct neighbor islands connected by a bridge and do not stack.

    The function should return a tuple containing a boolean indicating whether a cycle exists, and the updated adjacency matrix after illusions have been applied.

    Example:
    islands = [1, 2, 3]
    bridges = [(1, 2), (2, 3), (3, 1)]
    illusions = [(1, 3)]
    Output should be (True, [[0, 1, 0], [1, 0, 1], [1, 1, 0]])

    """

```

## Cleaned Prompt

```python
Create a function that takes in three parameters:
1. `islands`: a list of unique integers representing islands.
2. `bridges`: a list of tuples, each representing a bridge between two islands (i.e., (i, j) is a bridge between island i and j).
3. `illusions`: a list of tuples, each indicating an effect where activating an illusion on the source island sets the values of directly connected destination island to 0.
The function should first check if there's a cycle in the bridges and then apply the effects of the illusions using an adjacency matrix representation.
The function should return a boolean indicating the presence of a cycle and the final adjacency matrix after applying the illusions.
```

## Warnings

- Solution failed correctness check.
- 4, Inconsistent bridge application: The prompt suggests that bridges connect islands which would imply adjacency, but the example shows that the adjacency matrix values are not consistent. For instance, islands with no direct bridge connection are sometimes shown as connected in the matrix, which might be the result of inadequate explanation of how bridges apply to the matrix or a mistake in maintaining matrix consistency after applying illusions.
- 5, Weak problem constraints: The problem is missing constraints on the ranges or limits for the number of islands, bridges, and illusions, as well as the specific nature of these bridges or illusions. This could lead to incorrect implementations if specific edge cases are not considered, like having bridges or illusions that could form self-loops or multiple bridges between the same pair of islands.
- 4, Ambiguous adjacency matrix update for illusions: The mechanism to update the adjacency matrix based on illusions is ambiguous. The example provided in the documentation implies a global update (all values of an island are set to zero), which conflicts with earlier parts of the description suggesting only directly connected islands should be affected. This can lead to confusion on the correct behavior of this feature.

## Canonical Solution

```python
def set_the_stage(islands, bridges, illusions):
    import collections
    def detect_cycle(n, adj):
        visited = set()
        def dfs(v, parent):
            visited.add(v)
            for neighbor in adj[v]:
                if neighbor not in visited:
                    if dfs(neighbor, v):
                        return True
                elif neighbor != parent:
                    return True
            return False
        for i in range(1, n+1):
            if i not in visited and dfs(i, -1):
                return True
        return False

    def apply_illusions(n, adj, illusions):
        for source, target in illusions:
            direct_neighbors = [index for index, connected in enumerate(adj[target-1]) if connected == 1]
            for neighbor in direct_neighbors:
                adj[neighbor] = [0] * n

    n = len(islands)
    adj = [[0]*n for _ in range(n)]
    for i, j in bridges:
        adj[i-1][j-1] = 1
        adj[j-1][i-1] = 1
    cycle_exists = detect_cycle(n, adj)
    apply_illusions(n, adj, illusions)
    return (cycle_exists, adj)
```

## Test Cases

```python
def check(candidate):
    assert candidate([1, 2, 3], [(1, 2), (2, 3), (3, 1)], [(1, 3)]) == (True, [[0, 1, 0], [1, 0, 1], [1, 1, 0]])
    assert candidate([1, 2, 3, 4], [(1, 2), (2, 3), (3, 4)], []) == (False, [[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]])
    assert candidate([1, 2, 3, 4, 5], [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)], [(1, 3), (4, 2)]) == (True, [[0, 0, 0, 0, 1], [1, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 1], [1, 0, 0, 1, 0]])
    assert candidate([1, 2, 3, 4], [(1, 3), (3, 4), (2, 4), (4, 1)], [(2, 4)]) == (False, [[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 1], [1, 0, 1, 0]])
    assert candidate([1, 2, 3], [], []) == (False, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
```

## Entry Point

`set_the_stage`

