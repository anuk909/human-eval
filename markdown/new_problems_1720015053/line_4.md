# Task ID: hard/3

## Topics

['String', 'Probability and Statistics']

## Cover Story

['dragons', 'friendly ghosts']

## Prompt

```python
def ghost_dragons_messages(messages):
    """
    You are in a magical land where dragons and friendly ghosts communicate using special encoded messages. Each message is a string composed of letters and digits. Dragons and ghosts only care about prime frequency characters.

    You are given a list of strings 'messages'. Each string represents one message. Your task is to calculate and return the probability that a randomly selected character from a randomly selected message from the list is a prime frequency character.

    A prime frequency character is one whose frequency in its message is a prime number.

    Example:
    If messages = ['aabb', 'aabc', 'ccccc'], prime frequency characters from:
    - 'aabb' are ['a', 'b'] (each appears 2 times which is prime),
    - 'aabc' has ['c'] (appears 1 time, not prime),
    - 'ccccc' has ['c'] (appears 5 times which is prime).
    Thus, the probability in this example would be 6 (prime frequency characters) / 12 (total characters) = 0.5.

    Note:
    - If the list is empty or there are no prime frequency characters in any message, the probability should be 0.0.
    - Each message in the list can be empty.
    """
```

## Cleaned Prompt

```python
def ghost_dragons_messages(messages):
    Calculate and return the probability that a randomly selected character from a randomly selected message from the list is a prime frequency character. Assume that each message is a string consisting of alphanumeric characters.
```

## Canonical Solution

```python
    from collections import Counter
    from math import isqrt

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    def ghost_dragons_messages(messages):
        total_chars = 0
        prime_freq_chars = 0

        for msg in messages:
            if msg:
                freq_counter = Counter(msg)
                for char, freq in freq_counter.items():
                    if is_prime(freq):
                        prime_freq_chars += freq
                total_chars += len(msg)

        return prime_freq_chars / total_chars if total_chars != 0 else 0.0
```

## Test Cases

```python
def check(candidate):
    assert candidate(['aabb', 'aabc', 'ccccc']) == 0.5
    assert candidate(['abcd']) == 0.0
    assert candidate(['aaa', 'bb', 'cc']) == 5/6
    assert candidate(['zzz', 'yyy', 'zzz']) == 12/12
    assert candidate([]) == 0.0
    assert candidate(['', 'aaaa', 'bbbbbbbb']) == 12/13
```

## Entry Point

`ghost_dragons_messages`

## Warnings

- Solution failed correctness check.
- 4, Ambiguity in Definition of Prime Frequency: The problem statement specifies 'prime frequency' characters with the example stating that characters appearing 2 times are considered as having a prime frequency, while 2 is the only even prime number. The example does not consider 1 as prime which is correct but fails to explicitly exclude 0 which makes interpreting inconsistent frequencies confusing, especially considering empty strings or characters that do not appear.

