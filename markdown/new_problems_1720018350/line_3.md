# Task ID: hard/3

## Topics

['Subsets', 'Reservoir Sampling', 'Tree']

## Cover Story

['urban jungle', 'cyber cafe']

## Prompt

```python
def cyber_cafe_analysis(max_capacity, logs):
    """
    In the bustling city of Neonopolis, a hybrid entertainment venue called 'CyberBrewCafe' is known for its urban jungle theme adorned with aesthetic digital trees. The cafe comprises different sections, each represented as a node in an undirected tree graph structure and halls as edges. Each node has a maximum capacity of attendees and logs are maintained to record visitors' timestamps and sections visited.

    The venue uses a special analysis to optimize visitor experience by estimating the average number of visitors per section over a time frame. However, due to constantly changing visitor patterns, they cannot store all past data but rather sample them using the Reservoir Sampling technique.

    Given the maximum capacities of each section (in a list where index represents the section/node) and a list of logs (each log is a tuple of timestamp, list of visited sections for that timestamp), implement a function to estimate the average occupancy rate across all sections for the given logs.

    Each section's occupancy rate is calculated as the average number of visitors during the observed timestamps, divided by the maximum capacity of the section.

    For example: If max_capacity is [10, 15, 20] and logs are [(1, [0, 1]), (2, [0, 1, 2]), (3, [2])], the estimated average occupancy rates would be approximately [0.20, 0.13, 0.10] respectively for each section considering each timestamp sees each section visited as one visitor unit.

    Note:
    - Sections' indices and logs must be valid. Assume a correct graph structure and valid logs.
    - Resulting occupancy rates should be a list of floats rounded to two decimal places.
    """

```

## Cleaned Prompt

```python
Given the maximum capacities of each cafe section and a list of logs (each log is a tuple of timestamp, list of visited sections), implement a function to estimate the average occupancy rate across all sections for the given logs. Each section's occupancy rate is calculated as the average number of visitors during the observed timestamps, divided by the maximum capacity of the section.
```

## Canonical Solution

```python
from collections import defaultdict

def cyber_cafe_analysis(max_capacity, logs):
    visitor_counts = defaultdict(int)
    timestamps_per_section = defaultdict(int)

    for _, sections_visited in logs:
        unique_sections = set(sections_visited)
        for section in unique_sections:
            visitor_counts[section] += 1

    for _, sections_visited in logs:
        for section in set(sections_visited):
            timestamps_per_section[section] += 1

    occupancy_rates = []
    for i, max_cap in enumerate(max_capacity):
        if i in timestamps_per_section:
            average = visitor_counts[i] / timestamps_per_section[i]
            occupancy_rate = round(average / max_cap, 2)
        else:
            occupancy_rate = 0.0
        occupancy_rates.append(occupancy_rate)

    return occupancy_rates
```

## Test Cases

```python
def check(candidate):
    assert candidate([10, 15, 20], [(1, [0, 1]), (2, [0, 1, 2]), (3, [2])]) == [0.67, 0.67, 0.50]
    assert candidate([10, 10, 10], [(1, [0, 1]), (5, [0, 2]), (7, [2])]) == [0.67, 0.33, 0.67]
    assert candidate([100, 150, 200], [(1, [0]), (2, [1]), (3, [0, 1, 2])]) == [0.67, 0.67, 0.33]
    assert candidate([5, 15, 25], []) == [0.0, 0.0, 0.0]
    assert candidate([1, 1, 1, 1], [(1, [0, 1, 2, 3]), (2, [0, 1, 2, 3]), (3, [0, 1, 2, 3])]) == [3.0, 3.0, 3.0, 3.0]
```

## Entry Point

`cyber_cafe_analysis`

## Warnings

- Solution failed correctness check.
- 5, Inconsistent problem description and example: The prompt describes the task as calculating the "average occupancy rate" but then provides incorrect calculations in the examples that do not match the described methodology. The examples calculate occupancy based on total visitor visits divided by the number of timestamps, and not the average number of visitors per section over time divided by the maximum capacity.
- 4, Misleading problem context with unnecessary details: The description of the cafe as a venue with an urban jungle theme and a tree graph structure is misleading and irrelevant to the solution of the problem. It suggests complexities related to graph theory which are not actually applied in the given solution, potentially confusing participants about the nature of the problem.

