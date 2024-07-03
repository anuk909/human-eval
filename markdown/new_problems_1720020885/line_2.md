# Task ID: hard/5

## Topics

['Concurrency', 'Hash Table', 'String']

## Cover Story

['restaurant', 'boat']

## Prompt

```python
def overlapping_reservations(reservations):
    """
    Imagine you are designing a system for a restaurant on a boat. The restaurant has limited capacity, and it is crucial to keep track of reservations to avoid overbooking.
    Given a list of reservation entries, each entry is a string formatted as '<name>-<start>-<end>', where:

    - <name> is the customer's name,
    - <start> is the start time in 24-hour format (HHMM, e.g., '1845' for 6:45 PM),
    - <end> is the end time in 24-hour format (HHMM).

    You need to determine if there are any overlapping reservations. Return True if there are overlaps, else False.
    Reservation times are inclusive, meaning from start to the start of the end time (exclusive).

    Note:
    - If <start> is equal to or later than <end>, the reservation is invalid and should be ignored.
    - You need to process potentially large numbers of reservation entries, so your solution should be efficient.

    Examples:
    - overlapping_reservations(['Alice-1200-1300', 'Bob-1230-1330']) should return True because Bob's reservation starts before Alice's ends.
    - overlapping_reservations(['Charlie-0700-0800', 'Delta-0800-0900']) should return False as Delta's reservation starts exactly when Charlie's ends.

    """
```

## Cleaned Prompt

```python
Given a list of reservation entries formatted as '<name>-<start>-<end>', determine if there are any overlapping reservations. If a time range overlaps with any other, return True; otherwise return False. Ignore invalid reservations where <start> is not less than <end>. Example: overlapping_reservations(['Alice-1200-1300', 'Bob-1230-1330']) should return True because there is an overlap.
```

## Warnings

- Solution failed correctness check.
- 4, Ambiguous Input Formatting: The problem expects the input in '<name>-<start>-<end>' format but does not specify how strictly formatted the inputs will be, creating potential issues in parsing inputs. For instance, there could be names with dashes or malformed input strings which can result in runtime errors or incorrect processing.
- 4, Efficiency Concerns Not Benchmarked: While the prompt hints at needing an efficient solution due to potentially large numbers of reservation entries, there is no specifics provided on the expected limits (e.g., maximum number of entries), which makes it difficult to assess whether the provided solution meets necessary performance criteria for all edge cases.

## Canonical Solution

```python
    def overlapping_reservations(reservations):
        cleaned_reservations = []
        for entry in reservations:
            name, start, end = entry.split('-')
            start, end = int(start), int(end)
            if start < end:
                cleaned_reservations.append((start, end))
        cleaned_reservations.sort()
        previous_end = 0
        for start, end in cleaned_reservations:
            if start < previous_end:
                return True
            previous_end = end
        return False
```

## Test Cases

```python
def check(candidate):
    assert candidate(['Alice-1200-1300', 'Bob-1230-1330']) == True
    assert candidate([]) == False
    assert candidate(['Charlie-0700-0800', 'Delta-0800-0900']) == False
    assert candidate(['Eve-1100-1200', 'Frank-1200-1300', 'Gina-1150-1210']) == True
    assert candidate(['Henry-2100-2200', 'Ivy-2000-2100']) == False
    assert candidate(['Jack-1300-1400', 'Jack-1400-1500', 'Kate-1330-1430']) == True
    assert candidate(['Larry-0930-1015', 'Mona-1015-1100']) == False
    assert candidate(['Nate-1500-1600', 'Olivia-1600-1700', 'Pat-1500-1700']) == True
    assert candidate(['Quinn-0845-0915', 'Rosa-0910-1000']) == True
```

## Entry Point

`overlapping_reservations`

