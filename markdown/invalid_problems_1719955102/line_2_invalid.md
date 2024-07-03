# Task ID: hard/1

## Topics

Aho-Corasick Automaton, Monotonic Stack

## Cover Story

['time travel', 'airplane']

## Prompt

```python
def flight_safety_protocol(routes, reports):
    """
    As a time-traveling air traffic controller, you need to manage overlapping flight routes across multiple timelines. Two airplanes ‘overlap’ in flight if their routes cross at the same time. The input is given as a list of routes and a collection of reports where each airplane route is tagged with a unique identifier. Your task is to detect all overlaps given specific reports in real-time as quickly as possible using a hybrid approach with Aho-Corasick Automaton and Monotonic Stack.

    Each route in 'routes' list is a tuple in format (id, start_time, end_time, path) where 'path' is a string representing the flight path. Each 'report' in 'reports' list is a tuple in format (id, timestamp), querying for overlaps of the airplane at a given timestamp.

    Return the results as a dictionary where each key is a report's timestamp and the value is a list of ids of airplanes that overlap with the airplane in the report at that timestamp.

    Example:
    routes = [(1, 0, 100, 'ABCD'), (2, 20, 70, 'BCDX'), (3, 50, 150, 'ABEF')]
    reports = [(1, 50), (2, 35)]
    output = { 50: [1, 3], 35: [1, 2] }

    Notes:
    - If there are no overlaps, return an empty list for that timestamp.
    - Ensure the implementation is efficient for real-time response.
    """
```

## Cleaned Prompt

```python
def flight_safety_protocol(routes, reports):
    """
    Given a list of flight routes and a collection of reports, identify all overlaps for each report using a hybrid approach with Aho-Corasick Automaton and Monotonic Stack.

    Each route is a tuple (id, start_time, end_time, path), and each report is a tuple (id, timestamp).

    Return a dictionary with report timestamps as keys and lists of ids of overlapping routes as values.
    """
```

## Canonical Solution

```python
    def build_aho_corasick(paths):
        from collections import defaultdict
        automaton = defaultdict(dict)
        for path in paths:
            current = automaton
            for char in path:
                current = current.setdefault(char, {})
        return automaton

    def check_overlap(r1, r2, timestamp):
        if r1[1] <= timestamp <= r1[2] and r2[1] <= timestamp <= r2[2]:
            return True
        return False

    paths = {route[0]: route[3] for route in routes}
    time_segments = {route[0]: (route[1], route[2]) for route in routes}

    aho_automaton = build_aho_corasick(paths.values())
    results = {}
    for report in reports:
        overlaps = []
        querying_route = paths.get(report[0])
        for route_id, route_path in paths.items():
            if aho_automaton.search(querying_route, route_path) and check_overlap(time_segments[report[0]], time_segments[route_id], report[1]):
                overlaps.append(route_id)
        results[report[1]] = overlaps
    return results
```

## Test Cases

```python
def check(candidate):
    assert candidate([(1, 0, 100, 'ABCD'), (2, 20, 70, 'BCDX'), (3, 50, 150, 'ABEF')], [(1, 50), (2, 35)]) == {50: [1, 3], 35: [1, 2]}
    assert candidate([(1, 0, 100, 'ABCD'), (2, 80, 160, 'XYZ')], [(1, 90)]) == {90: []}
    assert candidate([(1, 0, 50, 'LOOP'), (2, 35, 85, 'LOOPX'), (3, 40, 60, 'LOOPY')], [(2, 40)]) == {40: [2, 3]}
    assert candidate([(4, 10, 20, 'XYZ'), (5, 15, 25, 'XYZ')], [(4, 18)]) == {18: [4, 5]}
    assert candidate([(6, 0, 100, 'NML'), (7, 0, 100, 'NMLK'), (8, 50, 150, 'NMLKJ')], [(7, 75)]) == {75: [6, 7, 8]}
```

## Entry Point

`flight_safety_protocol`

## Reason

```
Solution failed correctness check.
```

