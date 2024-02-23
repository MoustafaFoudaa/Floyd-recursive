import timeit
import itertools

MAX_LENGTH = 3  # Adjust the size of the matrix for demonstration purposes

def floyd_iterative(distance):
    """
    Iterative implementation of Floyd's algorithm
    """
    for intermediate in range(MAX_LENGTH):
        for start_node in range(MAX_LENGTH):
            for end_node in range(MAX_LENGTH):
                if start_node == end_node:
                    distance[start_node][end_node] = 0
                    continue
                distance[start_node][end_node] = min(
                    distance[start_node][end_node],
                    distance[start_node][intermediate] + distance[intermediate][end_node]
                )

def floyd_recursive(distance, k, i, j):
    """
    Recursive implementation of Floyd's algorithm
    """
    if k == 0:
        return distance[i][j]
    include_k = floyd_recursive(distance, k - 1, i, k) + floyd_recursive(distance, k - 1, k, j)
    exclude_k = floyd_recursive(distance, k - 1, i, j)
    return min(include_k, exclude_k)

def time_test_iterative():
    # Initialize the distance matrix (assuming some specific graph)
    graph = [[1] * MAX_LENGTH for _ in range(MAX_LENGTH)]

    # Use timeit to measure the execution time of the iterative approach
    elapsed_time = timeit.timeit(lambda: floyd_iterative(graph), number=10)
    print(f"Iterative Approach - Elapsed Time: {elapsed_time:.8f} seconds")

def time_test_recursive():
    # Initialize the distance matrix (assuming some specific graph)
    graph = [[1] * MAX_LENGTH for _ in range(MAX_LENGTH)]

    # Use timeit to measure the execution time of the recursive approach
    elapsed_time = timeit.timeit(lambda: floyd_recursive(graph, MAX_LENGTH - 1, 0, 1), number=10)
    print(f"Recursive Approach - Elapsed Time: {elapsed_time:.8f} seconds")

if __name__ == "__main__":
    # Run the time tests for both approaches
    time_test_iterative()
    time_test_recursive()
