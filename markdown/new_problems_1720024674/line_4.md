# Task ID: hard/3

## Topics

['Memoization', 'Merge k Sorted Lists']

## Cover Story

['lost city', 'wise old tree']

## Prompt

```python
def recover_artifacts(artifact_images, artifact_connections):
    """
    In the folklore of an ancient lost city, it is said that there exists a wise old tree that holds the knowledge of the city's once-thriving artifacts. These artifacts are scattered around the world, and legends suggest that if one could merge the stories of these artifacts in the correct order, the location of the city could be found.

    You have been provided with two inputs:
    - artifact_images: A list of lists of matrices (numpy arrays) where each matrix represents a greyscale image of an artifact.
    - artifact_connections: A list of tuples (a, b), representing that the artifact image_list 'a' must be merged after artifact image_list 'b'.

    Your task is to merge the artifact image lists in an order consistent with the provided 'artifact_connections' requirements. The merging should respect the constraints of 'artifact_connections' implying a clean, sequential manner to reveal a final M x N matrix representing the full picture of the artifacts combined.

    Additionally, use memoization to efficiently handle repetitive computations while merging these images. Apply image processing techniques to accurately merge them without data distortion.

     Further Considerations:
    - Every single artifact in 'artifact_images' represents a sequence of artifact conditions through time presented as a series of matrices.
    - The merged result must be a single matrix which is the composition of all these image lists in a sequence dictated by 'artifact_connections'.
    - Use numpy for matrix operations.
    - Assume all matrices within each list are of equal dimensions MxN and all merge operations work on matrices of the same size.
    
    Example:
    if artifact_images = [
        [np.array([[1, 1], [1, 1]]), np.array([[2, 2], [2, 2]])],
        [np.array([[3, 3], [3, 3]])],
        [np.array([[4, 4], [4, 4]])]
    ]
    and artifact_connections = [(1, 0), (2, 1)]

    The correct order of merging would be list 0 -> list 1 -> list 2 which means:
    - First, [np.array([[1, 1], [1, 1]]), np.array([[2, 2], [2, 2]])],
    - Next,  [np.array([[3, 3], [3, 3]])],
    - Finally, [np.array([[4, 4], [4, 4]])].

    """
```

## Cleaned Prompt

```python
Define a function recover_artifacts that takes a list of lists of matrices where each matrix is a greyscale image of an artifact and a list of tuples representing a mandatory merge order. Merge these matrices respecting this order to reveal a final composition that unveils more information.
```

## Warnings

- Only 3 test cases found. Minimum recommended is 5.
- Solution failed correctness check.
- 4, Unclear Merge Mechanism: The problem description ambiguously outlines how the matrices should be merged. Beyond saying that matrices should be merged in a sequence, it doesn’t specify the merge operation - sum, average, max, etc. This lack of definition could lead to different interpretations of the required output.
- 4, Vague Use of Memoization: While the prompt suggests using memoization to manage repetitive computations, it doesn't specify which part of the computation is repetitive and would benefit from memoization. This could lead to incorrect implementations, especially since matrix operations can be computationally expensive without clear guidance.

## Canonical Solution

```python
    import numpy as np
    def merge_images(images):
        return np.sum(images, axis=0)

    def compute_merge_order(connections):
        from collections import defaultdict, deque
        in_degree = defaultdict(int)
        graph = defaultdict(list)
        for child, parent in connections:
            graph[parent].append(child)
            in_degree[child] += 1
        # 0 in-degree means no dependency, can process
        process_queue = deque([k for k in range(len(images)) if in_degree[k] == 0])
        order = []
        while process_queue:
            node = process_queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    process_queue.append(neighbor)
        return order

    def recover_artifacts(artifact_images, artifact_connections):
        order = compute_merge_order(artifact_connections)
        merged_artifact = np.zeros(artifact_images[0][0].shape)
        for idx in order:
            image_list = artifact_images[idx]
            merged_image = merge_images(image_list)
            merged_artifact += merged_image
        return merged_artifact

```

## Test Cases

```python
def check(candidate):
    import numpy as np
    test_artifacts1 = [
        [np.array([[1, 1], [1, 1]]), np.array([[2, 2], [2, 2]])],
        [np.array([[3, 3], [3, 3]])],
        [np.array([[4, 4], [4, 4]])]
    ]
    test_connections1 = [(1, 0), (2, 1)]
    test_result1 = np.array([[10, 10], [10, 10]])
    assert np.array_equal(candidate(test_artifacts1, test_connections1), test_result1)

    test_artifacts2 = [
        [np.array([[2, 2], [3, 3]])],
        [np.array([[0, 0], [1, 1]])],
        [np.array([[4, 4], [5, 5]])]
    ]
    test_connections2 = [(2, 0)]
    test_result2 = np.array([[6, 6], [9, 9]])
    assert np.array_equal(candidate(test_artifacts2, test_connections2), test_result2)

    assert np.array_equal(candidate([], []), np.zeros((0, 0)))

    check(recover_artifacts)
```

## Entry Point

`recover_artifacts`

