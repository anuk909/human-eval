# Task ID: hard/3

## Topics

['Group Anagrams', "Manacher's Algorithm"]

## Cover Story

['treasure', 'steampunk']

## Prompt

```python
def steampunk_treasure_decoder(text):
    """
    In a steampunk world, treasure maps are cleverly encoded in long texts. The key to finding the treasure is hidden within anagrams located in palindromic substrings of the text. Your task is to decode these texts using the following steps:

    1. Identify all possible contiguous substrings that are palindromes using Manacher's Algorithm.
    2. For each identified palindrome, extract words (sequences of alphabetic characters, ignoring spaces and punctuation) and group the words into anagrams.
    3. Return a dictionary where the keys are the palindromic substrings, and the values are lists where each list contains groups of words that are anagrams of each other represented as sets.

    A correctly formatted output for the input 'A man, a plan, a canal, Panama!' could be:
    {
        'A man, a plan, a canal, Panama': [{'a', 'a'}, {'man', 'nam'}, {'plan', 'lanap'}],
        'anana': [{'ana', 'naa'}]
    }

    Notes:
    - Ignore case differences when checking for palindromes and anagrams. Consider 'A' the same as 'a'.
    - This task combines the use of Manacher's Algorithm for palindrome detection, which is efficient even for large texts, with an anagram grouping mechanism.
    """
```

## Cleaned Prompt

```python
def steampunk_treasure_decoder(text):
    """
    Given a text, identify all palindromic substrings using Manacher's Algorithm, and for each palindrome, group its words into anagrams. Return a dictionary where keys are palindrome substrings and values are lists of anagram groups (as sets), while ignoring case and non-alphabetic characters in words.
    """
```

## Warnings

- Only 4 test cases found. Minimum recommended is 5.
- Solution failed correctness check.
- 5, Output Specification Mismatch: The problem prompt incorrectly specifies the dictionary output. The keys in the example result are incorrect based on the description. The example shows keys like 'A man, a plan, a canal, Panama' which include punctuation and spaces, whereas the description states that words in palindromes should ignore spaces and punctuation. This inconsistency could lead to confusion about what exactly should be used as keys in the output dictionary.
- 4, Complex Algorithm Combination Without Adequate Details: The task combines the use of Manacher's Algorithm with an anagram grouping mechanism, which individually are complex. There is a lack of sufficient detail on implementing Manacher’s Algorithm specifically, as just a placeholder without any implementation or resources is provided. This could potentially make the problem too challenging or ambiguous for participants who are unfamiliar with advanced algorithms.

## Canonical Solution

```python
    def steampunk_treasure_decoder(text):
        import re

        def find_palindromes(text):
            # Here insert a concrete implementation of Manacher's Algorithm to find all palindromic substrings
            pass

        def group_anagrams(words):
            d = {}
            for word in words:
                sorted_word = ''.join(sorted(word.lower()))
                if sorted_word in d:
                    d[sorted_word].add(word.lower())
                else:
                    d[sorted_word] = {word.lower()}
            return list(d.values())

        palindromes = find_palindromes(text)
        result = {}
        for p in palindromes:
            words = re.findall(r'\b[a-zA-Z]+\b', p)
            anagrams = group_anagrams(words)
            result[p] = anagrams

        return result
```

## Test Cases

```python
def check(candidate):
    result = candidate('A man, a plan, a canal, Panama!')
    assert len(result) == 2, 'The function should detect two palindromic substrings'
    assert 'A man, a plan, a canal, Panama' in result, 'Longest palindrome should be identified correctly'
    assert [{'a', 'a'}, {'man', 'nam'}, {'plan', 'lanap'}] == result['A man, a plan, a canal, Panama'], 'Anagram groups within the palindrome are not identified correctly'
    assert [{'ana', 'naa'}] == result['anana'], 'Anagram groups for shorter palindrome are incorrect'
```

## Entry Point

`steampunk_treasure_decoder`

