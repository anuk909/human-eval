# Task ID: hard/1

## Topics

['Linked List Cycle', '3-Sum Problem']

## Cover Story

['library', "sorcerer's tower"]

## Prompt

```python
def sorcerers_library(tomes, enchantments):
    """
    In an ancient sorcerer's tower, there's a unique library filled with magical tomes. Each tome details an enchantment technique encoded as an integer. A sorcerer apprentice discovered that the tomes have been enchanted and thus, form a magical link among themselves.

    These links create a magical formation where three specific tomes' enchantments, when summed, produce a magical glyph (a value of 0). The tomes themselves are arranged in a complex spiral linked list structure. The apprentice suspects that this linked list has a cycle formed by a corrupt magic that must be broken to stop the enchantments from causing havoc.

    You need to write a function that explores this list of tomes, represented by list 'tomes', and list 'enchantments', which represents the enchantments as integers on each tome. You'll need to find a triplet of integers among the enchantments that sum to zero, and also detect if there's a cycle in the linked list structure where each node points to a next tome, using the integer list form as indices.

    Your solution should return a tuple (contains_cycle, zero_sum_triplet_exists).

    Examples:
    If 'tomes' = [1, 4, 3, 2, 0] and 'enchantments' = [-1, 0, 2, -3, 1], the output should be (True, True) as there's a cycle (0->1->4->0) and the triplet (-1, 2, -3) corresponding to indices (0, 2, 3) sum to zero.

    Note:
    - The 'tomes' list will be non-empty and have length equal to 'enchantments'.
    """

```

## Cleaned Prompt

```python
Write a function that takes two lists: 'tomes' which represents indices pointing to other indices in the same list forming a linked list, and 'enchantments' which are integers associated with each tome. Your function should determine if a cycle exists in the linked list represented by 'tomes' and whether any triplet of integers in 'enchantments' sums to zero. The function should return a tuple (contains_cycle, zero_sum_triplet_exists). Implement a function that efficiently addresses both problems considering the distinct constraints. Example: for tomes [1, 4, 3, 2, 0] and enchantments [-1, 0, 2, -3, 1], return (True, True).
```

## Warnings

- Solution failed correctness check.
- 5, Unclear Data Structure Description: The problem description does not adequately explain the structure or expected values within the 'tomes' list, particularly how they represent a "complex spiral linked list." It also assumes knowledge that indices can refer to other indices, which isn't a usual interpretation and may confuse participants unfamiliar with such representations.
- 5, Problem Complexity Misalignment: The task combines the detection of a cycle in a linked list and finding a zero-sum triplet, which are significantly different in complexity, potentially leading to confusion over the focus required to address each sub-problem effectively. This could affect the design of an efficient solution and is not typical in competitive programming where problems usually focus on a single clear objective.
- 4, Inconsistent Example Mapping to Problem Description: In the given examples, there's an implied assumption that elements in 'tomes' are always valid indices within its own range (e.g., no index out of bound errors), but there's no explicit guarantee mentioned in the problem description that 'tomes' will not contain out-of-range values. This might lead to runtime errors in implementations if not properly handled.

## Canonical Solution

```python
def sorcerers_library(tomes, enchantments):
    def has_cycle(node):
        slow = tomes[node]
        fast = tomes[tomes[node]]
        while fast != slow:
            if fast == tomes[fast]: break # detecting self-loop
            fast = tomes[tomes[fast]]
            slow = tomes[slow]
        return fast == slow

    def three_sum_zero(enchantments):
        enchantments.sort()
        n = len(enchantments)
        for i in range(n):
            if i > 0 and enchantments[i] == enchantments[i - 1]: continue
            l, r = i + 1, n - 1
            while l < r:
                sum_lr = enchantments[i] + enchantments[l] + enchantments[r]
                if sum_lr == 0: return True
                elif sum_lr < 0: l += 1
                else: r -= 1
        return False

    contains_cycle = has_cycle(0)
    zero_sum_triplet_exists = three_sum_zero(enchantments)

    return (contains_cycle, zero_sum_triplet_exists)
```

## Test Cases

```python
def check(candidate):
    assert candidate([1, 4, 3, 2, 0], [-1, 0, 2, -3, 1]) == (True, True)
    assert candidate([0, 2, 3, 4, 1], [5, 1, -2, -4, 0]) == (True, True)
    assert candidate([2, 0, 3, 4, 1], [1, -1, 1, -1, 0]) == (False, False)
    assert candidate([3, 2, 0, 1], [-1, 2, -3, 2]) == (False, True)
    assert candidate([0, 1, 2, 3], [0, 0, 0, 0]) == (False, True)
```

## Entry Point

`sorcerers_library`

