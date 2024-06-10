# Task ID: hard/1

## Prompt

```python
def find_first_recurring_char(s):
    """
    Write a function that takes a string and returns the first recurring character in it. If there are no recurring characters, return None.

    A recurring character is the one that appears more than once in the string.

    For example:
    - If input is 'acbbac', the output should be 'b' since 'b' is the first character that appears more than once.
    - If input is 'abcdef', the output should be None since there are no characters appearing more than once.

    Parameters:
    - s (str): The input string.

    Returns:
    - (Optional[char]): The first recurring character or None if there is no recurring character.
    """

```

## Canonical Solution

```python
def find_first_recurring_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None
```

## Test Cases

```python
def check(candidate):
    assert candidate('acbbac') == 'b'
    assert candidate('abcdef') == None
    assert candidate('') == None
    assert candidate('abba') == 'b'
    assert candidate('xyz xyz') == 'x'
    assert candidate('hello world') == 'l'
```

## Entry Point

`find_first_recurring_char`

