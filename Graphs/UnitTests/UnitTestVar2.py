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

class TestDrawGraphComplete_false(unittest.TestCase):
    def setUp(self):
        self.matrix_str_cases = ["[[1, 0], [0, 1]]", "[[1, 1], [1, 0]]", "[[1, 0, 1], [0, 1, 0], [1, 0, 1]]", "[[1, 1, 1], [1, 1, 1], [1, 1, 1]]", "[[1, 0, 0], [0, 1, 0], [0, 0, 1]]",
                            "[[1, 1, 1], [1, 0, 1], [1, 1, 1]]", "[[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]", "[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]"]
        self.missing_edges_cases = [[(1,4)], [1,5], [(2, 5), (1, 5)], [(1,4)], [(2, 2), (1, 5), (6, 3)], [(1,3)], [(1, 5), (1, 2), (2, 4), (3, 5)], [(1, 4), (1, 6), (2, 4), (2, 6), (2, 4), (3, 4)]]

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
            self.assertFalse(missing_edges == expected_missing_edges)

class TestIntersectionGraph(unittest.TestCase):
    def setUp(self):
        self.matrix1_str_cases = ["[[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]]","[[0,1,0,1,0,0],[1,0,1,0,1,1],[0,1,0,1,0,0],[1,0,1,0,0,1],[0,1,0,0,0,0],[0,1,0,1,0,0]]",
                                  "[[0,1,0,1,0,0,1,0,1],[1,0,1,0,1,1,0,1,0],[0,1,0,1,0,0,1,0,1],[1,0,1,0,0,1,0,1,1],[0,1,0,0,0,0,1,1,0],[0,1,0,1,0,0,0,0,0],[1,0,1,0,1,0,0,1,1],[0,1,0,1,1,0,1,0,1],[1,0,1,1,0,0,1,1,0]]",]
        "[[0,1,0],[1,0,1],[0,1,0]]", "[[0,1,0,1,0,1],[1,0,1,0,1,0],[0,1,0,1,0,1],[1,0,1,0,1,0],[0,1,0,1,0,1],[1,0,1,0,1,0]]"
        self.matrix2_str_cases = ["[[0,1,0,1],[1,0,1,0],[0,1,0,0],[1,0,0,0]]","[[0,1,0,1,0,1],[1,0,1,0,1,0],[0,1,0,0,0,1],[1,0,0,0,1,0],[0,1,0,1,0,1],[1,0,1,0,1,0]]",
                                  "[[0,1,0,1,0,1,1,1,1],[1,0,1,0,1,0,0,1,1],[0,1,0,0,0,1,1,0,0],[1,0,0,0,1,0,1,0,1],[0,1,0,1,0,1,0,1,0],[1,0,1,0,1,0,1,0,0],[1,0,1,1,0,1,0,1,1],[1,1,0,0,1,0,1,0,1],[1,1,0,1,0,0,1,1,0]]",
                                 "[[0,1,0],[1,0,1],[0,1,0]]", "[[0,1,1,1,1,1],[1,0,0,0,0,1],[1,0,0,1,0,0],[1,0,1,0,1,0],[1,0,0,1,0,1],[1,1,0,0,1,0]]"]
        self.intersection_graph_cases = [[(1, 2), (1, 4), (2, 3)], [(1, 2), (1, 4), (2, 3), (2, 5)],[(1, 2), (1, 4), (1, 7), (1, 9), (2, 3), (2, 5), (2, 8), (3, 7), (4, 9), (5, 8), (7, 8), (7, 9), (8, 9)],
                                         [(1, 2), (2, 3)], [(1, 2), (1, 4), (1, 6), (3, 4), (4, 5), (5, 6)]]
    def test_intersection_graph(self):
        for index, matrix_str in enumerate(self.matrix1_str_cases):
            expected_intersection_graph = self.intersection_graph_cases[index]
            matrix_str2 = self.matrix2_str_cases[index]
            matrix1 = np.array(eval(matrix_str))
            matrix2 = np.array(eval(matrix_str2))
            intersection_graph = nx.Graph()

                # Add nodes from matrix1 that also exist in matrix2
            for i in range(len(matrix1)):
                if i + 1 not in intersection_graph.nodes():
                    intersection_graph.add_node(i + 1)

                # Add edges that exist in both matrix1 and matrix2
            for i in range(len(matrix1)):
                for j in range(i + 1, len(matrix1)):
                    if matrix1[i][j] == 1 and matrix2[i][j] == 1:
                        intersection_graph.add_edge(i + 1, j + 1)
            self.assertEqual(list(intersection_graph.edges), expected_intersection_graph)

