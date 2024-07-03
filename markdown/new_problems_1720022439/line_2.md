# Task ID: hard/5

## Topics

['Line Sweep', "Kosaraju's Algorithm", 'Bloom Filter']

## Cover Story

['mystic monastery', 'arctic']

## Prompt

```python
def find_secret_artifacts(locations, connections, photos):
    """
    In a remote arctic monastery near the north pole, there are several sacred locations scattered across the area where ancient artifacts are hidden. These locations are identified by coordinates on a 2D plane. The connections between locations are provided which indicate paths that need to be cleared of snow to access the artifacts. Each connection is bidirectional.

    As a part of an initiation ritual, scholars need to find out if it's possible to clear a path to collect all artifacts from all the sacred locations. The monastery uses ancient blueprints (represented as photos), which are noisy binary images (0s and 1s) representing large artifacts. Each image corresponds to one location, and major artifacts appear as large connected components of 1s in the image.

    To determine if a complete path can be established, use the following methods:
    - Use Kosaraju’s Algorithm to check if all locations are strongly connected when considering the given `connections`.
    - Use a Line Sweep Algorithm to determine the complexity of each area around the locations based on the number of major artifacts identified in the photos using a Computer Vision connected components algorithm.
    - Store the analysis results efficiently using a Bloom Filter to filter locations with major artifacts for quick checks.

    Implement the function such that it returns True if it is possible to establish a complete path to collect all artifacts (assuming that Kosaraju's and Line Sweep results are favorable) and False otherwise.

    Example:
    locations = [(0,0), (2,3), (5,5)]
    connections = [(0, 1), (1, 2)]
    photos = [
        [[0, 1], [1, 1]], # Photo for location 0
        [[1, 0], [0, 0]], # Photo for location 1
        [[0, 0], [0, 1]]  # Photo for location 2
    ]
    The function should return True since there is a direct path covering all locations and at least one major artifact can be detected from the photos.
    """

```

## Cleaned Prompt

```python
Determine if all sacred locations in a remote arctic monastery can be strongly interconnected for initiating access to artifacts using Kosaraju’s Algorithm, Line Sweep Algorithm, and Bloom Filters.
Example:
locations = [(0,0), (2,3), (5,5)]
connections = [(0, 1), (1, 2)]
photos = [
    [[0, 1], [1, 1]], # Photo for location 0
    [[1, 0], [0, 0]], # Photo for location 1
    [[0, 0], [0, 1]]  # Photo for location 2
]
Return True or False denoting if artifact paths can be entirely connected and major artifacts are detected at these coordinates.
```

## Warnings

- Solution failed correctness check.
- 4, Misaligned Algorithms: The problem statement introduces three separate algorithms (Kosaraju's Algorithm for strong connectivity, Line Sweep Algorithm for artifact detection complexity, and Bloom Filter for efficient storage) but provides no clear explanation on how these are feasibly integrated within the provided function description. Specifically, the Line Sweep Algorithm's usage is ambiguous as the canonical solution instead uses traditional Computer Vision blob detection which contradicts or does not align with Line Sweep methods typically used for geometric computations rather than image processing tasks.
- 5, Lack of Clear Problem Specifications: The problem does not clearly define what constitutes as a "major artifact" in images, nor how to quantify or qualify a connection between artifacts and location connectivity for the artifact collection mentioned. Without these critical definitions, implementing the function or understanding the requirements for successful artifact path clearing is vague and open-ended, leading to possible incorrect implementations.
- 4, Inconsistent Implementation Details: The use of a Bloom Filter for checking if major artifacts are present is unusual and not typically suitable for this task. Bloom Filters are probabilistic and not typically used for definite data checks (where exact matches are critical) such as confirming the existence of major artifacts, which could lead to incorrect conclusions about artifact presence due to the inherent possibility of false positives in Bloom Filters.
- 5, Unrealistic Application of Kosaraju's Algorithm: The task confusingly uses Kosaraju's Algorithm, which is specific for strongly connected components in directed graphs, but the problem context and the example given (using undirected edges) suggest an undirected graph (since each connection is bidirectional), making Kosaraju's application misleading and inappropriate.

## Canonical Solution

```python
    import cv2
    import numpy as np
    from scipy.sparse.csgraph import csgraph_from_dense, connected_components

    def is_strongly_connected(connections, num_locations):
        matrix = np.zeros((num_locations, num_locations), dtype=int)
        for conn in connections:
            matrix[conn[0], conn[1]] = 1
            matrix[conn[1], conn[0]] = 1
        graph = csgraph_from_dense(matrix, null_value=0)
        n_components, labels = connected_components(graph, connection='strong')
        return n_components == 1

    def detect_major_artifacts(photo):
        # Using connectedComponentsWithStats to find blobs
        _, _, stats, _ = cv2.connectedComponentsWithStats(np.array(photo, dtype=np.uint8))
        # Considering a blob major if it has area > 1
        major_artifacts = sum(1 for _, _, _, _, area in stats[1:] if area > 1)
        return major_artifacts > 0

    def check_bloom_filter(locations, photos, bf_size=1000):
        bloom_filter = set()
        major_found = False
        # Assuming simple hash function for bloom filter
        hash_func = lambda x: hash(x) % bf_size
        for loc, photo in zip(locations, photos):
            if detect_major_artifacts(photo):
                bloom_filter.add(hash_func(loc))
                major_found = True
        return major_found

    def find_secret_artifacts(locations, connections, photos):
        if not is_strongly_connected(connections, len(locations)):
            return False
        if not check_bloom_filter(locations, photos):
            return False
        return True
```

## Test Cases

```python
def check(candidate):
    # Test cases will reflect the complexity and cover different scenarios including edge and generic cases.

    # All locations are connected and at least one major artifact is detected
    assert candidate([(0,0), (2,2), (3,4)], [(0, 1), (1, 2)], [[[0,1],[1,1]], [[0,0],[0,1]], [[1,0],[1,1]]]) is True

    # Locations are not strongly connected
    assert candidate([(0,0), (10,10), (20,20)], [(0, 1)], [[[1,0],[0,1]], [[0,1],[1,0]], [[1,1],[1,1]]]) is False

    # Locations are connected but no major artifacts
    assert candidate([(0,0), (5,5), (10,10)], [(0, 1), (1, 2)], [[[0,0],[0,0]], [[0,0],[0,0]], [[0,0],[0,0]]]) is False

    # Only one location with everything as an artifact
    assert candidate([(0,0)], [], [[[1,1],[1,1]]]) is True

    # Dense connectivity and multiple major artifacts
    assert candidate([(0,0), (2,2), (5,5), (10,10)], [(0, 1), (1, 2), (2, 3), (3, 0)], [[[0,1],[1,1]], [[1,1],[1,1]], [[1,0],[1,1]], [[1,1],[1,1]]]) is True
```

## Entry Point

`find_secret_artifacts`

