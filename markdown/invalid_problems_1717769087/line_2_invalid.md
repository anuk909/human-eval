## Reason

```
Solution failed correctness check. correctness_check_result: failed:
```

# Task ID: hard/1

## Prompt

```python
def unique_char_in_order(s):
    """
    Write a function that takes a string and returns a string containing all unique characters from the input string in the order they first appeared.

    For example:
    - if the input is 'hello', the output should be 'helo'.
    - if the input is 'characters', the output should be 'chartes'.
    - if the input is '', the output should be '' (an empty string).

    Note:
    - The input string will only contain lowercase letters.
    """

```

## Canonical Solution

```python
    def unique_char_in_order(s):
        result = ''
        seen = set()
        for char in s:
            if char not in seen:
                result += char
                seen.add(char)
        return result
```

## Test Cases

```python
def check(candidate):
    assert candidate('hello') == 'helo'
    assert candidate('characters') == 'chartes'
    assert candidate('') == ''
    assert candidate('repetition') == 'reption'
    assert candidate('continuous') == 'continu'
    assert candidate('abbreviation') == 'abreviton'
    assert candidate('punctuation') == 'punctioa'
```

## Entry Point

`unique_char_in_order`

