# Task ID: hard/5

## Prompt

```python
def group_anagrams(words):
    """
    Write a function that takes a list of words and returns a list of lists, where each inner list contains words that are anagrams of each other. Words are considered to be anagrams if they contain the same characters with the same frequency.

    For example:
    - Input: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    - Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] because 'eat', 'tea', 'ate' are anagrams; similarly, 'tan' and 'nat' are anagrams, and 'bat' is in its own group.

    All output inner lists should be sorted alphabetically, and the outer list should also be sorted based on the first element of each inner list.

    Parameters:
    - words (List[str]): The input list of words.

    Returns:
    - List[List[str]]: A list with grouped anagrams.
    """

```

## Canonical Solution

```python
def group_anagrams(words):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    result = [sorted(group) for group in anagrams.values()]
    return sorted(result, key=lambda x: x[0])
```

## Test Cases

```python
def check(candidate):
    result = candidate(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
    expected = [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]
    assert all(sorted(r) == sorted(e) for r, e in zip(result, expected)), 'Test case 1 failed'
    result = candidate([''])
    expected = [['']]
    assert all(sorted(r) == sorted(e) for r, e in zip(result, expected)), 'Test case 2 failed'
    result = candidate(['a'])
    expected = [['a']]
    assert all(sorted(r) == sorted(e) for r, e in zip(result, expected)), 'Test case 3 failed'
    result = candidate(['abc', 'bca', 'cab', 'test', 'sett'])
    expected = [['abc', 'bca', 'cab'], ['sett', 'test']]
    assert all(sorted(r) == sorted(e) for r, e in zip(result, expected)), 'Test case 4 failed'
    result = candidate([])
    expected = []
    assert all(sorted(r) == sorted(e) for r, e in zip(result, expected)), 'Test case 5 failed'
```

## Entry Point

`group_anagrams`

