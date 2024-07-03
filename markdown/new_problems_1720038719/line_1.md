# Task ID: hard/2

## Topics

['Array', 'Brainteaser', 'Error Handling']

## Cover Story

['flying carpet', 'car']

## Prompt

```python
def determine_fuel_usage(car_path, carpet_path, fuel_rates):
    """
    Calculate the total fuel usage for a journey by a car and a magic carpet, each with their own specified route configurations.
    - The car's journey is described by a list of integers, `car_path`, where each integer represents the fuel consumed for that segment of the journey.
    - The magic carpet's path is described by a string, `carpet_path`, consisting of characters 'u' (up), 'd' (down), and 'f' (forward), with standard fuel consumptions of 1, 2, and 3 units respectively for these directions. You can override these rates with a `fuel_rates` dictionary specifying custom fuel consumption for these actions.
    - If `fuel_rates` is incomplete or missing values for 'u', 'd', or 'f', default values of 1, 2, and 3 respectively should be used.
    - The function should consider robust input handling. Specifically, `car_path` should contain only non-negative integers, and `carpet_path` should only consist of the characters 'u', 'd', 'f'. An exception should be raised for invalid inputs.

    Example usages:
    - For inputs ([3, 5, 1], 'ffudfd', {'u': 1, 'd': 2, 'f': 3}), the function should return (9, 13) signifying 9 units for the car and 13 units for the carpet.
    - If `car_path` or `carpet_path` are empty, or `fuel_rates` is empty, the function should still handle these cases, returning the calculated sum based on available data or default consumption rates.
    """
```

## Cleaned Prompt

```python
Define a function that calculates total fuel usage for a car and a magic carpet given their respective path segments. The car's path is represented by a list of integers indicating fuel consumed per segment. The magic carpet's path is a string with characters ('u', 'd', 'f') representing actions consuming fuel. Additionally, a dictionary can specify modified fuel rates impacting carpet fuel consumption. Compute the total fuel usage for both car and carpet, handling inputs robustly for error scenarios.
```

## Warnings

- Solution failed correctness check.
- 4, Functionality Limitation: The problem does not specify what should happen if the `fuel_rates` dictionary includes keys other than 'u', 'd', or 'f'. This might lead to unexpected behavior if extra keys are provided or if these keys map to invalid values (non-numeric or negative).

## Canonical Solution

```python
def determine_fuel_usage(car_path, carpet_path, fuel_rates=None):
        if fuel_rates is None:
            fuel_rates = {'u': 1, 'd': 2, 'f': 3}
        else:
            fuel_rates.setdefault('u', 1)
            fuel_rates.setdefault('d', 2)
            fuel_rates.setdefault('f', 3)
        if any(not isinstance(segment, int) or segment < 0 for segment in car_path):
            raise ValueError('Invalid car_path: all segments must be non-negative integers')
        if any(c not in 'udf' for c in carpet_path):
            raise ValueError('Invalid carpet_path: must only contain u, d, f')

        car_fuel_usage = sum(car_path)
        carpet_fuel_usage = sum(fuel_rates[char] for char in carpet_path)

        return (car_fuel_usage, carpet_fuel_usage)
```

## Test Cases

```python
def check(candidate):
    assert candidate([3, 5, 1], 'ffudfd', {'u': 1, 'd': 2, 'f': 3}) == (9, 13)
    assert candidate([], '', {}) == (0, 0)
    assert candidate([1, 2, 3, 4], 'ufdfud', {'u': 2, 'd': 3, 'f': 4}) == (10, 23)
    assert candidate([4], 'd', {'d': 2}) == (4, 2)
    assert candidate([1, 1, 1], 'uuu', {}) == (3, 3)
    assert candidate([2, 2], 'fff', {'f': 3.5}) == (4, 10.5)
```

## Entry Point

`determine_fuel_usage`

