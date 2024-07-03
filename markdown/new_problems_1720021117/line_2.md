# Task ID: hard/3

## Topics

['Rejection Sampling', 'Strongly Connected Component', 'Counting']

## Cover Story

['archaeological dig', 'submarine']

## Prompt

```python
def recover_artifacts(nav_grid, sub_path):
    """
    During a deep-sea archaeological exploration, your submarine follows a predetermined path through a grid of sectors. Each sector on the grid can contain zero or more archaeological artifacts. After the submarine completes its path, it can communicate the sectors it traversed to the surface team. Based on environmental factors and the submarine's path, the likelihood of recovering artifacts from each sector varies.

    The grid is represented as a 2D array 'nav_grid', where each element is a list that could contain names of artifacts found in that sector (e.g., ['vase', 'coin']). The submarine's path is a series of directions given as a list of tuples (row, col) starting from the top left corner (0, 0).

    However, there is a complication. Due to communication errors and navigation glitches, the submarine might not follow the path perfectly. It has a known probability of rejection 'rejection_probability' that defines how often the submarine will reject moving to the intended next sector and instead randomly choose one of the adjacent sectors (up, down, left, or right). If the intended move was out of bounds or back to a previously visited sector, the rejection option is considered again.

    Your task is to calculate the average number of unique artifacts that would be collected from the path, taking into account the rejection probability and ensuring the submarine remains within bounds and doesn't revisit sectors. The submarine can only move up, down, left, or right.

    Example:
    nav_grid = [[['ancient lamp'], []], [['rusted sword'], ['golden coin']]]
    sub_path = [(0, 0), (1, 0), (1, 1)]
    rejection_probability = 0.1

    Assuming perfect navigation (0% rejection), the submarine collects: ['ancient lamp', 'rusted sword', 'golden coin'].

    Note:
    - The grid will have at least size 1x1 and can be non-square.
    - The sub_path will start at (0, 0) and it will include valid positions within the bounds of the grid.
    """
```

## Cleaned Prompt

```python
The problem involves a submarine navigating a grid of sectors, each sector can contain archaeological artifacts. The submarine follows a defined path with a chance of deviation due to a 'rejection_probability' that causes it to potentially move to an adjacent sector instead of the intended. The task is to compute the average number of unique artifacts collected considering this probability.
```

## Warnings

- Solution failed correctness check.
- 4, Missing rejection probability parameter: The task prompt does not specify the `rejection_probability` as a parameter for the `recover_artifacts` function, while the canonical solution and the test case definition include it. This discrepancy can lead to confusion about the function's definition and usage.

## Canonical Solution

```python
    def recover_artifacts(nav_grid, sub_path, rejection_probability):
        import random
        from collections import defaultdict

        def in_bounds(r, c):
            return 0 <= r < len(nav_grid) and 0 <= c < len(nav_grid[0])

        def get_adjacent(r, c):
            adj = []
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if in_bounds(nr, nc):
                    adj.append((nr, nc))
            return adj

        artifacts_collected = set()
        current_position = sub_path[0]
        artifacts_collected.update(nav_grid[current_position[0]][current_position[1]])

        for next_position in sub_path[1:]:
            if random.random() > rejection_probability:
                if current_position == next_position:
                    continue
                artifacts_collected.update(nav_grid[next_position[0]][next_position[1]])
                current_position = next_position
            else:
                possible_moves = get_adjacent(*current_position)
                random_choice = random.choice(possible_moves)
                artifacts_collected.update(nav_grid[random_choice[0]][random_choice[1]])
                current_position = random_choice

        return len(artifacts_collected)
```

## Test Cases

```python
def check(candidate):
    nav_grid1 = [[['vase'], []], [['coin'], ['rusted sword']]]
    sub_path1 = [(0, 0), (1, 0), (1, 1)]
    assert candidate(nav_grid1, sub_path1, 0) == 3
    assert candidate(nav_grid1, sub_path1, 0.1) >= 2
    assert candidate(nav_grid1, sub_path1, 1) >= 1

    nav_grid2 = [[['vase', 'map'], ['treasure']], [['golden coin'], ['mask']]]
    sub_path2 = [(0, 0), (0, 1)]
    assert candidate(nav_grid2, sub_path2, 0) == 3
    assert candidate(nav_grid2, sub_path2, 0.5) >= 2
    assert candidate(nav_grid2, sub_path2, 1) >= 1
```

## Entry Point

`recover_artifacts`

