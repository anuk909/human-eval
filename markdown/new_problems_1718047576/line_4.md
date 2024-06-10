# Task ID: hard/4

## Prompt

```python
def unique_strings_in_order(strings):
    """
    Write a function that takes a list of strings and returns a new list containing only the unique strings in the order they first appeared in the input list.

    For example:
    - If the input is ['apple', 'banana', 'apple', 'orange', 'banana', 'pear'], the output should be ['apple', 'banana', 'orange', 'pear'] because 'apple' and 'banana' are repeated and we consider them only once in the order they first appear.

    Parameters:
    - strings (List[str]): The input list of strings.

    Returns:
    - List[str]: A list of strings with duplicates removed, preserving the original order of first occurrences.
    """

```

## Canonical Solution

```python
def unique_strings_in_order(strings):
    seen = set()
    unique = []
    for string in strings:
        if string not in seen:
            unique.append(string)
            seen.add(string)
    return unique
```

## Test Cases

```python
def check(candidate):
    assert candidate(['apple', 'banana', 'apple', 'orange', 'banana', 'pear']) == ['apple', 'banana', 'orange', 'pear']
    assert candidate([]) == []
    assert candidate(['orange', 'apple', 'apple', 'banana', 'orange']) == ['orange', 'apple', 'banana']
    assert candidate(['hello', 'hello', 'hello']) == ['hello']
    assert candidate(['unique']) == ['unique']
    assert candidate(['string', 'string', 'string', 'string']) == ['string']
```

## Entry Point

`unique_strings_in_order`

