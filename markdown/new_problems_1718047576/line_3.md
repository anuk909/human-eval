# Task ID: hard/3

## Prompt

```python
def count_matched_parentheses(expressions):
    """
    Write a function that takes a list of string expressions and returns the number of expressions that have perfectly matched parentheses.

    An expression has perfectly matched parentheses if:
    - Each opening parenthesis '(' has a corresponding closing parenthesis ')'.
    - Parentheses are properly nested and matched from inside to outside.

    For example:
    - If the input is ['(a+b)', 'a+(b+c)', '(a+b))', 'a+b)'], the output should be 2 because only '(a+b)' and 'a+(b+c)' have perfectly matched parentheses.

    Parameters:
    - expressions (List[str]): A list of string expressions.

    Returns:
    - int: Number of expressions with perfectly matched parentheses.
    """

```

## Canonical Solution

```python
def count_matched_parentheses(expressions):
    def is_matched(expr):
        balance = 0
        for char in expr:
            if char == '(': balance += 1
            elif char == ')': balance -= 1
            if balance < 0: return False
        return balance == 0

    return sum(is_matched(expr) for expr in expressions)
```

## Test Cases

```python
def check(candidate):
    assert candidate(['(a+b)', 'a+(b+c)', '(a+b))', 'a+b)']) == 2
    assert candidate(['()', '()()', '((()))', '(()']) == 3
    assert candidate(['', '(())', '(()()())']) == 3
    assert candidate(['(a(b)c))', ')(', '((a))', '(()']) == 1
    assert candidate(['((((((((((a))))))))))', '(b(c(d)e)f)g)']) == 1
    assert candidate([]) == 0
```

## Entry Point

`count_matched_parentheses`

