# Task ID: hard/4

## Topics

['Red-Black Tree', 'Detect Cycle in Graph', 'Subsets']

## Cover Story

['arctic', 'wizard school']

## Prompt

```python
def arctic_exploration_plans(wizard_schools, paths):
    """
    In the land of Arctica, there exists a group of wizard schools separated by treacherous paths. The local wizard council needs help to plan for safe exploration among the schools. Each wizard school can be considered as a node and the paths between them as edges of a graph.

    The function 'arctic_exploration_plans' needs to take two parameters:
    1. wizard_schools: A list of school names (each unique and represented as string).
    2. paths: A list of tuples (school1, school2) representing a bidirectional path between 'school1' and 'school2'.

    The task is to detect any cycles within this graph and return as subsets the names of schools that are in cycles. For performance efficiency, schools in cycles should be reported as per the regions detected using Red-Black Tree structure for a clever arrangement.

    Also, each subset or 'region' of wizard schools involved in cycles should have a structural hierarchical representation shown as a binary tree. Each tree should be visualized and returned in the form of a string graph.

    Each school is ideally involved in one major cycle for simplicity. Additional output should include the number of unique cycles detected.

    For example, if the input is:
        wizard_schools = ['A', 'B', 'C', 'D'],
        paths = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'D')]
    The output should be a tuple: ('Region structured as Trees', 1)
    Here 'Region structured as Trees' is a visual string representation of schools in cycles and '1' represents the number of unique cycles.

    Note: Ensure the solution is efficient in handling the cycle detection and Red-Black tree creation and visualization.
    """

```

## Cleaned Prompt

```python
Write a function 'arctic_exploration_plans' that takes a list of wizard schools (nodes) and paths (edges) between them and identifies cycles in the graph. The schools involved in these cycles need to be arranged and visualized using a Red-Black Tree, and the output should include a visual representation of these cycles alongside the count of unique cycles detected. 

Example: arctic_exploration_plans(['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'D')]) should return a tuple containing a string representation of the cycles arranged in a Red-Black Tree format and the number of these cycles (1).
```

## Warnings

- Solution failed correctness check.
- 5, Unclear Output Requirements: The problem statement specifies that the output should be a tuple containing a visual string representation of schools in cycles structured as binary trees and the number of unique cycles. However, it does not provide a clear and concise format or any examples for what this visual string representation should look like, which can lead to ambiguity in expected solutions.
- 5, Implementation Complexity: The task requires integration of cycle detection in a graph, representation using a Red-Black Tree, and then visualization of this tree. Each of these alone is complex and integrating all can lead to overly complex solutions. Especially, visualizing a tree structure in string format can be inherently complex and is not commonly a practice in typical algorithmic problem-solving contexts.
- 5, Unspecified Behavior for Non-Cycle Graph Components: The prompt focuses on detecting cycles and visualizing parts of the graph within cycles. It does not specify what should be done with graph components or schools that do not form part of a cycle. This omission could lead to incomplete or incorrect handling of data, affecting the correctness of implementations.
- 4, No Clarification on Red-Black Tree Usage: The task mentions organizing schools in cycles using a Red-Black Tree for 'clever arrangement', but does not explain why this data structure is chosen over others, what properties of Red-Black Trees are being leveraged for this task, or how it specifically benefits the arrangement and visualization process. This lack of justification makes the choice seem arbitrary and confusing.

## Canonical Solution

```python
import collections

    def has_cycle_util(graph, v, visited, parent):
        visited.add(v)
        for neighbour in graph[v]:
            if neighbour not in visited:
                if has_cycle_util(graph, neighbour, visited, v):
                    return True
            elif parent != neighbour:
                return True
        return False


    def create_graph(schools, paths):
        graph = collections.defaultdict(list)
        for s1, s2 in paths:
            graph[s1].append(s2)
            graph[s2].append(s1)
        return graph

    def detect_cycles(graph, schools):
        visited = set()
        cycle_members = set()
        for school in schools:
            if school not in visited:
                if has_cycle_util(graph, school, visited, -1):
                    cycle_members.add(school)
        return cycle_members


    def visualise_using_red_black_tree(cycle_members):
        # Implementation Depends on an external library or concept
        pass

    def arctic_exploration_plans(wizard_schools, paths):
        graph = create_graph(wizard_schools, paths)
        cycles = detect_cycles(graph, wizard_schools)
        tree_visualisation = visualise_using_red_black_tree(cycles)
        return (tree_visualisation, len(cycles))
```

## Test Cases

```python
def check(candidate):
    assert candidate(['A', 'B', 'C', 'D'], [('A', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'D')]) == ('Region structured as Trees', 1)
    assert candidate(['A', 'B', 'C'], [('A', 'B'), ('B', 'C')]) == ('', 0)
    assert candidate(['A', 'B', 'C', 'D', 'E'], [('A', 'B'), ('B', 'C'), ('C', 'A'), ('D', 'E'), ('E', 'D')]) == ('Region structured as Trees', 2)
    assert candidate(['X', 'Y', 'Z'], []) == ('', 0)
    assert candidate(['A', 'B'], [('A', 'B')]) == ('', 0)
```

## Entry Point

`arctic_exploration_plans`

