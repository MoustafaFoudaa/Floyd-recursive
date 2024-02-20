import unittest
from Floyd_recursive_function import floyd_warshall_recursive, floyd_warshall_recursive_wrapper

class TestFloydWarshallRecursive(unittest.TestCase):
    def test_floyd_warshall_recursive_example(self):
        graph_example = [
            [0, 7, float('inf'), 8],
            [float('inf'), 0, 5, float('inf')],
            [float('inf'), float('inf'), 0, 2],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        result = floyd_warshall_recursive(graph_example, 3, 1, 2)
        expected_result = float('inf')  # Add your expected result based on the input
        self.assertEqual(result, expected_result)

    def test_floyd_warshall_recursive_wrapper(self):
        graph_example = [
            [0, 7, float('inf'), 8],
            [float('inf'), 0, 5, float('inf')],
            [float('inf'), float('inf'), 0, 2],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        result = floyd_warshall_recursive_wrapper(graph_example)
        # Add your assertions for the wrapper function here
        self.assertIsNotNone(result)
        # You can add more specific assertions based on the expected behavior

if __name__ == '__main__':
    unittest.main()
