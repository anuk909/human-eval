# Task ID: hard/2

## Topics

['Meeting Rooms', 'Counting Sort', 'Longest Palindromic Substring']

## Cover Story

['fairy tale', 'energy vortex']

## Prompt

```python
def plan_fairy_meetings(meetings):
    """
    In the enchanted forest, fairies need to attend a series of meetings to stabilize the energy vortexes. Each meeting is scheduled at a specific time and takes place in different parts of the forest. The meeting times are provided as a list of tuples, where each tuple consists of two integers representing the start and end times of a meeting (inclusive). However, the spatial-temporal constraints of the forest mean not all meetings can be attended consecutively due to overlapping times. 

    Your task is to write a function that returns the maximum number of non-overlapping meetings a single fairy can attend.

    For example:
    - If input is [(1, 3), (2, 5), (4, 6)], fairies can only attend the first and last meetings [1, 3] and [4, 6], so you should return 2.
    - For input [(1, 2), (3, 4), (5, 6)], fairies can attend all since there's no overlap, hence you should return 3.
    """

```

## Cleaned Prompt

```python
Write a function that returns the maximum number of non-overlapping meetings a single fairy can attend. The meeting times are provided as a list of tuples, where each tuple consists of two integers representing the start and end times of a meeting. Return the maximum number of meetings a single fairy can attend consecutively without overlapping.

Examples:
- For input [(1, 3), (2, 5), (4, 6)], output should be 2.
- For input [(1, 2), (3, 4), (5, 6)], output should be 3.
```

## Warnings

- Solution failed correctness check.
- 5, Ambiguous Definition: The problem statement is inconsistent about the inclusiveness of the meeting end times in the description versus the tests provided. The prompt states that the meeting times are inclusive, which would imply that a meeting ending at time t and another starting at time t should be considered overlapping. However, the given test cases and the solution example treat these as non-overlapping (e.g., [(5, 10), (10, 15)]) which should have been counted as overlapping as per the inclusive definition but counts as non-overlapping and returns 3.
- 4, Unclear Edge Cases: There's a lack of explicit handling or mention of what should be considered when there's contradictory meeting data such as negative time, zero or negative duration meetings, or extremely large values for start and end times. This may lead to incorrect implementations if edge cases are not considered.

## Canonical Solution

```python
def plan_fairy_meetings(meetings):
    if not meetings:
        return 0
    # Sort meetings by their end times
    meetings.sort(key=lambda x: x[1])
    # Initialize with the first meeting
    last_end_time = meetings[0][1]
    count = 1
    for start, end in meetings[1:]:
        if start > last_end_time:
            last_end_time = end
            count += 1
    return count
```

## Test Cases

```python
def check(candidate):
    assert candidate([(1, 3), (2, 5), (4, 6)]) == 2
    assert candidate([(1, 2), (3, 4), (5, 6)]) == 3
    assert candidate([(0, 1), (2, 3), (1, 2)]) == 3
    assert candidate([(10, 15), (16, 20), (21, 25)]) == 3
    assert candidate([(5, 10), (10, 15), (15, 20)]) == 3
    assert candidate([]) == 0
    assert candidate([(1, 3), (3, 5), (4, 6), (7, 10), (9, 11)]) == 3
    assert candidate([(5, 7), (6, 8), (9, 12)]) == 2
```

## Entry Point

`plan_fairy_meetings`

