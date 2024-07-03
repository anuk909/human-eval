# Task ID: hard/2

## Topics

['Brainteaser', "Graham's Scan", 'Hopcroft-Karp Algorithm']

## Cover Story

['floating island', 'sentient rocks']

## Prompt

```python
def map_floating_islands(rocks):
    """
    In an ancient world, there is a sky with floating islands made up of sentient rocks. Each rock on an island can only recognize and communicate with rocks on the same island. These rocks form polygonal islands when connected with the shortest line possible without intersecting with any other island. You are a part of a research team that wants to map out how these rocks cluster to form islands in a 2D plane.

    Given a list of rocks represented as tuples of x and y coordinates, implement the Graham's scan algorithm to compute the convex hull for each cluster of rocks forming these floating islands. You will also need to ensure that these convex hulls do not intersect with one another. Once convex hulls are formed, find a maximum matching of these islands with a minimum distance metric using the Hopcroft-Karp Algorithm.

    Example Input: [(0, 0), (3, 0), (0, 3), (3, 3), (1, 1), (2, 2), (4, 4)]
    Example Output: [[[0, 0], [3, 0], [3, 3], [0, 3]], [[1, 1], [2, 2], [4, 4]]]

    Notes:
    - Assume the input list may have duplicate coordinates.
    - You must prevent the convex hulls from intersecting with each other.
    - Apply the Graham's scan algorithm to find the convex hull for each cluster of rocks.
    - Then, use the Hopcroft-Karp algorithm to find effective matchings of the islands based on minimum distances.
    """

```

## Cleaned Prompt

```python
Given a list of coordinates, use the Graham's scan algorithm to calculate the convex hulls for clusters forming separate polygons. Ensure these polygons don't intersect. Then use the Hopcroft-Karp algorithm to determine a maximum matching between these polygons considering the minimum distance. Sample Input: [(0, 0), (3, 0), (0, 3), (3, 3), (1, 1), (2, 2), (4, 4)]. Sample Output: [[[0, 0], [3, 0], [3, 3], [0, 3]], [[1, 1], [2, 2], [4, 4]]]
```

## Warnings

- Solution failed correctness check.
- 4, Undefined_clusters: The problem statement does not clearly define how to cluster the rocks into separate islands, which is critical for forming the convex hulls. Without this information, implementing the Graham's scan algorithm becomes problematic as we cannot determine which points belong to which cluster.
- 5, Algorithm_intersection_handling: The prompt instructs to ensure that convex hulls do not intersect with each other, but does not provide a method or criteria for doing so. This is a significant omission because without it, forming non-intersecting convex hulls according to the problem's requirements is infeasible.

## Canonical Solution

```python
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    def graham_scan(points):
        points = sorted(set(points))
        if len(points) <= 1:
            return points

        lower = []
        for p in points:
            while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) != 2:
                lower.pop()
            lower.append(p)

        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) != 2:
                upper.pop()
            upper.append(p)

        return lower[:-1] + upper[:-1]

    # Further code for Hopcroft-Karp and constraint handling goes here
```

## Test Cases

```python
def check(candidate):
    assert candidate([(0, 0), (3, 0), (0, 3), (3, 3), (1, 1), (2, 2), (4, 4)]) == [[[0, 0], [3, 0], [3, 3], [0, 3]], [[1, 1], [2, 2], [4, 4]]]
    assert candidate([(1, 1), (3, 3), (5, 5)]) == [[[1, 1], [3, 3], [5, 5]]]
    assert candidate([(0, 0), (2, 0), (1, 3), (2, 2), (5, 1), (3, 4), (5, 0)]) == [[[0, 0], [5, 0], [2, 0], [5, 1], [3, 4], [1, 3]]]
    assert candidate([(1, 0), (0, 1), (2, 2), (3, 3), (4, 5), (1, 5), (0, 4)]) == [[[0, 1], [2, 2], [0, 4], [1, 5], [4, 5], [3, 3], [1, 0]]]
    assert candidate([(0, 0), (1, 1), (2, 1), (1, 0)]) == [[[0, 0], [2, 1], [1, 1], [1, 0]]]
```

## Entry Point

`map_floating_islands`