class TestIntersectionGraph_false(unittest.TestCase):
    def setUp(self):
        self.matrix1_str_cases = ["[[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]]",
                                  "[[0,1,0,1,0,0],[1,0,1,0,1,1],[0,1,0,1,0,0],[1,0,1,0,0,1],[0,1,0,0,0,0],[0,1,0,1,0,0]]",
                                  "[[0,1,0,1,0,0,1,0,1],[1,0,1,0,1,1,0,1,0],[0,1,0,1,0,0,1,0,1],[1,0,1,0,0,1,0,1,1],[0,1,0,0,0,0,1,1,0],[0,1,0,1,0,0,0,0,0],[1,0,1,0,1,0,0,1,1],[0,1,0,1,1,0,1,0,1],[1,0,1,1,0,0,1,1,0]]",
                                  "[[0,1,0],[1,0,1],[0,1,0]]",
                                  "[[0,1,0,1,0,1],[1,0,1,0,1,0],[0,1,0,1,0,1],[1,0,1,0,1,0],[0,1,0,1,0,1],[1,0,1,0,1,0]]"]
        self.matrix2_str_cases = ["[[0,1,0,1],[1,0,1,0],[0,1,0,0],[1,0,0,0]]",
                                  "[[0,1,0,1,0,1],[1,0,1,0,1,0],[0,1,0,0,0,1],[1,0,0,0,1,0],[0,1,0,1,0,1],[1,0,1,0,1,0]]",
                                  "[[0,1,0,1,0,1,1,1,1],[1,0,1,0,1,0,0,1,1],[0,1,0,0,0,1,1,0,0],[1,0,0,0,1,0,1,0,1],[0,1,0,1,0,1,0,1,0],[1,0,1,0,1,0,1,0,0],[1,0,1,1,0,1,0,1,1],[1,1,0,0,1,0,1,0,1],[1,1,0,1,0,0,1,1,0]]",
                                  "[[0,1,0],[1,0,1],[0,1,0]]",
                                  "[[0,1,1,1,1,1],[1,0,0,0,0,1],[1,0,0,1,0,0],[1,0,1,0,1,0],[1,0,0,1,0,1],[1,1,0,0,1,0]]"]
        self.intersection_graph_cases = [[(1, 4), (1, 3), (1, 4)],
                                         [(1, 4), (1, 2), (22, 3), (2, 5)],
                                         [(1, 2), (4, 4), (11,7), (1, 9), (4, 3), (2, 5), (2, 1), (3, 7), (4, 9), (5, 8), (7, 8), (7, 9), (8, 9)],
                                         [(1, 4), (4, 3)],
                                         [(1, 5), (1, 3), (1, 6), (3, 4), (4, 5), (5, 6)]]

    def test_intersection_graph(self):
        for index, matrix_str in enumerate(self.matrix1_str_cases):
            expected_intersection_graph = self.intersection_graph_cases[index]
            matrix_str2 = self.matrix2_str_cases[index]
            matrix1 = np.array(eval(matrix_str))
            matrix2 = np.array(eval(matrix_str2))
            intersection_graph = nx.Graph()
            # Add nodes from matrix1 that also exist in matrix2
            for i in range(len(matrix1)):
                if i + 1 not in intersection_graph.nodes():
                    intersection_graph.add_node(i + 1)
            # Add edges that exist in both matrix1 and matrix2
            for i in range(len(matrix1)):
                for j in range(i + 1, len(matrix1)):
                    if matrix1[i][j] == 1 and matrix2[i][j] == 1:
                        intersection_graph.add_edge(i + 1, j + 1)
            self.assertFalse(list(intersection_graph.edges) == expected_intersection_graph, "Test failed for index " + str(index))

