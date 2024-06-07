## Reason

```
Solution failed correctness check. correctness_check_result: failed:
```

# Task ID: hard/1

## Prompt

```python
def longest_common_start(sa, sb):
    """
    Write a function that takes two strings and returns the length of the longest common starting substring from both strings.
    A substring is a contiguous sequence of characters within a string.

    For example:
    - longest_common_start('prefixsuffix', 'prefixabc') should return 6 because the common starting substring is 'prefix'.
    - longest_common_start('hello', 'world') should return 0 because there is no common starting substring.
    - longest_common_start('abc', 'abcdefg') should return 3 as 'abc' is the common starting substring.
    - longest_common_start('abcdefg', 'abc') should return 3 as 'abc' is the common starting substring.

    Note:
    - If either string is empty, the returned length should be 0.

    The function should be optimized for performance.
    """

```

## Canonical Solution

```python
    def longest_common_start(sa, sb):
        min_length = min(len(sa), len(sb))
        for i in range(min_length):
            if sa[i] != sb[i]:
                return i
        return min_length
```

## Test Cases

```python
def check(candidate):
    assert candidate('prefixsuffix', 'prefixabc') == 6
    assert candidate('hello', 'world') == 0
    assert candidate('', 'prefix') == 0
    assert candidate('abc', 'abcdefg') == 3
    assert candidate('abcdefg', 'abc') == 3
    assert candidate('incursion', 'incense') == 3
    assert candidate('literature', 'literal') == 5
    assert candidate('compatibility', 'comparison') == 5
    assert candidate('interview', 'internet') == 5
    assert candidate('hardware', 'hardwork') == 4
```

## Entry Point

`longest_common_start`

