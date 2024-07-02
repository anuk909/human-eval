# Task ID: hard/1

## Topics

Enumeration, Sprague-Grundy Theorem

## Cover Story

['post-apocalyptic world', 'cyberpunk']

## Prompt

```python
def survival_grundy(n, k, moves):
    """
    In a post-apocalyptic cyberpunk world, cities are represented as nodes in a graph (with n nodes). Two players are engaged in a survival game where they can choose a city to perform critical operations to ensure survival. Each player alternates turns, and on their turn, they can select up to k ruins (where k is a specific number of nodes they can operate at once).

    The operation initiative is assigned a Grundy number using the Sprague-Grundy theorem which helps in determining which player has a winning strategy given the current state of the game.

    Given the number of cities (n), the maximum number of operations one can perform in a turn (k), and an array moves that specify the permissible number of cities a player can operate on in their turn (up to k), you need to return the Grundy number for the game state starting with all n cities operational.

    Note:
    - moves array contains at least one element.
    - All elements in moves are distinct and between 1 and k inclusive.
    - The Grundy number for a game state where no operations can be performed (no available moves) is 0.
    """
```

## Cleaned Prompt

```python
def survival_grundy(n, k, moves):
    """
    Given a number of cities (n), a maximum number of operations in a turn (k), and permissible moves in a turn, return the Grundy number for a game state starting with all cities operational using the Sprague-Grundy theorem.
    """
```

## Canonical Solution

```python
def mex(s):
        m = 0
        while m in s:
            m += 1
        return m

    def grundy(n, k, moves):
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            reachable_grundies = set()
            for move in moves:
                if i >= move:
                    reachable_grundies.add(dp[i - move])
            dp[i] = mex(reachable_grundies)
        return dp[n]

    return grundy(n, k, moves)
```

## Test Cases

```python
def check(candidate):
    assert candidate(10, 3, [1, 3]) == 2
    assert candidate(5, 5, [1, 2, 3, 4, 5]) == 0
    assert candidate(7, 2, [1, 2]) == 2
    assert candidate(12, 4, [1, 4]) == 4
    assert candidate(75, 5, [1, 2, 3, 4, 5]) == 1
```

## Entry Point

`survival_grundy`

## Reason

```
Solution failed correctness check.
```

