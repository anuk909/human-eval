# Task ID: hard/1

## Topics

Floyd-Warshall Algorithm, KMP Algorithm

## Cover Story

['haunted house', 'enchanted mirror']

## Prompt

```python
def enchanted_mirror_paths(house_map, queries):
    """
    In a haunted house, there are rooms connected by enchanted mirrors that allow you to travel between them in only one direction. However, due to the spell on these mirrors, the travel times between rooms can sometimes change unexpectedly. You are given a map of the house in the form of a matrix where house_map[i][j] represents the current travel time from room i to room j. If house_map[i][j] is 0 (where i != j), it means there is no direct path from i to j.

    Implement a function to answer several queries where you must determine the shortest possible time to travel from a starting room to a destination room after considering all possible paths. Use the Floyd-Warshall algorithm to find the shortest path between any two points before evaluating the queries. Each query is a tuple of the form (start, end).

    Note:
    - The house_map matrix is square and the diagonal elements (house_map[i][i]) are always 0 as they represent the travel time from a room to itself which is trivially 0.
    - Ensure to re-check the shortest paths each time because the queries arrive after updating the house map.
    - Return a list of results corresponding to the minimal travel times for each query.
    - Assume there are no negative cycles.
    """
```

## Cleaned Prompt

```python
def enchanted_mirror_paths(house_map, queries):
    """
    You are given an adjacency matrix 'house_map' where house_map[i][j] represents the travel time from room i to room j. Implement a function to process several queries to determine the shortest travel time from a starting room to a target room using the Floyd-Warshall algorithm. Each query is of form (start, end). Handle the possibility of travel time updates.
    """
```

## Canonical Solution

```python
    def floyd_warshall(house_map):
        n = len(house_map)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if house_map[i][k] > 0 and house_map[k][j] > 0:
                        new_distance = house_map[i][k] + house_map[k][j]
                        if house_map[i][j] == 0 or new_distance < house_map[i][j]:
                            house_map[i][j] = new_distance

    def enchanted_mirror_paths(house_map, queries):
        floyd_warshall(house_map)
        results = []
        for start, end in queries:
            results.append(house_map[start][end])
        return results
```

## Test Cases

```python
def check(candidate):
    house_map1 = [
        [0, 3, 0, 0],
        [0, 0, 5, 0],
        [0, 0, 0, 2],
        [4, 0, 0, 0]
    ]
    queries1 = [(0, 2), (3, 2), (1, 3)]
    assert candidate(house_map1, queries1) == [7, 0, 0]

    house_map2 = [
        [0, 1, 2, 0],
        [0, 0, 3, 0],
        [0, 0, 0, 4],
        [0, 0, 0, 0]
    ]
    queries2 = [(0, 3), (1, 3), (0, 1)]
    assert candidate(house_map2, queries2) == [6, 0, 1]
```

## Entry Point

`enchanted_mirror_paths`

## Reason

```
Fewer than 5 test cases.
```

