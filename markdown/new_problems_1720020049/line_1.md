# Task ID: hard/5

## Topics

['Iterator', 'Array', 'Line Sweep']

## Cover Story

['airplane', 'farm']

## Prompt

```python
def crop_duster_schedule(timespans, duration):
    """
    Imagine running a farm that gets serviced by a crop-dusting airplane whose availability is governed by a strict schedule. The airplane can only operate continuously over the farm for a specified maximum duration, and the farm needs to optimize when the crop-dusting should take place during the day based on available time slots.

    You need to write a function that takes a list of time intervals (timespans) during which the airplane is available for crop-dusting, and the maximum continuous duration (in minutes) the airplane can fly over your farm. Each time interval is represented as a tuple (start, end) where both start and end are integers representing minutes since midnight (e.g., 600 for 10:00 AM and 660 for 11:00 AM).

    Your function should return the earliest possible continuous time interval of 'duration' minutes for which the airplane could operate. If no such interval can be found within any of the given timespans, return None.

    Note:
    - The entries in the timespan list do not necessarily come in a chronological order.
    - The start and end of a timespan are inclusive.
    - If there are multiple intervals that meet the criterion, return the earliest one based on the start time.
    """

```

## Cleaned Prompt

```python
def crop_duster_schedule(timespans, duration):
    Given a list of time intervals (timespans) and a maximum duration, return the earliest continuous time interval of that duration that fully fits within one of the available timespans. If no such interval exists, return None.
```

## Warnings

- Solution failed correctness check.
- 5, Time calculation error: The test case `assert candidate([(600, 615), (620, 675)], 60) == (620, 680)` incorrectly calculates a 60-minute interval as starting at 620 and ending at 680, which actually spans 61 minutes (not 60). The correct ending minute should be 679 for a 60-minute duration starting at 620. This shows a misunderstanding or mistake in the problem's tests concerning time intervals.
- 4, Inclusivity contradiction: The problem prompt describes the start and end times of a timespan as inclusive, which isn't consistent with typical time interval handling where the end is often exclusive. This might lead to off-by-one errors, especially in calculations and might confuse participants about how to implement their solutions.

## Canonical Solution

```python
    def crop_duster_schedule(timespans, duration):
        if not timespans or duration <= 0:
            return None

        # Normalize and sort the timespans by start time
        sorted_spans = sorted((min(start, end), max(start, end)) for start, end in timespans)

        # Use the algorithm similar to line sweep to find feasible interval
        potential_starts = []
        current_end = 0

        for start, end in sorted_spans:
            if start > current_end:
                current_end = start
            while current_end + duration <= end:
                potential_starts.append((current_end, current_end + duration))
                current_end += 1

        if potential_starts:
            return min(potential_starts, key=lambda x: x[0])

        return None
```

## Test Cases

```python
def check(candidate):
    assert candidate([(600, 700), (720, 800)], 30) == (600, 630)
    assert candidate([(600, 615), (620, 675)], 60) == (620, 680)
    assert candidate([(300, 330), (340, 360)], 20) == (300, 320)
    assert candidate([(100, 105), (200, 205)], 10) == None
    assert candidate([(600, 700), (750, 820)], 90) == None
    assert candidate([(200, 400), (500, 600)], 180) == (200, 380)
```

## Entry Point

`crop_duster_schedule`

