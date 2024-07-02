# Task ID: hard/1

## Topics

['Shell', 'Z-Algorithm']

## Cover Story

['dragons', 'shopping mall']

## Prompt

```python
def dragon_shopping_encryption(events, queries):
    """
    At the Magical Mall, dragons use a special method to encrypt their shopping events using a shell algorithm. An event can combine a series of words to form a long string. The query system at the mall uses a modified Z-algorithm to help the dragons find out how many times a pattern appears in the event string exactly.

    The function receives two parameters:
    - events: a list of tuples, where each tuple contains a string (shop activity description) and an integer (how many times the description should repeat as a shell).
    - queries: a list of strings, where each string is a pattern for which the dragon wants to find exact matches in the built event string.

    It should return a list of integers, where each integer corresponds to the respective query and represents the number of exact matches found in the completed event string.

    Example:
    events = [('fire', 2), ('ice', 1)]   # This would form the string 'firefireice'
    queries = ['fire', 'ice', 'icefire']

    The function should return [2, 1, 0] because:
    - 'fire' appears exactly 2 times
    - 'ice' appears exactly 1 time
    - 'icefire' does not appear

    Note:
    - The events are repeated to form the event string using each tuple's integer as the repetition count.
    - The queries should match exactly and should not overlap.
    """
```

## Cleaned Prompt

```python
Write a function 'dragon_shopping_encryption' that takes a list of tuples representing event descriptions and their repetition counts, and a list of strings representing queries. The function should return how many times each query string exactly appears in the event description after building it from the repetitions.
```

## Canonical Solution

```python
def dragon_shopping_encryption(events, queries):
    def generate_event_string(events):
        return ''.join([desc * mult for desc, mult in events])

    def z_algorithm(s, pattern):
        combined = pattern + '$' + s
        Z = [0] * len(combined)
        l, r, K = 0, 0, 0
        for i in range(1, len(combined)):
            if i > r:
                l, r = i, i
                while r < len(combined) and combined[r] == combined[r - l]:
                    r += 1
                Z[i] = r - l
                r -= 1
            else:
                K = i - l
                if Z[K] < r - i + 1:
                    Z[i] = Z[K]
                else:
                    l = i
                    while r < len(combined) and combined[r] == combined[r - l]:
                        r += 1
                    Z[i] = r - l
                    r -= 1
        return [Z[i] for i in range(len(pattern) + 1, len(combined)) if Z[i] == len(pattern)]

    result = []
    event_string = generate_event_string(events)
    for query in queries:
        matches = z_algorithm(event_string, query)
        result.append(len(matches))
    return result
```

## Test Cases

```python
def check(candidate):
    assert candidate([('fire', 2), ('ice', 1)], ['fire', 'ice', 'icefire']) == [2, 1, 0]
    assert candidate([('flight', 3), ('fight', 2)], ['flight', 'fight']) == [3, 2]
    assert candidate([('dragon', 1), ('magic', 4)], ['gonma', 'magic']) == [0, 4]
    assert candidate([], ['anything']) == [0]
    assert candidate([('imagination', 1)], ['magi', 'nation', 'imagination']) == [1, 1, 1]
    assert candidate([('aa', 2)], ['aaa', 'a']) == [0, 4]
    assert candidate([('xy', 5), ('zxy', 4)], ['xy', 'zxy']) == [5, 4]
```

## Entry Point

`dragon_shopping_encryption`

## Reason

```
Solution failed correctness check.
```

