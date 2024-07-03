# Task ID: hard/5

## Topics

['Dynamic Programming', 'Minimum Path Sum', 'Topological Sort']

## Cover Story

['wizards', 'supernatural storm']

## Prompt

```python
def storm_escape_path(rooms, portals):
    """
    In a mystical land, a wizard resides in a complex of magical rooms connected by portals that form a directed acyclic graph (DAG). Each room is imbued with a storm's power which fluctuates in intensity. Unfortunately, a supernatural storm has become uncontrollable, and the wizard needs to seek shelter in the safest room (the room with minimal storm intensity).

    You are to help the wizard by determining the optimal path to the safest room with the minimum cumulative storm power intensity. This is akin to the minimum path sum problem on DAGs, using dynamic programming and topological sorting.

    The wizard's complex is described by:
    - rooms: a list of integers representing the storm power in each room.
    - portals: a list of tuples (a, b), representing a directed portal from room 'a' to room 'b'.

    The function should return the minimum cumulative storm power intensity the wizard must endure to reach the safest room starting from any room.

    Assume there are no cycles in the portals structure (the network forms a DAG).

    Example Input:
    rooms = [6, 10, 3, 1, 7]
    portals = [(0,1), (1,2), (2,3), (0,4), (4,3)]
    Output: 7 (Path: 0->4->3 with storm powers summing up to 6+1=7)

    Constraints:
    - Each room can have one or multiple escape paths, but the paths do not form cycles.

    Note:
    - The function should handle multiple starting points, and aim to calculate the safest pathway to the minimal storm room from any starting room.
    """
```

## Cleaned Prompt

```python
Write a function storm_escape_path(rooms, portals) that calculates the minimum cumulative storm power intensity to reach the room with the smallest storm power from any starting room in a directed acyclic graph (DAG) setting. Each room has a storm power (given as an integer), and portals represent directed connections between rooms. Use dynamic programming and topological sort to solve the problem efficiently.
```

## Warnings

- Solution failed correctness check.
- 4, Incorrect output format: The problem description states that the output should be the minimal cumulative storm power intensity that the wizard must endure to reach the safest room, which implies providing the result of the calculations directly. However, the provided example also specifies a path (0->4->3) with its cumulative power (6+1=7), making it ambiguous whether the function should return only the numerical sum or also include the path taken. This may confuse participants regarding what the expected output should be.

## Canonical Solution

```python
    def storm_escape_path(rooms, portals):
        from heapq import heappush, heappop
        import sys

        n = len(rooms)
        adj_list = [[] for _ in range(n)]
        for start, end in portals:
            adj_list[start].append(end)

        def topological_sort():
            in_degree = [0] * n
            for start, ends in enumerate(adj_list):
                for end in ends:
                    in_degree[end] += 1
            stack = [i for i in range(n) if in_degree[i] == 0]
            sorted_order = []
            while stack:
                node = stack.pop()
                sorted_order.append(node)
                for connected_node in adj_list[node]:
                    in_degree[connected_node] -= 1
                    if in_degree[connected_node] == 0:
                        stack.append(connected_node)
            return sorted_order

        sorted_rooms = topological_sort()
        dp = [sys.maxsize] * n
        for room in sorted_rooms:
            if not adj_list[room]:
                dp[room] = rooms[room]
            for next_room in adj_list[room]:
                dp[next_room] = min(dp[next_room], dp[room] + rooms[next_room])

        return min(dp)

```

## Test Cases

```python
def check(candidate):
    assert candidate([6, 10, 3, 1, 7], [(0,1), (1,2), (2,3), (0,4), (4,3)]) == 7
    assert candidate([5, 1, 3, 9, 2], [(0,1), (0,2), (1,3), (2,3), (2,4), (4,3)]) == 3
    assert candidate([1], []) == 1
    assert candidate([2, 8, 5, 1], [(0,1), (0,2), (1,3), (2,3)]) == 3
    assert candidate([3, 1, 10, 4, 7], [(0,1), (0,2), (1,3), (2,3), (3,4)]) == 8
```

## Entry Point

`storm_escape_path`

