# Task ID: hard/2

## Prompt

```python
def longest_non_repeating_substring(s):
    """
    Write a function that takes a string and returns the length of the longest substring without repeating characters.

    For example:
    - If input is 'abcabcbb', the output should be 3 ('abc' is the longest substring without repeating characters).
    - If input is 'bbbbb', the output should be 1 (the longest substring without repeating characters could be any single 'b').
    - If input is '', the output should be 0 (no substring).

    Parameters:
    - s (str): The input string.

    Returns:
    - int: The length of the longest substring without repeating characters.
    """

```

## Canonical Solution

```python
def longest_non_repeating_substring(s):
    max_len = 0
    start = 0
    seen = {}

    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        else:
            max_len = max(max_len, i - start + 1)

        seen[char] = i

    return max_len
```

## Test Cases

```python
def check(candidate):
    assert candidate('abcabcbb') == 3
    assert candidate('bbbbb') == 1
    assert candidate('') == 0
    assert candidate('pwwkew') == 3
    assert candidate('abcdefghi') == 9
    assert candidate('dvdf') == 3
```

## Entry Point

`longest_non_repeating_substring`

