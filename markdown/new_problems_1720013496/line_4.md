# Task ID: hard/5

## Topics

['Heavy-Light Decomposition', 'Line Sweep']

## Cover Story

['magic wand', 'sneaky shadows']

## Prompt

```python
def shadow_casts(wand_directions, shadow_starts, shadow_ends):
    """
    In the mystical world of Codelandia, there is a Magic Wand that can cast shadows by swinging in various directions. Every direction can be represented on a Cartesian plane as a straight line segment, given by its starting coordinates and ending coordinates. A shadow is cast when two or more wand direction lines intersect, creating a shadowed area, starting from the leftmost point to the rightmost point of the intersection.

    You are given lists containing the starting and ending points of multiple wand directions. Calculate the total length of unique shadows cast on the x-axis, assuming the shadows are projected downwards. Note that if multiple shadow regions overlap, they count as a single continuous shadow.

    Wand directions are provided as lists of tuples, where each tuple contains two pairs defining the start and end coordinates of a line segment (e.g., (x1, y1, x2, y2)).

    Implement a line sweep algorithm to efficiently compute the unique shadow projection on the x-axis.

    Note:
    - The wand lines can intersect at any point, and intersections may form shadow regions due to overlaps.
    - Coordinates are in integer values and can be positive or negative.

    Example:
    - shadow_casts([(0, 0, 10, 10), (5, 5, 15, 15)], [(0, 0), (5, 10)]) should return 15 because the unique shadow cast from these directions spans from x = 0 to x = 15.
    """
```

## Cleaned Prompt

```python
Define a function that takes a list of wand directions, each described by starting and ending coordinates, and computes the total length of distinct shadow spans projected on the x-axis resulting from intersections of these directions.
```

## Canonical Solution

```python
    from collections import defaultdict

    def line_intersection(line1, line2):
        x1, y1, x2, y2 = line1
        x3, y3, x4, y4 = line2
        # Calculate determinant
        det = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
        if det == 0:
            return None  # Lines are parallel
        t = ((x3 - x1) * (y4 - y3) - (y3 - y1) * (x4 - x3)) / det
        u = ((x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)) / det
        if 0 <= t <= 1 and 0 <= u <= 1:  # Check if intersection is within the segments
            intersect_x = x1 + t * (x2 - x1)
            return intersect_x
        return None

    def shadow_casts(wand_directions, shadow_starts, shadow_ends):
        shadow_points = []
        # Find all intersections
        for i in range(len(wand_directions)):
            for j in range(i + 1, len(wand_directions)):
                intersect_x = line_intersection(wand_directions[i], wand_directions[j])
                if intersect_x is not None:
                    shadow_points.append(intersect_x)
        # Add in the starting and ending points as relevant shadow points
        shadow_points.extend(x for x, _ in shadow_starts)
        shadow_points.extend(x for x, _ in shadow_ends)
        # Calculate unique shadow coverage
        shadow_points = sorted(set(shadow_points))
        total_shadow = 0
        for i in range(1, len(shadow_points)):
            total_shadow += shadow_points[i] - shadow_points[i-1]
        return total_shadow
```

## Test Cases

```python
def check(candidate):
    assert candidate([(0, 0, 10, 10), (5, 5, 15, 15)], [(0, 0), (5, 10)]) == 15
    assert candidate([(1, 1, 4, 4), (2, 2, 6, 6), (3, 0, 3, 5)], [(2, 2), (3, 3)]) == 4
    assert candidate([(0, 1, 0, 6), (1, 1, 1, 6)], [(0, 0), (1, 1)]) == 1
    assert candidate([(-5, -5, 0, 0), (0, 0, 5, 5), (-2, 3, 2, -1)], [(-5, -5), (5, 5)]) == 10
    assert candidate([(-10, -10, -5, -5), (-3, 0, 2, -5)], [(-10, -10), (-3, 0)]) == 9
```

## Entry Point

`shadow_casts`

## Warnings

- Solution failed correctness check.
- 4, Problem Specification Mismatch: The function signature in the prompt `shadow_casts(wand_directions, shadow_starts, shadow_ends)` and the provided canonical solution with the same function name inconsistently handle `shadow_starts` and `shadow_ends`. The problem description does not explicitly mention the use of `shadow_starts` and `shadow_ends` in determining shadow length based on line intersections. The canonical solution combines intersections with these points arbitrarily without justification or explanation in the description, possibly confusing the purpose and mechanics of how shadows are treated.
- 4, Insufficient Explanation of Terms: The description does not sufficiently clarify how the shadow projection is calculated from the intersections of the line segments on the Cartesian plane. Terms like "shadow regions" and how they overlap or are projected to result in a "unique shadow projection on the x-axis" require more explicit detailed explanation to avoid ambiguity and ensure that the problem is understood correctly.

