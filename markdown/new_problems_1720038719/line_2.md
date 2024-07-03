# Task ID: hard/4

## Topics

['Group Anagrams', 'Brainteaser']

## Cover Story

['city', 'gemstone mine']

## Prompt

```python
def evaluate_gem_distribution(city_names, mine_outputs):
    """
    This function evaluates the gemstone outputs of various cities and identifies potential trade partners based on these outputs. Each city has a gemstone mine, and daily outputs are encoded as strings where each character represents a type of gemstone.

    Given two lists, `city_names` and `mine_outputs`, where `city_names` contains unique city names and `mine_outputs` is a list of strings representing the gem outputs for these cities, the function returns a dictionary. This dictionary maps each city to a list of other cities whose gem outputs are anagrams of the first city's output.

    Requirements:
    - Both `city_names` and `mine_outputs` must have the same length and contain only valid strings.
    - City names must be unique and consist only of letters.
    - Outputs will be lowercase English letters only.
    - If a city has no potential trade partners, its value in the returned dictionary should be an empty list.
    - The function should handle cases with just a single city correctly by returning an empty list for that city.
    - The function should validate inputs; invalid or malformed input should raise a ValueError.

    Example:
        city_names = ['Delta', 'Echo', 'Golf']
        mine_outputs = ['abcd', 'dcba', 'abdc']
        expected output: {'Delta': ['Echo', 'Golf'], 'Echo': ['Delta', 'Golf'], 'Golf': ['Delta', 'Echo']}
    """
```

## Cleaned Prompt

```python
Write a function to evaluate mine outputs of different cities and find potential trade partners. Each city's mine output is represented as a string of gemstone codes (lowercase letters). Cities are potential trade partners if their mine outputs are anagrams of each other. Return a dictionary mapping each city to its list of potential trade partner cities.
```

## Warnings

- Solution failed correctness check.
- 5, Ambiguous problem definition: The problem statement ambiguously defines the handling of potential edge cases, such as what should be returned if there are duplicate entries within city_names or if mine_outputs contains invalid character entries. The expected behavior in these scenarios isn't described.
- 4, Assumed input validation: The prompt adopts that the solution must validate the input, yet it does not clearly define all criteria. For example, it doesn't mention if numeric strings as city names are valid or not, creating potential confusion in requirement scope.

## Canonical Solution

```python
    def evaluate_gem_distribution(city_names, mine_outputs):
        if len(city_names) != len(mine_outputs):
            raise ValueError('Mismatched input lengths.')
        if any(not isinstance(city, str) or not city.isalpha() for city in city_names):
            raise ValueError('Invalid city names.')
        if any(not isinstance(output, str) or not output.islower() for output in mine_outputs):
            raise ValueError('Invalid mine outputs.')

        from collections import defaultdict
        # Maps each city to its sorted tuple of mine output
        city_to_sorted_gems = {city: tuple(sorted(output)) for city, output in zip(city_names, mine_outputs)}
        # Reverse map from sorted tuple of gems to list of cities
        sorted_gems_to_cities = defaultdict(list)
        for city, sorted_gems in city_to_sorted_gems.items():
            sorted_gems_to_cities[sorted_gems].append(city)
        # Result dictionary
        result = defaultdict(list)
        for city, sorted_gems in city_to_sorted_gems.items():
            for partner_city in sorted_gems_to_cities[sorted_gems]:
                if partner_city != city:
                    result[city].append(partner_city)
        return dict(result)
```

## Test Cases

```python
def check(candidate):
    # Add more test cases including those focusing on input validation and unique situations such as single city scenarios.
    assert candidate(['Delta', 'Echo', 'Golf'], ['abcd', 'dcba', 'abdc']) == {'Delta': ['Echo', 'Golf'], 'Echo': ['Delta', 'Golf'], 'Golf': ['Delta', 'Echo']}
    assert candidate(['A'], ['a']) == {'A': []}  # Testing single city scenario
    # Testing invalid inputs
    try:
        candidate(['Delta', 123], ['abcd', 'dcba'])
        assert False, 'Expected ValueError due to non-string city name'
    except ValueError:
        assert True
    try:
        candidate(['Alpha', 'Beta'], ['abcd', 'abC'])  # mixed case should raise ValueError
        assert False, 'Expected ValueError due to non-lowercase letter'
    except ValueError:
        assert True
```

## Entry Point

`evaluate_gem_distribution`

