## Reason

```
Solution failed correctness check. correctness_check_result: failed:
```

# Task ID: hard/1

## Prompt

```python
def balanced_braces(n):
    """
    Write a function that generates all possible combinations of 'n' pairs of balanced braces in lexicographical order.

    For example, if n is 2, the function should return ['(())', '()()'].

    Note:
    - 'n' will be a non-negative integer.
    - The output should be a list of strings.
    - If n is 0, return an empty list [].
    """

```

## Canonical Solution

```python
    def generate_braces(result, current, open, close, n):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open < n:
            generate_braces(result, current + '(', open + 1, close, n)
        if close < open:
            generate_braces(result, current + ')', open, close + 1, n)

    result = []
    generate_braces(result, '', 0, 0, n)
    return result
```

## Test Cases

```python
def check(candidate):
    assert candidate(2) == ['(())', '()()']
    assert candidate(1) == ['()']
    assert candidate(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']
    assert candidate(0) == []
    assert candidate(4) == ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()(())()', '()(()())', '()()(())', '()()()()']
```

## Entry Point

`balanced_braces`

