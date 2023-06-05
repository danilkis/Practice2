import unittest
import networkx as nx
import numpy as np

class GraphTest(unittest.TestCase):
    def test_num_edges(self):
        def get_num_edges(matrix_str):
            G = nx.Graph()
            matrix = np.array(eval(matrix_str))

            for i in range(len(matrix)):
                G.add_node(i + 1)
                for j in range(i + 1, len(matrix)):
                    if matrix[i][j] == 1:
                        G.add_edge(i + 1, j + 1)

            return G.number_of_edges()

        test_cases = [
            {
                "matrix_str": "[[0, 0, 0], [0, 0, 0], [0, 0, 0]]",
                "expected_count": 0
            },
            {
                "matrix_str": "[[1, 0, 0], [0, 1, 0], [0, 0, 1]]",
                "expected_count": 0
            },
            {
                "matrix_str": "[[1, 1, 0], [1, 0, 0], [0, 0, 1]]",
                "expected_count": 1
            },
            {
                "matrix_str": "[[1, 1, 1], [1, 1, 0], [1, 0, 1]]",
                "expected_count": 2
            },
            {
                "matrix_str": "[[1, 0, 1], [0, 1, 0], [1, 0, 1]]",
                "expected_count": 1
            },
            {
                "matrix_str": "[[0, 1, 0], [1, 0, 1], [0, 1, 0]]",
                "expected_count": 2
            },
            {
                "matrix_str": "[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]",
                "expected_count": 0
            },
            {
                "matrix_str": "[[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]",
                "expected_count": 3
            },
            {
                "matrix_str": "[[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]",
                "expected_count": 2
            }
        ]

        for test_case in test_cases:
            matrix_str = test_case["matrix_str"]
            expected_count = test_case["expected_count"]

            actual_count = get_num_edges(matrix_str)

            self.assertEqual(actual_count, expected_count, "Неверное количество ребер в графе")

if __name__ == '__main__':
    unittest.main()