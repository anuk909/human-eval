# Task ID: hard/1

## Topics

['Jarvis March', 'Recursion']

## Cover Story

['portal', 'mountains']

## Prompt

```python
def find_visible_portals(coordinates):
    """
    In a 2D representation of a fantasy world, 'portals' are special points located at different coordinates (x, y) on a plane. These portals are on various mountains. Assume the 'viewing point' is located directly above the highest mountain's peak, which is the point with the highest y-value in the given coordinates. From this elevated position, you can only see the portals that are on the outer edge or boundary forming the convex shape of the terrain profile when viewed from above.

    Implement a recursive version of Jarvis's March algorithm to calculate the convex hull of the portal points. The convex hull represents the boundary or outline of the set of points when viewed from the highest portal's perspective, showing which portals are potentially visible. Note that while Jarvis's March algorithm is inherently iterative, this recursive implementation adds an additional challenge.

    Example:
    Input: coordinates = [(0,0), (4,4), (1,1), (3,1), (2,2)]
    Output: [(4,4), (3,1), (0,0)]
    Explanation: The highest mountain's peak is at (4,4), and the visible portals forming the convex hull in a clockwise order when viewed from this point are (4,4), (3,1), and (0,0).

    Notes:
    - Duplicate coordinates are considered a single location.
    - Input list of coordinates is non-empty.
    - Due to recursive implementation challenges, your solution needs careful consideration of stack depth and efficiency.
    """
```

## Cleaned Prompt

```python
def find_visible_portals(coordinates):
    """
    Given the coordinates of portals on a 2D plane in a list of tuples, calculate the convex hull of these points visible from the highest y-coordinate using Jarvis's March (Gift Wrapping) algorithm implemented recursively.

    Example:
    Input: coordinates = [(0,0), (4,4), (1,1), (3,1), (2,2)]
    Output: [(4,4), (3,1), (0,0)]
    """
```

## Warnings

- Solution failed correctness check.
- 4, Incorrect Problem Statement Logic: The problem prompt assumes that the viewing point being directly above the highest mountain's peak only allows visibility to portals on the convex hull. However, logically, an elevated viewing point should enable visibility to all portals, not just those on the convex hull. The convex hull algorithm actually identifies the minimal bounding polyline, which does not necessarily align with the visibility from an elevated point. This fundamental flaw in logic renders the problem's intent misleading about what is considered "visible."
- 4, Recursive Jarvis's March Complexity: The task mandates implementing Jarvis's March algorithm for convex hull calculation in a recursive manner. However, Jarvis's March inherently involves a sequence of iterative steps to select hull points, making this an overly complex and unnatural application for recursion. This requirement tends to lead to inefficient solutions prone to exceed stack depth for reasonably sized datasets, making the problem extremely complex and potentially unsolvable under typical recursive depth constraints.

## Canonical Solution

```python
    def find_visible_portals(coordinates):
        def orientation(p, q, r):
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        def next_portal(portals, current):
            right_most = portals[0]
            for portal in portals[1:]:
                if orientation(current, right_most, portal) < 0:
                    right_most = portal
            return right_most

        def recursive_convex_hull(portals, current, hull):
            next_pt = next_portal(portals, current)
            if next_pt not in hull:
                hull.append(next_pt)
                recursive_convex_hull(portals, next_pt, hull)

        highest_portal = max(coordinates, key=lambda p: p[1])
        hull = [highest_portal]
        recursive_convex_hull(coordinates, highest_portal, hull)
        return hull
```

## Test Cases

```python
def check(candidate):
    assert candidate([(0,0), (4,4), (1,1), (3,1), (2,2)]) == [(4,4), (3,1), (0,0)]
    assert candidate([(0,0), (2,3), (1,1), (3,0), (4,5)]) == [(4,5), (3,0), (0,0)]
    assert candidate([(1,2), (2,4), (5,2)]) == [(2,4), (5,2), (1,2)]
    assert candidate([(0,3), (1,1), (2,2), (3,1), (4,3)]) == [(4,3), (0,3)]
    assert candidate([(0,0), (1,3), (2,1), (3,5), (4,2)]) == [(3,5), (1,3), (0,0)]
```

## Entry Point

`find_visible_portals`

