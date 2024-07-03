# Task ID: hard/2

## Topics

['Course Schedule', 'Doubly-Linked List', 'Two Pointers']

## Cover Story

['music', 'snakes and rocks']

## Prompt

```python
def snake_concert_planner(courses, prerequisites):
    """
    You are an event manager for a unique concert in the desert that features a live rock band, rare snakes, and interactive music courses. Attendees can take various music-related courses, but some courses have prerequisites that need to be taken first.

    Each course is uniquely represented as an integer, and for each course, there might be one or more prerequisite courses. Given a list of courses and a list of prerequisite pairs, determine if it is possible for an attendee to complete all courses. The additional twist is that each course has a version with a rock music perspective and a version with a snake handling perspective, implemented as a node in a doubly linked list.

    Implement this linked list internally to simulate the course and its perspectives. When checking if it is possible to finish all courses, both perspectives for each course (if exists) should still have prerequisites maintained.

    Note:
    - A course might or might not have a perspective version.
    - Use a two-pointer approach to navigate and manage the doubly linked list.

    Example:
    If courses = [1,2,3], and prerequisites = [(1,2), (2,3)], there is a valid order: either [1,2,3] or its perspective ridden linked versions.

    """

```

## Cleaned Prompt

```python
Given a list of music courses and a list of prerequisite pairs between them, determine if it is possible to complete all courses. Each course can have two perspectives like 'Rock' and 'Snake handling' and can be considered as a node in a doubly linked list, meaning each course has two possible versions linked. When checking for course completion possibility, both perspectives and their prerequisites should be considered. Use two-pointers to manage the doubly linked list transitions.
```

## Warnings

- Solution failed correctness check.
- 5, Ambiguity in Handling Twisted Perspectives: The problem statement introduces an intriguing complexity about multiple perspectives (Rock and Snake Handling) for each course but does not clearly describe how these versions affect the prerequisites and how they should be modeled in the solution. Moreover, it's unclear whether these perspectives are supposed to be separate nodes in the doubly linked list or if each course node should internally represent both perspectives. This lack of clarity can lead to various interpretations and inconsistent implementations.
- 5, Inappropriate Doubly Linked List Utilization: The problem involves prerequisites and course ordering which typically suggests a graph-based approach (like detecting cycles in a directed graph). However, the problem forces the use of a doubly linked list to represent course sequences, which is not naturally suited for prerequisites management involving complex dependencies because doubly linked lists are linear structures. This mismatch complicates the solution unnecessarily and doesn't align well with the fundamental requirements of the problem.
- 5, Unclear Requirements for Two-pointer Technique: The prompt suggests using a "two-pointer approach" to manage the doubly linked list, but it remains unclear how this technique should be effectively applied in the context of course prerequisites which inherently have a hierarchical structure, not a linear one. The two-pointer technique is usually applied to problems involving searches or window-based manipulations on arrays or linear linked lists, not for complex graph traversal or hierarchy resolution in a scenario like checking course completion feasibility.

## Canonical Solution

```python
    class Node:
        def __init__(self, course, next=None, prev=None):
            self.course = course
            self.next = next
            self.prev = prev

    def snake_concert_planner(courses, prerequisites):
        if not courses:
            return True

        course_dict = {course: Node(course) for course in courses}

        # Building the doubly linked list
        for course in courses:
            if course + 1 in course_dict:
                course_dict[course].next = course_dict[course + 1]
                course_dict[course + 1].prev = course_dict[course]

        # Detecting cycle using two pointers
        indegree = {course: 0 for course in courses}
        for pre, course in prerequisites:
            indegree[course] += 1
        stack = [course for course in indegree if indegree[course] == 0]
        visited = 0
        while stack:
            course = stack.pop()
            visited += 1
            node = course_dict[course]
            if node.next and indegree[node.next.course] > 0:
                indegree[node.next.course] -= 1
                if indegree[node.next.course] == 0:
                    stack.append(node.next.course)
        return visited == len(courses)
```

## Test Cases

```python
def check(candidate):
    assert candidate([1, 2, 3], [(1, 2), (2, 3)]) == True
    assert candidate([1, 2, 3], [(1, 2), (2, 3), (3, 1)]) == False
    assert candidate([1, 2, 3, 4], [(1, 2), (2, 3), (3, 4)]) == True
    assert candidate([], []) == True
    assert candidate([1, 2], [(1, 2), (2, 1)]) == False
```

## Entry Point

`snake_concert_planner`

