import os
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def draw_graph_complete(matrix_str):
    # Определяем граф
    matrix = np.array(eval(matrix_str))
    G1 = nx.Graph()

    # Определяем индексы отсутствующих ребер
    missing_edges = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i][j] == 0:
                missing_edges.append((i + 1, j + 1))

    # Добавляем отсутствующие ребра в граф
    if missing_edges:
        G1.add_edges_from(missing_edges)

    # Создаем директорию для сохранения изображения
    os.makedirs('graphs_images', exist_ok=True)

    # Отображаем диаграмму данных графа
    pos = nx.spring_layout(G1)
    nx.draw_networkx(G1, pos, node_color='#D0DB97')
    plt.title('Дополнение')
    plt.savefig('graphs_images/graph_result_1.png')
    plt.clf() # Чистим фигуру
def create_intersection_graph(matrix_str1, matrix_str2): #todo: Посмотреть что тут
    # Create empty intersection graph
    matrix1 = np.array(eval(matrix_str1))
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

    pos = nx.spring_layout(intersection_graph)
    nx.draw_networkx(intersection_graph, pos,node_color='#D0DB97')
    plt.title('Пересечение')
    plt.savefig('graphs_images/graph_result_2.png')
    plt.clf()  # Чистим фигуру
import matplotlib.pyplot as plt
import networkx as nx

def create_union_graph(matrix_str1, matrix_str2):
    # Create empty union graph
    matrix1 = np.array(eval(matrix_str1))
    matrix2 = np.array(eval(matrix_str2))
    union_graph = nx.Graph()

    # Add nodes from matrix1
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

    pos = nx.spring_layout(union_graph)
    nx.draw_networkx(union_graph, pos,node_color='#D0DB97')
    plt.title('Объединение')
    plt.savefig('graphs_images/graph_result_3.png')
    plt.clf()  # Чистим фигуру


