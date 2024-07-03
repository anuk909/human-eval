# Task ID: hard/2

## Topics

['Permutations', 'Bitwise AND Operations']

## Cover Story

['farm', 'cyber cafe']

## Prompt

```python
def detect_farm_cams(image_data, camera_positions, permute_sequence):
    """
    In a futuristic farming scenario, Mr. Roboto has automated cameras positioned at specific coordinates in the farm. Each camera sends its image data as a stream of integers. Additionally, a permutation sequence is applied directly to the 'image_data' based on the camera positions to encrypt the data before it is transmitted for processing.

    Your task is to:
    1. Permute the `image_data` according to `permute_sequence`.
    2. Compute the pixel-average over bitwise AND of all permuted streams.

    Parameters:
    - image_data: A list of lists, where each sublist represents the pixel data from a camera.
    - camera_positions: A list of integer tuples (x, y) for camera positions (Note: for contextual purposes only).
    - permute_sequence: A list of indices that describes how to permute `image_data` based on `camera_positions`.

    The function should return the average of the bitwise AND results across all pixel data of the streams after applying the permutation sequence.

    Example:
    image_data = [[0xFF, 0xEE], [0xCC, 0xDD]]
    camera_positions = [(10, 20), (30, 40)]
    permute_sequence = [1, 0]
    Output should be 204 since:
    After permutation of image_data = [[0xCC, 0xDD], [0xFF, 0xEE]]
    Bitwise AND across the streams: [0xCC & 0xFF, 0xDD & 0xEE] = [0xCC, 0xCC]
    Average of [0xCC, 0xCC] is 204.

    Note:
    - All lists will be non-empty and all sublists in image_data will be of the same length.
    - Permute sequence will cover all indices of image_data exactly once.
    """
```

## Cleaned Prompt

```python
Write a function `detect_farm_cams` that takes three parameters `image_data`, `camera_positions`, and `permute_sequence`. The function should permute the camera_positions according to `permute_sequence`, compute the bitwise AND across all streams according to the new order and then return the average of results.

Examples:
- For `image_data = [[0xFF, 0xEE], [0xCC, 0xDD]]`, `camera_positions = [(10, 20), (30, 40)]`, and `permute_sequence = [1, 0]`, this returns 204.
- All input lists will be non-empty and permute sequence will cover all indices of camera_positions once. Assume all sublists in image_data are of the same length.
```

## Warnings

- Solution failed correctness check.
- 5, Logic Error in Canonical Solution: The problem description specifies that the cameras' pixel data should be permuted in the order given by `permute_sequence` before computing the bitwise AND. However, the canonical solution permutes the camera positions instead and does not permute the `image_data`, which leads to using the pixel data in the wrong order for bitwise AND operations, resulting in incorrect output.
- 4, Unclear Parameters Role: The problem statement and canonical solution use the `camera_positions` for permuting the order but do not utilize the actual coordinates (x, y) in any computation, making it unclear why these coordinates are needed or how they contribute to the solution, potentially causing confusion.

## Canonical Solution

```python
    def detect_farm_cams(image_data, camera_positions, permute_sequence):
        # Permute image_data according to the permute_sequence
        permuted_data = [image_data[i] for i in permute_sequence]

        # Initialize the result for bitwise AND operations
        if permuted_data:
            bitwise_result = [0xFFFFFFFF] * len(permuted_data[0])
            for data in permuted_data:
                bitwise_result = [x & y for x, y in zip(bitwise_result, data)]

        # Calculate average of bitwise results
        average_result = sum(bitwise_result) // len(bitwise_result)
        return average_result
```

## Test Cases

```python
def check(candidate):
    assert candidate([[0xFF, 0xEE], [0xCC, 0xDD]], [(10, 20), (30, 40)], [1, 0]) == 204
    assert candidate([[0xF0, 0x0F], [0x0F, 0xF0]], [(5, 5), (10, 10)], [1, 0]) == 15
    assert candidate([[0xAA, 0xBB], [0xCC, 0xDD]], [(7, 7), (8, 8)], [0, 1]) == 170
   assert candidate([[0xFF], [0xEF], [0xDF]], [(1, 2), (2, 3), (3, 4)], [2, 1, 0]) == 223
    assert candidate([[0x123, 0x234], [0x345, 0x456]], [(15, 25), (35, 45)], [0, 1]) == 837
```

## Entry Point

`detect_farm_cams`

