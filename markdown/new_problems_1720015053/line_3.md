# Task ID: hard/1

## Topics

['Wavelet Tree', 'Bucket Sort']

## Cover Story

['haunted house', 'mystic monastery']

## Prompt

```python
def hidden_treasure_messages(messages):
    """
    After a thrilling adventure exploring haunted houses, you've discovered cryptic messages left by monks from a mystic monastery. These messages are routes to hidden treasure but are encoded in such a way that only prime numbered positioned words in each message when read backwards lead to the real path.

    The function 'hidden_treasure_messages' takes a list of string messages and requires to output a list of processed messages. Here's the process for each message:
    - Use wavelet trees to determine quickly the abundance of each word allowing to efficiently pick unique words later.
    - Sort the encoded messages using a modified bucket sort where even indices of each word have a prime number of occurrences determined via a wavelet tree.
    - Concatenate the selected words in reverse, separated by a single space.

    Example:
    Input: ['monastery golden coin', 'golden hidden routes', 'hidden treasure found']
    Output: ['nioc nedlog', 'setuor nedlog', 'dnuof erusaert']

    Constraints:
    - Messages can have up to 50 words, and each word can have up to 15 characters.
    - Each message has to be processed independently.
    """

```

## Cleaned Prompt

```python
def hidden_treasure_messages(messages):
    Process each message by decoding the words positioned at prime indices when called in reverse and each word occurs prime number of times across the messages.

```

## Canonical Solution

```python
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def process_message(message):
        words = message.split()
        unique_words = list(set(words))  # Remove duplicates (distinct words)
        reverse_sorted_words = [word[::-1] for word in sorted(unique_words, key=lambda word: len([c for c in word if c in 'aeiou']))]
        prime_index_words = [word for idx, word in enumerate(reverse_sorted_words) if is_prime(idx) and word.isalpha()]
        return ' '.join(prime_index_words)

    return [process_message(message) for message in messages]
```

## Test Cases

```python
def check(candidate):
    assert candidate(['monastery golden coin', 'golden hidden routes', 'hidden treasure found']) == ['nioc nedlog', 'setuor nedlog', 'dnuof erusaert']
    assert candidate(['routes monastery treasure', 'coin treasure routes golden hidden']) == ['erusaert', 'dnuof']
    assert candidate(['routes treasure golden']) == ['nedlog']
    assert candidate(['hidden', 'hidden hidden', 'monastery']) == ['', '', '']
    assert candidate([]) == []
```

## Entry Point

`hidden_treasure_messages`

## Warnings

- Solution failed correctness check.
- 5, Incorrect Processing Details: The problem description suggests using wavelet trees and a modified bucket sort to handle the encoding of the messages. However, the canonical solution provided does not implement these methods. Instead, it uses basic set operations and list comprehensions for managing duplicates and sorting. This discrepancy between the stated problem requirements and the implemented solution in the canonical solution indicates a significant flaw, as it might lead to confusion about the expected techniques and their implementation.
- 4, Ambiguity in Problem Requirements: The prompt is ambiguous about how the messages should be sorted and further processed. It mentions sorting messages using a modified bucket sort and a prime determination via wavelet trees, which are complex data structures. Nevertheless, it fails to provide detailed methodology or clear requirements on how these data structures should be applied to sorting or the specific modifications required for bucket sort, potentially leading participants to make incorrect assumptions or face difficulties in implementing the desired solution.

