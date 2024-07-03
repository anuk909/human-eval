# Task ID: hard/1

## Topics

['Shell', 'Task Scheduling']

## Cover Story

['haunted ship', 'forest']

## Prompt

```python
def haunted_exploration(grid, operations):
    """
    Imagine you're aboard a haunted ship surrounded by a mystical forest. The ship is equipped with an old system that can execute certain operations based on a grid of surveillance data collected by mystical sensors. The grid is a 2D list where each cell can be 'S' (Ship), 'F' (Forest), or 'D' (Detected Anomaly). Operations are scheduled as tasks that need to be executed in a specific order to clear anomalies using ship resources.

    Your function takes two inputs:
    - grid: a 2-dimensional list representing the initial state of the area surrounding the ship.
    - operations: a list of operations where each operation is a string of up to four directional commands: 'U' (Up), 'D' (Down), 'L' (Left), 'R' (Right).

    Operations aim to navigate through the grid to clear 'D' elements turning them into 'S', signifying that anomalies have been addressed. Importantly, each operation starts from where the last one ended, not resetting to the top-left corner unless specifically stated at the end of an operation. Navigating into 'F' regions extends the time required to execute subsequent operations by 1 unit time each. Starting position is always the top-left of the grid unless stated otherwise by an operation.

    The goal is to return how much time in total will it take to execute all the operations. Each move within an operation takes 1 unit time, and if an operation passes through 'F', then *all* subsequent operations increase in duration by 1 unit time per 'F' encounter during that operation.

    Examples:
    Input: ([['S', 'D', 'F'], ['F', 'S', 'D']], ['R', 'D', 'R'])
    Output: 7 (Movement RDR takes 3 units, R takes 2 units due to 1 'F' from RDR, R takes 2 units due to 1 'F' from RDR)

    Note:
    - If an attempt is made to move outside the grid boundaries, the move is ignored and no extra time is consumed (this means the move command is effectively skipped).
    - Only anomaly 'D' can be turned into 'S' by directly stepping on it during an operation.
    """

```

## Cleaned Prompt

```python
Write a function to process operations in a 2D grid either marked as 'S' (Ship), 'F' (Forest), or 'D' (Detected Anomaly). Given initial grid state and a list of operations consisting of 'U', 'D', 'L', 'R' directional commands, manipulate the grid by turning 'D' into 'S'. Each move within an operation takes 1 unit of time and moving into 'F' increases all subsequent operations' time by 1 unit per 'F'. Determine the total time required to execute all operations. Note that each operation's direction navigates from the current grid point and anomalies cleared are modified in the grid.
```

## Warnings

- Solution failed correctness check.
- 5, Ambiguity in Operation Sequence: The problem statement does not clearly specify whether each operation starts from the termination point of the previous operation or is reset to the starting top-left corner each time. This ambiguity can cause confusion and incorrect implementations, making the problem challenging to solve correctly.
- 4, Edge Case Handling for Grid Navigation: The problem description lacks detailed guidance for scenarios where multiple moves in an operation attempt to navigate outside the grid boundaries (such as consecutive 'L' or 'U' commands when already at an edge). This absence of information could result in inconsistent behavior and implementations, affecting the solution's correctness.

## Canonical Solution

```python
def haunted_exploration(grid, operations):
    def in_bounds(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    time = 0
    additional_time = 0
    x, y = 0, 0
    for op in operations:
        local_f_count = 0
        for move in op:
            next_x, next_y = x, y
            if move == 'U':
                next_x -= 1
            elif move == 'D':
                next_x += 1
            elif move == 'L':
                next_y -= 1
            elif move == 'R':
                next_y += 1

            if in_bounds(next_x, next_y):
                x, y = next_x, next_y
                if grid[x][y] == 'D':
                    grid[x][y] = 'S'
                elif grid[x][y] == 'F':
                    local_f_count += 1
        time += len(op) + additional_time
        additional_time += local_f_count

    return time
```

## Test Cases

```python
def check(candidate):
    assert candidate([['S', 'D', 'F'], ['F', 'S', 'D']], ['R', 'D', 'R']) == 7
    assert candidate([['S', 'D', 'S'], ['F', 'D', 'S']], ['D', 'RR', 'UU']) == 11
    assert candidate([['F', 'D', 'S'], ['S', 'S', 'D']], ['R', 'L', 'DD', 'RR']) == 13
    assert candidate([['S', 'S', 'S'], ['S', 'S', 'S']], ['RR', 'LL', 'DD']) == 9
    assert candidate([['D', 'D', 'D'], ['D', 'D', 'D']], ['RRR', 'DD', 'LLL', 'UUU']) == 17
```

## Entry Point

`haunted_exploration`

