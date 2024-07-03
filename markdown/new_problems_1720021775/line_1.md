# Task ID: hard/3

## Topics

['Greedy', 'Monotonic Queue', 'Binary Search']

## Cover Story

['mysterious cave', 'train station']

## Prompt

```python
def train_schedule_optimization(arrival_times, departure_times):
    """
    In the world of Anachronia, a mysterious cave near the train station has been found to oscillate geological stability every hour causing different train platforms to be safe or unsafe.
    Every hour, the safety of the platforms switches, which necessitates optimization of train schedules.

    You are given two lists 'arrival_times' and 'departure_times' where each index corresponds to a particular train.
    The 'arrival_times' list gives the timestamp (in hours) each train arrives and the 'departure_times' gives the timestamp each train departs.

    To maximize safety and minimize the change on platforms, figure out the minimum number of platforms needed at the station such that no train needs to change its allocated platform due to the oscillating safety.

    The function should implement a greedy approach utilizing a monotonic queue to efficiently track the platforms and provide the minimum number needed based on the provided times.

    Example:
    - arrival_times = [2, 2, 3]
    - departure_times = [3, 4, 5]
    If these are the arrival and departure times for 3 different trains, the minimum number of platforms needed would be 2 (one train arrives at 2 and leaves at 3, the second arrives at 2 and leaves at 4, and the third arrives at 3 and leaves at 5).

    Note:
    - The timestamps in 'arrival_times' and 'departure_times' are integers representing the hours.
    - Both lists will have the same length and will be sorted in non-decreasing order.
    - The returned value should be an integer representing the number of platforms needed.
    """

```

## Cleaned Prompt

```python
Write a function `train_schedule_optimization` that takes two sorted lists 'arrival_times' and 'departure_times' where each index corresponds to a particular train which tells the time each train arrives and departures respectively. The function should return the minimum number of platforms needed at the station using a greedy approach and a monotonic queue to ensure that no train needs to change its allocated platform amid oscillating safety of platforms.
Example:
With arrival_times = [2, 2, 3] and departure_times = [3, 4, 5], the minimum number of platforms needed would be 2.
```

## Warnings

- Solution failed correctness check.
- 5, Undefined Behavior with Oscillating Platform Safety: The problem statement introduces the concept of 'oscillating geological stability' affecting platform safety but fails to specify how this oscillation impacts the minimum platform calculation or how often it switches in relation to train schedules. This leaves a critical aspect of the task ambiguous and could lead to various interpretations that do not align, making the problem unusable without further clarification.
- 5, Misleading Example: The example provided does not take into account the described oscillating safety of platforms, making it difficult to understand how exactly this should influence the algorithm or the logical considerations in minimizing platform changes. This inconsistency between the problem's narrative and the practical example poses a significant flaw as it fails to illustrate the complexity introduced by the 'oscillating safety' concept.
- 4, Unclear Algorithm Requirement: While the prompt suggests using a 'greedy approach utilizing a monotonic queue,' it doesn't clearly define how this structure should be effectively used within the context of the problem, especially considering the undefined impact of the oscillating safety. The lack of clear guidance on implementing the specified data structure in relation to the problem scenario may leave participants guessing and result in a variety of unintended solution approaches.

## Canonical Solution

```python
    from sortedcontainers import SortedList

    def train_schedule_optimization(arrival_times, departure_times):
        if not arrival_times:
            return 0
        platforms = SortedList()

        for i in range(len(arrival_times)):
            if platforms and platforms[0] < arrival_times[i]:
                platforms.pop(0)
            platforms.add(departure_times[i])
        return len(platforms)
```

## Test Cases

```python
def check(candidate):
    assert candidate([2, 2, 3], [3, 4, 5]) == 2
    assert candidate([1, 3, 5], [2, 4, 6]) == 1
    assert candidate([1, 1, 1], [2, 3, 4]) == 3
    assert candidate([], []) == 0
    assert candidate([5, 7, 9, 15, 18], [8, 10, 12, 20, 24]) == 3
    assert candidate([1, 2, 3, 4, 5], [10, 10, 10, 10, 10]) == 5
```

## Entry Point

`train_schedule_optimization`