class TestUnionGraph(unittest.TestCase):
    def setUp(self):
        self.matrix1_str_cases = ["[[0,1,0,1,1],[1,0,1,0,0],[0,1,0,1,1],[1,0,1,0,1],[1,0,1,1,0]]", "[[0,1,1,1,0,1],[1,0,0,0,1,0],[1,0,0,1,0,1],[1,0,1,0,1,0],[0,1,0,1,0,1],[1,0,1,0,1,0]]", "[[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]]",
                                  "[[0,1,0],[1,0,1],[0,1,0]]", "[[0,1,0,1,1,0,1,0],[1,0,1,0,0,0,0,0],[0,1,0,1,1,1,1,1],[1,0,1,0,1,0,0,0],[1,0,1,1,0,0,1,0],[0,0,1,0,0,0,0,0],[1,0,1,0,1,0,0,1],[0,0,1,0,0,0,1,0]]"]
        self.matrix2_str_cases = ["[[0,1,0,1,0],[1,0,1,0,0],[0,1,0,1,1],[1,0,1,0,0],[0,0,1,0,0]]", "[[0,1,1,0,1,0],[1,0,0,0,0,1],[1,0,0,1,1,0],[0,0,1,0,1,0],[1,0,1,1,0,1],[0,1,0,0,1,0]]", "[[0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0]]",
                                  "[[0,1,0],[1,0,1],[0,1,0]]", "[[0,1,0,1,0,0,1,0],[1,0,1,0,0,1,0,1],[0,1,0,1,1,1,0,1],[1,0,1,0,0,0,1,0],[0,0,1,0,0,0,0,0],[0,1,1,0,0,0,1,0],[1,0,0,1,0,1,0,1],[0,1,1,0,0,0,1,0]]"]
        self.expected_union = [[(1, 2), (1, 4), (1, 5), (2, 3), (3, 4), (3, 5), (4, 5)], [(1, 2), (1, 3), (1, 4), (1, 6), (1, 5), (2, 5), (2, 6), (3, 4), (3, 6), (3, 5), (4, 5), (5, 6)], [(1, 2), (1, 4), (1, 3), (2, 3), (3, 4)],
                               [(1, 2), (2, 3)], [(1, 2), (1, 4), (1, 5), (1, 7), (2, 3), (2, 6), (2, 8), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (4, 5), (4, 7), (5, 7), (6, 7), (7, 8)]]
    def test_union_graph(self):
        for index, matrix_str in enumerate(self.matrix1_str_cases):
            expected_intersection_graph = self.expected_union[index]
            matrix_str2 = self.matrix2_str_cases[index]
            matrix1 = np.array(eval(matrix_str))
            matrix2 = np.array(eval(matrix_str2))
            # Add nodes from matrix1 that also exist in matrix2
            union_graph = nx.Graph()
            for i in range(len(matrix1)):
                union_graph.add_node(i + 1)
            # Add edges from matrix1
            for i in range(len(matrix1)):
                for j in range(i + 1, len(matrix1)):
                    if matrix1[i][j] == 1:
                        union_graph.add_edge(i + 1, j + 1)
            # Add nodes from matrix2
            for i in range(len(matrix2)):
                if i + 1 not in union_graph.nodes():
                    union_graph.add_node(i + 1)
            # Add edges from matrix2
            for i in range(len(matrix2)):
                for j in range(i + 1, len(matrix2)):
                    if matrix2[i][j] == 1:
                        union_graph.add_edge(i + 1, j + 1)

            self.assertEqual(list(union_graph.edges), self.expected_union[index])
