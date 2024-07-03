# Task ID: hard/4

## Topics

['Concurrency', 'Red-Black Tree']

## Cover Story

['urban jungle', 'mythology']

## Prompt

```python
def mythical_creatures_tracker(observations, order_of_arrival):
    """
    In the bustling metropolis teeming with both skyscrapers and ancient mythical creatures, the city council needs a system to manage sightings of these elusive beings.

    Each 'observation' is a sequence of (time, creature, location) tuples, where:
    - 'time' is the integer timestamp of the observation,
    - 'creature' is a string representing the type of mythical creature observed,
    - 'location' is a tuple (x,y) representing two-dimensional city coordinates.

    Because multiple observations might be reported asynchronously, they can arrive out of order. 'order_of_arrival' is a list indicating the sequential order in which observations are reported.

    Your mission is to organize these observations using a concurrency-aware Red-Black Tree structure and provide two functionalities:
    - Image capturing: Capture the 'creature' from a given 'location' and update its 'time of last seen'. Use a simulated image processing within the data structure.
    - Tracking query: Return the most recent 'time' a certain 'creature' was seen maintaining date-time integrity.

    The Red-Black Tree should efficiently manage changes, preventing race conditions and deadlocks, while handling concurrent insertions, deletions, and queries with mutex locks or similar mechanisms.

    Examples:
    Input:
    [(20210510, 'Dragon', (10, 23)), (20210512, 'Phoenix', (35, 76)), (20210511, 'Griffin', (52, 41))], [2, 1, 3]
    Image capture: ('Phoenix', (35, 76)) at 20210515
    Tracking query: 'Dragon'

    Output:
    Most recent sighting of 'Dragon': 20210510
    """

```

## Cleaned Prompt

```python
Organize observations of mythical creatures using a Concurrency-aware Red-Black Tree. Observations are (time, creature, location) tuples arriving in non-chronological order. Implement functionalities to capture images of creatures updating their last seen time and to query the most recent time a creature was seen. Ensure efficient concurrent operations for these functionalities.
```

## Warnings

- Only 3 test cases found. Minimum recommended is 5.
- Solution failed correctness check.
- 5, Unrealistic Problem Complexity: The task requires the implementation of a concurrency-aware Red-Black Tree, which is an advanced data structure involving complex concepts like tree balancing, coloring, and concurrent data access management. This level of complexity exceeds typical expectations for coding competitions, potentially discouraging participation due to the steep learning curve and implementation difficulty.
- 5, Lack of Clear Requirements: The problem statement does not specify how to handle edge cases such as querying a creature that hasn't been observed, or image capturing with a non-matching location. These ambiguities can lead to inconsistent implementations and misunderstandings about expected functionalities.

## Canonical Solution

```python
from threading import Lock

class Node:
    def __init__(self, data=None, color='red'):
        self.data = data
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

    def rotate_left(self):
        # Rotate left logic
        pass

    def rotate_right(self):
        # Rotate right logic
        pass

class RedBlackTree:
    def __init__(self):
        self.root = None
        self.lock = Lock()

    def insert(self, data):
        with self.lock:
            # Handling concurrent insertions
            if self.root is None:
                self.root = Node(data, 'black')
            else:
                # Insertion logic with rebalancing
                pass

    def delete(self, data):
        with self.lock:
            # Handling concurrent deletions
            pass

    def query(self, creature):
        with self.lock:
            # Handling concurrent queries
            pass

    def image_capture(self, creature, location, time):
        # Image capture simulation and update node
        pass

def mythical_creatures_tracker(observations, order_of_arrival):
    # Main function writing data operations based on given 'observations' in the order of 'order_of_arrival'
    tree = RedBlackTree()
    for idx in sorted(order_of_arrival):
        observation = observations[idx - 1]
        tree.insert(observation)

    # Implement additional functionalities as required
    pass

```

## Test Cases

```python
def check(candidate):
    observations = [(20210510, 'Dragon', (10, 23)), (20210512, 'Phoenix', (35, 76)), (20210511, 'Griffin', (52, 41))]
    order_of_arrival = [2, 1, 3]

    # Initialize tracker
    tracker = candidate(observations, order_of_arrival)

    # Simulate system operations
    tracker.image_capture('Phoenix', (35, 76), 20210515)
    assert tracker.query('Dragon') == 20210510
    assert tracker.query('Phoenix') == 20210515  # Updated time after image capture operation

    # Further operations and assertions can be conducted 

```

## Entry Point

`mythical_creatures_tracker`

