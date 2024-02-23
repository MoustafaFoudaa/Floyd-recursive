"""
including unit tests and performance measurement for the Floyd.

Warshall recursive functions.
"""

import unittest
import time
from Floyd_recursive_function import floyd_warshall_recursive, floyd_warshall_recursive_wrapper


class TestFloydWarshallRecursive(unittest.TestCase):
    """Test case for Floyd-Warshall recursive functions."""

    def test_floyd_warshall_recursive_example(self):
        """Test the example case for the Floyd-Warshall recursive function."""
        graph_example = [
            [0, 7, float('inf'), 8],
            [float('inf'), 0, 5, float('inf')],
            [float('inf'), float('inf'), 0, 2],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        result = floyd_warshall_recursive(graph_example, 3, 1, 2)
        expected_result = 5  # Add your expected result based on the input
        self.assertEqual(result, expected_result)

    def test_floyd_warshall_recursive_wrapper(self):
        """
        Test the wrapper function for the Floyd-Warshall.

        recursive function.
        """
        graph_example = [
            [0, 7, float('inf'), 8],
            [float('inf'), 0, 5, float('inf')],
            [float('inf'), float('inf'), 0, 2],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        result = floyd_warshall_recursive_wrapper(graph_example)
        self.assertIsNotNone(result)



def measure_performance(graph_function, graph, num_iterations=10):
    """
    Measure the performance of a graph function over multiple iterations.

    Parameters
----------
        graph_function: The function to measure the performance of.
        graph: The input graph for the function.
        num_iterations: The number of iterations for performance measurement.

    Returns
-------
        Tuple containing the result of the function and the average
        execution time.
    """
    total_execution_time = 0
    for _ in range(num_iterations):
        start_time = time.perf_counter()
        result = graph_function(graph)
        end_time = time.perf_counter()
        total_execution_time += end_time - start_time
    average_execution_time = total_execution_time / num_iterations
    return result, f"{average_execution_time:.8f}"


if __name__ == '__main__':
    unittest.main()
