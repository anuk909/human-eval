# Task ID: hard/2

## Topics

['Monotonic Queue', 'Minimum Spanning Tree']

## Cover Story

['weather machine', 'mystic monastery']

## Prompt

```python
def optimal_weather_pattern(deltas, k):
    """
    In a mystic monastery located atop a secluded mountain, monks have developed a weather machine that can alter the temperature of the surrounding area. The monastery is laid out in a linear fashion with 'k' weather stations positioned strategically. Connected by ley lines, they are meant to minimize the temperature variations across the stations when activated simultaneously.

    The machine operates by a series of 'n' potential temperature adjustments (deltas) that may be applied sequentially to these stations. Each delta represents a possible change (increase or decrease) in temperature. For safety and effectiveness, only a contiguous subarray of these deltas of size exactly 'k' can be used at any one operation.

    However, the ley lines work in such a way that activating the weather machines according to the selected deltas can create temperature imbalances unless selected optimally. The goal is to choose the contiguous subarray of changes that minimizes the maximum variation in temperature (calculated as the difference between the highest and lowest temperatures) when applied across the stations.

    For example, if deltas = [1, -3, 2, -4, 3, 5] and k = 3, applying the subarray [-3, 2, -4] would yield differences of [-3, 2, -4] with a maximum variation of 6 (from -4 to 2). The goal is to minimize this maximum variation.

    Thus, your goal is to find and return the minimum of the maximum variation that can be achieved by any choice of 'k' consecutive deltas.

    Note: 'k' will always be at least 1 and no greater than the length of 'deltas'.
    """
```

## Cleaned Prompt

```python
def optimal_weather_pattern(deltas, k):
    """
    Given a list of integers 'deltas' and an integer 'k', which represents the size of contiguous subarrays to be considered, find and return the minimum of the maximum variation that can be achieved across such 'k' consecutive deltas.
    """
```

## Canonical Solution

```python
    def optimal_weather_pattern(deltas, k):
        from collections import deque
        def min_sliding_window(arr, k):
            # Monotonic queue approach to find minimum in sliding window
            min_queue, max_queue = deque([]), deque([])
            minima, maxima = [], []

            for i in range(len(arr)):
                while min_queue and arr[min_queue[-1]] > arr[i]:
                    min_queue.pop()
                while max_queue and arr[max_queue[-1]] < arr[i]:
                    max_queue.pop()

                min_queue.append(i)
                max_queue.append(i)

                if min_queue[0] == i - k:
                    min_queue.popleft()
                if max_queue[0] == i - k:
                    max_queue.popleft()

                if i >= k - 1:
                    minima.append(arr[min_queue[0]])
                    maxima.append(arr[max_queue[0]])

            max_variation = [maxima[i] - minima[i] for i in range(len(minima))]
            return min(max_variation)

        return min_sliding_window(deltas, k)
```

## Test Cases

```python
def check(candidate):
    assert candidate([1, -3, 2, -4, 3, 5], 3) == 3
    assert candidate([-2, 1, -3, 4, -1, 2, 6], 2) == 3
    assert candidate([5, 3, 6, 1, 2], 4) == 5
    assert candidate([0, 0, 0, 0], 2) == 0
    assert candidate([1, 2, 3, 4, -5, 6, 7, -8], 5) == 8
    assert candidate([-5, -1, -2, 1, 2, 3], 3) == 3
```

## Entry Point

`optimal_weather_pattern`

## Warnings

- Solution failed correctness check.
- 5, Logical mismatch in problem definition: The problem prompt does not clearly link the operation of weather stations and the use of deltas onto them. It mentions "minimizes the maximum variation in temperature" but does not explain how these deltas are actually applied across the stations, leading to significant confusion about how the temperatures at various stations interact or compound.
- 5, Incorrect output explanation: The given examples and their explanations do not logically deduce the correct output for the optimal_weather_pattern function. For example, the explanation for deltas = [1, -3, 2, -4, 3, 5] and k = 3 implies a variation calculation error. The correct variation should involve looking at max and min differences properly computed which is not clearly happening.
- 4, Incomplete constraints and assumptions: The prompt assumes that the input deltas are appropriate for modification without specifying the valid range for these integers or considering edge cases like all elements being the same or all deltas being either all positive or all negative.

