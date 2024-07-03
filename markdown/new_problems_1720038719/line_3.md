# Task ID: hard/1

## Topics

['Two Pointers', 'Reverse Linked List']

## Cover Story

['spicing up menu', 'batch grouping of recipes']

## Prompt

```python
def reverse_linked_list_by_group(head, k):
    """
    Imagine a chef named Alex who needs to arrange a set menu from a collection of recipe cards arranged in a specific order. He decides to spice things up by grouping the recipes in batches of 'k' and reversing the order of recipes within each group to make the menu more interesting.

    Representing each recipe by a node in a singly linked list, where each node holds a number denoting the recipe, your task is to write a function that reverses the nodes of the singly linked list in groups of size 'k' and returns the modified list's head. If the number of nodes is not a multiple of k, the last remaining nodes should be left as they are.

    The Node class is defined as:
    class Node:
        def __init__(self, value=0, next=None):
            self.value = value
            self.next = next

    Example:
    If k=3 and the list is 1->2->3->4->5->6->7, the output should be 3->2->1->6->5->4->7.
    If k=2, list is 1->2->3->4->5, the output should be 2->1->4->3->5.

    Constraints:
    - 1 <= list length <= 5000
    - 1 <= k <= list length

    Note:
    - You should not use extra space for another data structure, although variables to track nodes are allowed.
    """

```

## Cleaned Prompt

```python
def reverse_linked_list_by_group(head, k):
    """
    Write a function to reverse nodes of a singly linked list in groups of size 'k'. If the number of nodes is not a multiple of k, leave the remaining nodes as they are. Each node in the list does not need to be in any particular order. There should be no use of extra space for another data structure.

    Example:
    If k=3, list is 1->2->3->4->5->6->7, expected output is 3->2->1->6->5->4->7.
    If k=2, list is 1->2->3->4->5, expected output is 2->1->4->3->5.
    """

```

## Warnings

- Solution failed correctness check.
- 5, Imaginary Context in Prompt: The problem description unnecessarily includes a story about a chef named Alex arranging menu items, which is confusing and unrelated to the actual coding task of reversing nodes in a linked list. This could mislead participants and detract from understanding the core task.

## Canonical Solution

```python
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list_by_group(head, k):
    if not head or k == 1:
        return head
    dummy = Node(0, head)
    group_prev = dummy
    
    while True:
        kth = group_prev
        count = 0
        while count < k and kth:
            kth = kth.next
            count += 1
        if not kth:
            break

        group_start = group_prev.next
        prev = kth.next
        curr = group_start
        
        while curr != kth.next:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        group_prev.next = prev
        group_prev = group_start
    
    return dummy.next
```

## Test Cases

```python
def check(candidate):
    def list_to_linked(lst):
        if not lst:
            return None
        head = Node(lst[0])
        current = head
        for element in lst[1:]:
            current.next = Node(element)
            current = current.next
        return head

    def linked_to_list(head):
        lst = []
        current = head
        while current:
            lst.append(current.value)
            current = current.next
        return lst

    # Test cases
    assert linked_to_list(candidate(list_to_linked([1, 2, 3, 4, 5, 6, 7]), 3)) == [3, 2, 1, 6, 5, 4, 7]
    assert linked_to_list(candidate(list_to_linked([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]
    assert linked_to_list(candidate(list_to_linked([1]), 1)) == [1]
    assert linked_to_list(candidate(list_to_linked([1, 2, 3, 4, 5, 6]), 1)) == [1, 2, 3, 4, 5, 6]
    assert linked_to_list(candidate(list_to_linked([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 4)) == [4, 3, 2, 1, 8, 7, 6, 5, 12, 11, 10, 9]
```

## Entry Point

`reverse_linked_list_by_group`

