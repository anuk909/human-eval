# Task ID: hard/3

## Topics

['Enumeration', "Kosaraju's Algorithm"]

## Cover Story

['lost city', 'enchanted lab']

## Prompt

```python
def find_components(graph):
    """
    In the ancient land of Graphonia, a mythical laboratory in the once-lost city of Nodar is intricately connected through a magical network of one-way transporters. Each room in the lab corresponds to a 'node', and each transporter corresponds to a 'directed edge' connecting a pair of rooms (nodes). The historical texts suggest that the transporters were enchanted to form mystical components where any room within a component can be reached from any other room within the same component.

    Your quest is to uncover these mystical components using Kosaraju's Algorithm for strongly connected components. Given the layout of the lab as a directed graph represented by an adjacency list, where the keys are nodes and each value list contains the nodes that can be reached directly from the key node, you should return a list of components. Each component should be a list of nodes, sorted and then components should be sorted by their first element. 

    Note:
    - Nodes are represented as positive integers.
    - Resulting component lists should be sorted internally, and the list of components should be sorted by the smallest element in each component.
    """,
    
```

## Cleaned Prompt

```python
def find_components(graph):
    Return a list of strongly connected components of the directed graph using Kosaraju's Algorithm. Nodes are represented as integers. Components should be lists of nodes, sorted internally, and the list of components sorted by the smallest element in each component.
```

## Canonical Solution

```python
def find_components(graph):
    def dfs(stack, node, visited, visit_order):
        visited[node] = True
        for neighbor in graph.get(node, []):
            if not visited.get(neighbor, False):
                dfs(stack, neighbor, visited, visit_order)
        visit_order.append(node)

    def reverse_graph(graph):
        reversed_graph = {}
        for src in graph:
            for dest in graph[src]:
                if dest not in reversed_graph:
                    reversed_graph[dest] = []
                reversed_graph[dest].append(src)
        return reversed_graph

    def fill(stack, node, visited, component):
        visited[node] = True
        component.append(node)
        for neighbor in reversed_g.get(node, []):
            if not visited.get(neighbor, False):
                fill(stack, neighbor, visited, component)

    visited = {}
    stack = []
    for node in graph:
        if not visited.get(node, False):
            dfs(stack, node, visited, stack)

    reversed_g = reverse_graph(graph)
    visited = {}
    components = []
    while stack:
        node = stack.pop()
        if not visited.get(node, False):
            component = []
            fill(stack, node, visited, component)
            components.append(sorted(component))
    components.sort(key=lambda x: x[0])
    return components
```

## Test Cases

```python
def check(candidate):
    assert candidate({1: [2], 2: [3], 3: [1], 4: [5], 5: [], 6: [7], 7: [8], 8: [6]}) == [[1, 2, 3], [4], [5], [6, 7, 8]]
    assert candidate({1: [2], 2: [3], 3: [1]}) == [[1, 2, 3]]
    assert candidate({}) == []
    assert candidate({1: [], 2: [], 3: []}) == [[1], [2], [3]]
    assert candidate({1: [2], 2: [3], 3: [4], 4: [1], 5: [6], 6: [7], 7: [5], 8: [9], 9: [8], 10: [11], 11: [12], 12: [10]}) == [[1, 2, 3, 4], [5, 6, 7], [8, 9], [10, 11, 12]]
```

## Entry Point

`find_components`

## Warnings

- Solution failed correctness check.
- 4, Algorithm explanation: The problem assumes knowledge of Kosaraju's algorithm. However, it does not provide any explanation or reference for participants who might not be familiar with it. Since the algorithm is central to solving the problem, a brief explanation or external reference to study the algorithm could greatly aid understanding.
- 5, Inefficiency in canonical solution logic: The use of a stack is repeated (`stack` variable is unnecessarily passed to the `fill` function, though it is not used in that function). This indicates possible inefficiencies or redundancies in how components are handled or in the overall design of the algorithm solution, which could be streamlined for better performance and clarity.

