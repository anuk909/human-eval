# Task ID: hard/5

## Topics

['Dynamic Programming', 'Line Sweep', 'Finding Articulation Points in Graphs']

## Cover Story

['school', 'mischievous fairies']

## Prompt

```python
def enchanted_classroom(seating, whispers):
    """
    In a classroom at a magic school, students are seated in a line with varying magical powers. Each student is represented by an integer in the list `seating` where the integer represents the student's power level. However, due to some mischievous fairies, some students start whispering spells to their neighbors.

    The `whispers` list consists of tuples (i, j), indicating that student i is whispering a spell to student j. This whisper increases the power of student j by the power of student i.

    The goal of this function is to determine the final power levels of each student after all the spells from their neighbors have been applied. Note that whispers can have a cumulative effect (a student can receive power from multiple peers), and the spells are instantaneous meaning they all happen at the same time.

    Example:
    seating = [10, 20, 30]
    whispers = [(0, 1), (1, 2), (0, 2)]

    The output should be [10, 30, 60] because:
    - Student 0 (with power 10) whispers to Student 1, making Student 1's power 20 + 10 = 30
    - Student 1 (with power 20) whispers to Student 2, making Student 2's power 30 + 20 = 50
    - Student 0 also whispers directly to Student 2, adding another 10, making Student 2's power 50 + 10 = 60

    Constraints:
    - `seating` has at least 2 and at most 1000 students.
    - `whispers` list size will be at most 10000.

    Employ a method using graph theory and ensure each student has their final calculated power effectively.
    """
```

## Cleaned Prompt

```python
Write a function that adjusts the power level of students based on the given whispers. The input includes two lists: `seating`, representing students' initial powers, and `whispers`, where each whisper (i, j) means student i adds their power to student j's power. All whispers are simultaneous.
```

## Warnings

- Solution failed correctness check.
- 5, Missing Input Validation: The problem statement does not specify what should happen if the indexes in the 'whispers' tuples are out of the bounds of the 'seating' list. This could lead to runtime errors if the function tries to access an index that does not exist in the 'seating' list.
- 4, Ambiguity in Problem Definition: There's no clarification provided on whether the interactions (whispers) can cycle (e.g., student A whispers to student B, student B to student C, and student C back to student A). The presence of cycles can significantly affect the logic required to solve the problem, especially in relation to maintaining the simultaneity of effects. The example test case involving a cycle does not detail if additional complexity should be handled or if such cases might be omitted.
- 4, Unclear Error Handling: The problem does not specify how to handle invalid input, such as negative indices in 'whispers', non-integer values in 'seating' or 'whispers', or empty lists. Making assumptions about these can lead to varying implementations, potentially affecting the robustness and reliability of the solution.
- 4, Inadequate Explanation of Example: While the example output explanation adds the values correctly, it contradicts the given output. The walkthrough adds up to [10, 30, 60], but the calculation described adds up to [10, 30, 70] by adding 50 (current power of 2) + 20 (power of 1 after the initial whisper from 0 to 1). This inaccuracy can confuse readers about how the whispers propagate and in which order, impacting their understanding of the problem logic.

## Canonical Solution

```python
def enchanted_classroom(seating, whispers):
    n = len(seating)
    final_powers = seating[:]
    # Initialize graph with number of students
    graph = [[] for _ in range(n)]
    # Graph creation
    for src, dest in whispers:
        graph[src].append(dest)

    # Distribute the powers from each student to the others
    for i in range(n):
        for neighbor in graph[i]:
            final_powers[neighbor] += seating[i]

    return final_powers
```

## Test Cases

```python
def check(candidate):
    assert candidate([10, 20, 30], [(0, 1), (1, 2), (0, 2)]) == [10, 30, 60]
    assert candidate([40, 50, 20], [(1, 0), (2, 1)]) == [90, 70, 20]
    assert candidate([100, 200], [(0, 1)]) == [100, 300]
    assert candidate([1, 2, 3, 4, 5], [(0, 1), (1, 2), (2, 3), (3, 4)]) == [1, 3, 5, 7, 9]
    assert candidate([10, 5, 25, 40, 10], [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4), (4, 0)]) == [20, 15, 30, 65, 50]
```

## Entry Point

`enchanted_classroom`

