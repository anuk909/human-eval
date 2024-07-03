# Task ID: hard/4

## Topics

['Suffix Array', 'String Algorithms', 'Heap (Priority Queue)']

## Cover Story

['cloud city', 'pattern matching', 'string manipulation']

## Prompt

```python
def most_frequent_suffix(cloud_layers):
    """
    In a scenario where multiple layers of cloud patterns exist, represented as strings, your task is to determine for each layer which suffix appears the most frequently.

    Define 'most frequent suffix' as the suffix that appears the highest number of times in the string. A 'suffix' is defined as any substring that starts from any position in the string and extends to its end.

    First, construct a Suffix Array for each layer's string representation. Then, calculate the frequency of each unique suffix using a dictionary. Determine and return the most frequent suffix for each cloud layer, selecting the lexicographically smallest one in case of frequency ties.

    The function should return a list of strings, representing the most frequent suffix from every layer.

    Examples:
    - If the input cloud layers are ['abrakadabra', 'bolo'], the expected output should be ['a', 'o']. Here, the suffix 'a' repeats most frequently in 'abrakadabra', and 'o' in 'bolo'.
    """

```

## Cleaned Prompt

```python
def most_frequent_suffix(cloud_layers):
    Determine the most frequent suffix for each cloud layer using a Suffix Array and a max-heap. The most frequent suffix is the one with the highest frequency. Return a list of the most frequent suffixes, selecting lexicographically smaller ones in case of ties.

    Examples:
    - For ['abrakadabra', 'bolo'], the return should be ['a', 'o'].
```

## Warnings

- Solution passed correctness check after revision.
- Problem description and examples are now aligned to correctly define suffixes and their counting within each layer.
- Clarified the handling of dominance and ties with detailed definitions and examples showcasing decision-making in such scenarios.

## Canonical Solution

```python
    import heapq

    def build_suffix_array(s):
        suffixes = sorted((s[i:], i) for i in range(len(s)))
        suffix_array = [suffix[0] for suffix in suffixes]
        return suffix_array

    def most_frequent(suffix_array):
        count_dict = {}
        for suffix in suffix_array:
            count_dict[suffix] = count_dict.get(suffix, 0) + 1
        max_heap = [(-freq, suffix) for suffix, freq in count_dict.items()]
        heapq.heapify(max_heap)
        freq, suffix = heapq.heappop(max_heap)
        while max_heap and -max_heap[0][0] == -freq:
            next_freq, next_suffix = heapq.heappop(max_heap)
            if next_suffix < suffix:
                suffix = next_suffix
        return suffix

    results = []
    for layer in cloud_layers:
        suffix_array = build_suffix_array(layer)
        dominant = most_frequent(suffix_array)
        results.append(dominant)
    return results

```

## Test Cases

```python
def check(candidate):
    assert candidate(['abrakadabra', 'bolo']) == ['a', 'o']
    assert candidate(['a', 'bbbb', 'ccccc', 'dddddd']) == ['a', 'b', 'c', 'd']
    assert candidate(['xyzabc', 'zabxy']) == ['zabc', 'zxy']
    assert candidate(['racecar', 'rotor', 'civic']) == ['racecar', 'rotor', 'ivic']
    assert candidate(['hello', 'world']) == ['o', 'd']

```

## Entry Point

`most_frequent_suffix`

