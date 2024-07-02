## Reason

```
Solution failed correctness check. correctness_check_result: failed:
```

# Task ID: hard/1

## Prompt

```python
def count_substring_without_repetition(s: str, substr: str) -> int:
    """
    Write a function that takes a string 's' and a substring 'substr', and returns the number of times 'substr' appears in 's' as a contiguous substring without any of its characters repeating more than once in 's'.

    For example, if 's' is 'abcdecfgh' and 'substr' is 'abc', the function returns 1 because 'abc' appears contiguously in 's' without any repeated character. If 's' is 'ababc' and 'substr' is 'ab', it returns 0 because each 'ab' in 'ababc' overlaps with a repeated 'a' or 'b' in the original string 's'.

    Note:
    - If either 's' or 'substr' is empty, return 0.

    Constraints:
    - The characters in 's' and 'substr' are all lowercase letters.
    """

```

## Canonical Solution

```python
    def count_substring_without_repetition(s, substr):
        n = len(substr)
        count = 0
        if n == 0:
            return 0
        for i in range(len(s) - n + 1):
            if s[i:i+n] == substr and len(set(s[i:i+n])) == n:
                count += 1
        return count
```

## Test Cases

```python
def check(candidate):
    assert candidate('abcdecfgh', 'abc') == 1
    assert candidate('ababc', 'ab') == 0
    assert candidate('testsubstrsubstr', 'substr') == 2
    assert candidate('nonrepeating', '') == 0
    assert candidate('', 'any') == 0
    assert candidate('xyz', 'xyz') == 1
    assert candidate('aabbcc', 'abc') == 0
```

## Entry Point

`count_substring_without_repetition`

