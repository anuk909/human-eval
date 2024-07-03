# Task ID: hard/1

## Topics

['Meeting Rooms', 'Line Sweep', 'Quadtree']

## Cover Story

['music', 'courtroom']

## Prompt

```python
def song_segmentation(frequencies, timestamps, threshold):
    """
    Imagine a court case where the authenticity of various musical recordings is in dispute. The challenge is to develop a software that detects changes in the music's tonality within a recording, which may indicate splicing or editing.

    Each recording is represented by two lists: frequencies and timestamps. The 'frequencies' list contains the dominant frequency (in Hz) at each sampled time point, and the 'timestamps' list contains the corresponding times (in seconds) of these samples. Additionally, you are given a 'threshold' which is the frequency deviation above which a change in the song segment is considered significant.

    Your task is to write a function that returns a list of tuples. Each tuple represents a continuous segment of the song where the frequency stays consistent (within the given threshold). Each tuple should contain the starting and ending time of that segment.

    Example:
    - If `frequencies` = [440.5, 442.1, 441.0, 600.3, 602.2, 800.0, 799.1, 600.4],
    - And `timestamps` = [0, 1, 2, 5, 6, 10, 11, 15],
    - And `threshold` = 2.0, (meaning we allow frequency deviation up to 2 Hz as consistent)
    - The output should be [(0, 2), (5, 6), (10, 11), (15, 15)] since these intervals show consistent frequencies within the threshold.

    Constraints:
    - The lengths of the 'frequencies' and 'timestamps' lists are the same.
    - All entries in 'frequencies' are non-negative floats.
    - All entries in 'timestamps' are non-negative integers and are strictly increasing.

    Note: If a segment consists of a single sample, it should be represented with the start and end time being the same.
    """

```

## Cleaned Prompt

```python
Write a function that takes two lists 'frequencies' and 'timestamps' and a 'threshold', and returns a list of tuples representing continuous segments in a musical recording where the frequency remains consistent within the given threshold. Each tuple should represent the start and end time of each segment where the frequency deviation is within the threshold.

Example:
Given the input lists of frequencies [440.5, 442.1, 441.0, 600.3, 602.2, 800.0, 799.1, 600.4], timestamps [0, 1, 2, 5, 6, 10, 11, 15], and threshold 2.0, the output should be [(0, 2), (5, 6), (10, 11), (15, 15)].
```

## Warnings

- Solution failed correctness check.
- 4, Edge Case Ambiguity: The problem statement does not specify how to handle edge cases where the input lists are empty. An explicit definition of expected behavior for edge cases like empty input lists would avoid ambiguity in the function implementation. For example, if both `frequencies` and `timestamps` are empty, should the function return an empty list or should it raise an error?

## Canonical Solution

```python
    from collections import deque

    def song_segmentation(frequencies, timestamps, threshold):
        if not frequencies or not timestamps:
            return []

        # Initialize
        current_freq = frequencies[0]
        start_time = timestamps[0]
        end_time = timestamps[0]
        result = []

        for i in range(1, len(frequencies)):
            if abs(frequencies[i] - current_freq) <= threshold:
                end_time = timestamps[i]
            else:
                result.append((start_time, end_time))
                current_freq = frequencies[i]
                start_time = timestamps[i]
                end_time = timestamps[i]

        result.append((start_time, end_time))
        return result
```

## Test Cases

```python
def check(candidate):
    assert candidate([440.5, 442.1, 441.0, 600.3, 602.2, 800.0, 799.1, 600.4], [0, 1, 2, 5, 6, 10, 11, 15], 2.0) == [(0, 2), (5, 6), (10, 11), (15, 15)]
    assert candidate([], [], 1.0) == []
    assert candidate([400], [0], 3.0) == [(0, 0)]
    assert candidate([300, 304.5, 310], [0, 5, 10], 5.0) == [(0, 5)]
    assert candidate([100, 150, 400, 850], [0, 2, 5, 7], 50) == [(0, 2), (5, 5), (7, 7)]
```

## Entry Point

`song_segmentation`

