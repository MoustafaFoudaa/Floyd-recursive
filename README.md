# Floyd recursive
# Floyd-Warshall Algorithm

This project implements the Floyd-Warshall algorithm for finding the shortest paths in a weighted graph. 
The implementation includes a recursive version of the algorithm and a wrapper function for ease of use.

## Table of Contents

- [Implementation](#implementation)
- [Usage](#usage)
- [License](#license)

## Implementation

### Recursive Implementation

The core of the implementation is the `floyd_warshall_recursive` function. 
It calculates the shortest path distance from a source vertex to a destination vertex considering intermediate vertices.
The `floyd_warshall_recursive_wrapper` function provides a convenient interface for using the algorithm on a graph.

## Usage

To use the Floyd-Warshall algorithm on your graph, follow these steps:

1. Ensure Python is installed.
2. Copy the Floyd-Warshall code into your project.
3. Create a graph represented as an adjacency matrix.
4. Call the `floyd_warshall_recursive_wrapper` function with your graph as input.

Example:

```python
graph_example = [
    [0, 7, float('inf'), 8],
    [float('inf'), 0, 5, float('inf')],
    [float('inf'), float('inf'), 0, 2],
    [float('inf'), float('inf'), float('inf'), 0]
]

result = floyd_warshall_recursive_wrapper(graph_example)
print("Result Matrix:")
print(result)

## License 
Feel free to customize this template based on your project's specific needs. 
You may want to add sections for unit testing, performance testing, or any additional information that is relevant to your project.
