import unittest

import networkx as nx
import numpy as np


class TestDrawGraphComplete(unittest.TestCase):
    def setUp(self):
        self.matrix_str_cases = ["[[1, 0], [0, 1]]", "[[1, 1], [1, 0]]", "[[1, 0, 1], [0, 1, 0], [1, 0, 1]]", "[[1, 1, 1], [1, 1, 1], [1, 1, 1]]", "[[1, 0, 0], [0, 1, 0], [0, 0, 1]]",
                            "[[1, 1, 1], [1, 0, 1], [1, 1, 1]]", "[[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]", "[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]"]
        self.missing_edges_cases = [[(1,2)], [], [(1, 2), (2, 3)], [], [(1, 2), (1, 3), (2, 3)], [], [(1, 2), (1, 3), (2, 4), (3, 4)], [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]]

    def test_draw_graph_complete(self):
        for index, matrix_str in enumerate(self.matrix_str_cases):
            expected_missing_edges = self.missing_edges_cases[index]
            G1 = nx.Graph()
            missing_edges = []
            matrix = np.array(eval(matrix_str))
            for i in range(len(matrix)):
                for j in range(i + 1, len(matrix)):
                    if matrix[i][j] == 0:
                        missing_edges.append((i + 1, j + 1))
            if missing_edges:
                G1.add_edges_from(missing_edges)
            self.assertEqual(missing_edges, expected_missing_edges)

