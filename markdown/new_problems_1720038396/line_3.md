# Task ID: hard/4

## Topics

['Skip List', 'Doubly-Linked List']

## Cover Story

['archaeological dig', 'ancient civilization']

## Prompt

```python
def decipher_artifacts(artifacts, queries):
    """
    As an archaeologist studying the ancient Azulitus civilization, you encounter inscriptions believed to contain hidden structures akin to a combination of a Skip List and a Doubly-Linked List.

    Each inscription is linked both forward and backward, and also incorporates 'express lanes' or skip links that jump across multiple inscriptions. Your task is to execute queries on these inscriptions to unravel and document the numeric sequences.

    Input Details:
    - `artifacts`: a list of tuples representing numeric sequences, where each tuple consists of (value, next_index, skip_index).
        'value' is the numeric inscription value.
        'next_index' refers to the linearly next inscription.
        'skip_index' leads to a further inscription, imitating a skip list link.
    - `queries`: a list of queries, where each query is a tuple (start_index, end_index, type).
        'type' specifies the query mode:
            'sum' - computes the sum between start_index and end_index inclusive, using the regular links.
            'skip-sum' - computes the sum using skip links starting from start_index and includes standard sequential links to reach end_index.

    Your goal is to implement the function decipher_artifacts, which processes each query and returns a list containing the results.

    Example:
    - artifacts = [(3,1,2), (4,2,-1), (2,-1,-1)]
    - queries = [(0,2,'sum'), (0,1,'skip-sum')]
    - Expected Output: [9, 5]
         For (0,2,'sum'), the path is 3 -> 4 -> 2 (sum = 9).
         For (0,1,'skip-sum'), the path is 3 (via skip) -> 2 (sum = 5).

    Note: A value of -1 in next_index or skip_index indicates the terminus of links in that respective direction.
    """
```

## Cleaned Prompt

```python
Write a function to simulate a combination of a Skip List and a Doubly-Linked List structure from artifacts data, and process queries summing the values accordingly. Given sequence artifacts are described as tuples (value, next_index, skip_index) and queries determine which indices and type of connection ('sum' or 'skip-sum') to use for summing. Indices -1 indicate the end of links.
```

## Warnings

- Solution failed correctness check.
- 5, Inconsistent and incorrect example output: The example output provided in the prompt description contradicts the explanation of the operations involved and also appears incorrect based on given logic. The example describes the output for `(0,1,'skip-sum')` should be `7` but following the explanation it should be `5` because the traversal using skip links from index `0` to index `1` should include elements `3` and `2` only.
- 5, Faulty logic in canonical solution: The traversal logic in the canonical solution does not correctly handle the condition where the current index moves beyond the `end` index when using skip links. This leads to accumulating values that are not within the specified range, which can result in incorrect query results.

## Canonical Solution

```python
def build_structure(artifacts):
        max_idx = len(artifacts)-1
        nodes = {}
        for i, artifact in enumerate(artifacts):
            node = {'value': artifact[0], 'next': artifact[1] if artifact[1] <= max_idx else None, 'skip': artifact[2] if artifact[2] <= max_idx else None}
            nodes[i] = node
        return nodes

    def traverse(nodes, start, end, use_skip=False):
        current = start
        result = 0
        while current is not None and current <= end:
            result += nodes[current]['value']
            if use_skip and nodes[current]['skip'] is not None and nodes[current]['skip'] <= end:
                current = nodes[current]['skip']
            else:
                current = nodes[current]['next']
        return result

    nodes = build_structure(artifacts)
    results = []
    for start, end, q_type in queries:
        if q_type == 'sum':
            results.append(traverse(nodes, start, end))
        elif q_type == 'skip-sum':
            results.append(traverse(nodes, start, end, use_skip=True))
    return results
```

## Test Cases

```python
def check(candidate):
    assert candidate([(3, 1, 2), (4, 2, -1), (2, -1, -1)], [(0, 2, 'sum'), (0, 1, 'skip-sum')]) == [9, 5]
    assert candidate([(10,1,-1), (20,2,1), (30,-1,-1)], [(0,2,'sum'), (0,2,'skip-sum')]) == [60, 50]
    assert candidate([(5,1,2), (-5,2,-1), (10,-1,-1)], [(0,1,'sum'), (1,1,'skip-sum')]) == [0, -5]
    assert candidate([(7,1,-1), (3,2,1), (2,-1,2), (8,-1,-1)], [(0,3,'sum'), (0,0,'skip-sum')]) == [20, 7]
    assert candidate([(1,1,-1), (1,1,0), (1,1,-1)], [(0,0,'sum'), (0,2,'skip-sum')]) == [1, 3]
```

## Entry Point

`decipher_artifacts`

