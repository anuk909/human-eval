# Task ID: hard/4

## Topics

['Linked List Cycle', 'Skip List']

## Cover Story

['dungeon', 'restaurant']

## Prompt

```python
def escape_plan(plans):
    """
    In a mystical RPG game, players navigate through dungeons that have magically enhanced security systems.
    Each dungeon security system is represented by a special linked list called a 'Skip List'.

    A skip list enhances a regular linked list by adding 'forward links' in addition to the 'next' link.
    These forward links allow quick jumps over several nodes promoting fast access and quick escapes.
    Each node in the list also captures images from the room it represents using infrared.

    To escape the dungeon, players need to find if any cycle exists using the regular 'next' links. If a cycle exists,
    adventurers can exploit the repeating sequence to trick the infrared cameras by looping unexpectedly, causing the cameras to desynchronize and allowing escape.

    Your function should receive a skip list (represented in a simplified form as a list of tuples where each tuple is (node_value, next_index, optional_forward_index)) 
    and return True if a cycle is detected in the 'next' links and False otherwise. The 'next_index' and 'optional_forward_index' are the indices in the list representing the respective links. A 'None' value in these indices indicates no link.

    Example:
    Input: [(0, 1, None), (1, 2, 4), (2, None, None), (3, 4, None), (4, 1, None)]
    It represents a list where:
      - Node with value 0 points to node with value 1. Node 0 has no forward link.
      - Node 1 points to node 2 and has a forward link to node 4.
      - Node 2 has no next or forward link.
      - Node 3 points to node 4 and has no forward link.
      - Node 4 points back to node 1, forming a cycle.

    Output: True - because there is a cycle (1 -> 2 -> None -> 4 -> 1).

    Note: Consider using techniques from computer vision like synchronicity problems to think about how adventurers could exploit the cycle.
    """
```

## Cleaned Prompt

```python
Write a function that takes a skip list (represented as a list of tuples (node_value, next_index, optional_forward_index)) and returns True if a cycle is detected in the 'next' links and False otherwise. A skip list is a linked list with additional forward links that allow for quick jumps over nodes.

Example: Input: [(0, 1, None), (1, 2, 4), (2, None, None), (3, 4, None), (4, 1, None)] meaning Node 0 points next to Node 1 and Node 1 points next to Node 2 and forward to Node 4, etc. Output: True as there's a cycle 1 -> 2 -> None -> 4 -> 1.
```

## Warnings

- Solution failed correctness check.
- 5, Unclear Problem Statement: The problem statement involves multiple confusing elements, potentially leading to misunderstandings about what is needed. The prompt includes non-relevant details about dungeons and magic, which does not add value to understanding the core problem of detecting cycles in skip lists.
- 4, Inconsistent Handling of 'None': The sample input allows for a 'None' index, implying that this makes a logical end to a linked chain. However, the problem setup and description do not clarify the expected behavior when such a 'next' link points to 'None'. This could cause incorrect implementations or interpretations of what constitutes a cycle.
- 4, Unspecified List Boundary Conditions: The prompt does not specify how out-of-range indices should be handled (i.e., if an index greater than list length is given). This can lead to confusion or inconsistency in implementing and understanding the cycle detection logic.

## Canonical Solution

```python
def escape_plan(plans):
    def detect_cycle(plans):
        slow = fast = 0
        while True:
            if slow is None or fast is None or plans[fast][1] is None:
                return False
            slow = plans[slow][1]
            fast = plans[fast][1]
            if plans[fast][1] is not None:
                fast = plans[fast][1]
            if slow == fast:
                return True
        return False
    return detect_cycle(plans)
```

## Test Cases

```python
def check(candidate):
    assert candidate([(0, 1, None), (1, 2, 4), (2, None, None), (3, 4, None), (4, 1, None)]) == True
    assert candidate([(0, 1, 2), (1, None, None), (2, None, None)]) == False
    assert candidate([(0, 1, None), (1, 2, None), (2, 0, None)]) == True
    assert candidate([]) == False
    assert candidate([(0, None, None),]) == False
    assert candidate([(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (5, 6, None), (6, 1, None)]) == True
```

## Entry Point

`escape_plan`

