# Task ID: hard/1

## Topics

["McCreight's Algorithm", 'Cuckoo Hashing']

## Cover Story

['circus', 'cloning device']

## Prompt

```python
def circus_tricks(order, tricks, k):
    """
    In a mystical circus, a performer has a cloning device and a list of tricks, where each trick has a certain appeal point (non-negative integer).
    Every day, the performer uses the cloning device to clone themselves for the day's performance.

    'order' is a string representing the sequence in which the tricks are performed, a shuffled permutation of integers from 0 to len(tricks)-1 in string format.
    'tricks' is a list of integers representing the appeal points for each trick.

    The cloning device comes with a constraint named 'k'. After every 'k' tricks performed, when the cloned performer goes back into the device, it causes all occurrences of the subsequence pattern used in the last k tricks to disappear from the subsequent performances if it's repetitive.
    Use McCreight's Algorithm to find these patterns in the order.

    Your task is to compute the sum of the appeal points for tricks that remain after considering all the eliminations caused by the device.

    Note:
    - The length of the order string equals the length of the tricks list.
    - Implement Cuckoo Hashing to manage and check sequences efficiently during the process.
    """

```

## Cleaned Prompt

```python
def circus_tricks(order, tricks, k):
    """
    Compute the sum of the appeal points for tricks that remain after considering all the eliminations caused by a cloning device in a circus performance.
    'order' is a string representing the sequence in which the tricks are performed.
    'tricks' is a list of the appeal points for each trick.
    Use McCreight's Algorithm to find repetitive sequences and Cuckoo Hashing to manage them.
    """

```

## Canonical Solution

```python
    def mc_creight_algorithm(string):
        # Implement the McCreight’s algorithm for finding patterns
        pass

    def cuckoo_hashing_insert(table, value, buffer):
        # Implement cuckoo hashing algorithm for sequence insertion and conflict resolution
        pass

    unique_tricks_set = set(order)
    for i in range(0, len(order), k):
        current_sequence = order[i:i+k]
        if mc_creight_algorithm(order, current_sequence):
            # Remove the found pattern using cuckoo hashing mechanics
            cuckoo_hashing_insert(table, current_sequence, buffer)
            order = order.replace(current_sequence, '')

    result = sum(tricks[int(trick)] for trick in unique_tricks_set if trick in order)
    return result
```

## Test Cases

```python
def check(candidate):
    assert candidate('42013', [5, 3, 7, 1, 4], 2) == 19
    assert candidate('0123456789', [1,2,3,4,5,6,7,8,9,10], 3) == 55
    assert candidate('4658709213', [4,8,15,16,23,42,2,7,45,11], 5) == 161
    assert candidate('012345', [0,0,0,0,0,0], 2) == 0
    assert candidate('22222', [1,1,1,1,1], 2) == 1
```

## Entry Point

`circus_tricks`

