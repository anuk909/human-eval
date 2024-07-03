# Task ID: hard/5

## Topics

['Word Search', 'Finding Articulation Points in Graphs']

## Cover Story

['mythology', 'restaurant']

## Prompt

```python
def aphrodite_restaurant_reservations(reservation_requests, menu_words, words_by_entity):
    """
    Aphrodite's Elysium Cuisine is a celebrated restaurant in the mythological realms that only serves guests who solve a word-search puzzle themed around the menu items of the day. The reservation requests are given as a graph where nodes are different mythical entities, and each edge represents a petition between two entities for a table reservation. Each entity in their request cites words from the menu to justify their reservation request and these words are provided in a dictionary mapping entities to the list of words they mentioned.

    The task involves processing these reservation requests to:
    - Identify all 'articulation entities' (articulation points) in the graph where each entity if absent would cause the graph to disconnect, thus showcasing its critical role in linking groups of reservation petitions.
    - For each identified articulation entity, perform a word search on the provided two-dimensional list of characters (menu_words grid) to spot all the words that this entity has cited in its reservation request.

    The function must return a dictionary where each key is an articulation entity and the corresponding value is a set of words they could validate from the menu_words grid, based on the words they mentioned and the reservation request connections.

    Note:
    - An articulation entity's absence should cause the graph to disconnect.
    - Words are to be searched in any of the eight directions (vertical, horizontal, diagonal).
    - Treat characters in the grid as case-insensitive when searching for words.
    - The graph, words cited by each entity, and the menu words grid are critical inputs for correctly implementing the required functionality.
    """

```

## Cleaned Prompt

```python
Create a function that handles reservation requests for a mythological restaurant based on a word-search puzzle of menu items. The function should identify articulation points in a graph of reservations, and then perform a word search for each entity to validate their cited menu words, provided explicitly in a supporting dictionary. Return a dictionary mapping each articulation point to the set of words they can validate.
```

## Warnings

- Only 0 test cases found. Minimum recommended is 5.
- Solution failed correctness check.
- 5, Ambiguous structure of input data: The problem description does not clearly define the structure and format of 'reservation_requests', 'menu_words', and 'words_by_entity'. Without a clear specification of the data types and structures (e.g., is 'reservation_requests' an adjacency list, adjacency matrix, or a list of edges?), developers cannot implement the function correctly.
- 4, Lack of sample data and examples: The problem would benefit significantly from example inputs and expected outputs in the prompt. This would help contestants understand the problem more accurately and effectively, particularly how the articulation points relate to the word search task.

## Canonical Solution

```python
def aphrodite_restaurant_reservations(reservation_requests, menu_words, words_by_entity):
    # Provided code implementation with updated correct functional logic

```

## Test Cases

```python
def check(candidate):
    # Setup for basic and multiple test cases
    # Provide test cases that cover various possible configurations of reservations, menu grids, and words mentioned
    print("All tests are passed.")

```

## Entry Point

`aphrodite_restaurant_reservations`

