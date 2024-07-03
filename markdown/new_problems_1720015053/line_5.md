# Task ID: hard/4

## Topics

['Bitmask', 'Boyer-Moore Algorithm']

## Cover Story

['sneaky shadows', 'shrink ray']

## Prompt

```python
def detect_sneaky_shadow(sequence, patterns):
    """
    Imagine you are trying to detect sneaky shadows in a sequence of actions. Each action in the sequence is either a 'stretch', 'shrink', or 'normal'. A sneaky shadow exhibits specific patterns after being hit by a shrink ray, and you need to detect all sequences that match these shadow patterns in the given sequence of actions.

    The sequence of actions is represented as a string consisting of 'S' for 'stretch', 'N' for 'normal', and 'R' for 'shrink'. Each shadow pattern is also represented as a string of these characters.

    Your task is to implement a function that returns the indices of the start of any pattern from the provided list of patterns that appears in the input sequence using a bitmask and the Boyer-Moore algorithm for maximum efficiency.

    Example:
    - Given the sequence 'SSNRSSRN' and patterns ['SSN', 'SRN'], the function should return [0, 5] since 'SSN' starts at index 0 and 'SRN' starts at index 5.

    Note:
    - This function should perform efficiently even if the sequence and patterns are large.
    """

```

## Cleaned Prompt

```python
def detect_sneaky_shadow(sequence, patterns):
    """
    Implement a function that returns the indices of the start of any pattern from a provided list that appears in the given sequence of actions, using a bitmask and the Boyer-Moore algorithm for searching efficiently.

    The sequence and patterns consist of characters 'S' (stretch), 'N' (normal), and 'R' (shrink).
    """

```

## Canonical Solution

```python
    def find_pattern(sequence, pattern):
        n = len(sequence)
        m = len(pattern)
        skip = 0
        for i in range(n - m + 1):
            for j in range(m):
                if sequence[i + j] != pattern[j]:
                    break
            else:
                return i
        return -1

    def detect_sneaky_shadow(sequence, patterns):
        results = []
        for pattern in patterns:
            index = find_pattern(sequence, pattern)
            if index != -1:
                results.append(index)
        return sorted(results)
```

## Test Cases

```python
def check(candidate):
    assert candidate('SSNRSSRN', ['SSN', 'SRN']) == [0, 5]
    assert candidate('SSSRNRSNRN', ['SSS', 'RNR']) == [0, 6]
    assert candidate('NSSRSSN', ['SSN', 'RN']) == [3]
    assert candidate('SSSS', ['RR', 'SS', 'NN']) == [0, 2]
    assert candidate('RRRR', ['RR', 'SS', 'NN']) == [0, 1, 2]
    assert candidate('NNSRRNSRRN', ['SS', 'NR', 'RS']) == [4, 8]
    assert candidate('', ['SS', 'RN']) == []
    assert candidate('NRSSR', ['SS', 'RN']) == [1]
```

## Entry Point

`detect_sneaky_shadow`

## Warnings

- Solution failed correctness check.
- 5, Contradiction in solution technology: The problem statement specifies that the solution must use a bitmask and the Boyer-Moore algorithm for maximum efficiency, but the provided canonical solution utilizes a naive implementation for pattern matching, which neither employs bitmasking nor the Boyer-Moore algorithm. This discrepancy makes the provided solution inconsistent with the task’s requirements, potentially leading to inefficiencies and misunderstanding about the required algorithmic approach.

