import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Определяем графы
G1 = nx.Graph()
G2 = nx.Graph()

def draw_graphs(matrix_str1, matrix_str2):
    matrix1 = np.array(eval(matrix_str1))
    matrix2 = np.array(eval(matrix_str2))
    # Добавляем вершины и ребра в каждый граф на основе матрицы смежности
    for i in range(len(matrix1)):
        G1.add_node(i+1)
        for j in range(i+1, len(matrix1)):
            if matrix1[i][j] == 1:
                G1.add_edge(i+1, j+1)

    for i in range(len(matrix2)):
        G2.add_node(i+1)
        for j in range(i+1, len(matrix2)):
            if matrix2[i][j] == 1:
                G2.add_edge(i+1, j+1)

    # Отображаем диаграммы данных графов
    pos = nx.spring_layout(G1)
    nx.draw_networkx(G1, pos)
    plt.title('Граф 1')
    plt.savefig('graphs_images/graph_source_1.png')
    plt.clf()  # Чистим фигуру

    pos = nx.spring_layout(G2)
    nx.draw_networkx(G2, pos)
    plt.title('Граф 2')
    plt.savefig('graphs_images/graph_source_2.png')
    plt.clf()  # Чистим фигуру

    print(matrix1)
    # Определяем число ребер в каждом графе
    num_edges_G1 = G1.number_of_edges()
    num_edges_G2 = G2.number_of_edges()

    # Определяем число изолированных подграфов в первом графе
    num_isolated_subgraphs = nx.number_connected_components(G1)

    # Определяем диаметр второго графа
    diameter_G2 = nx.diameter(G2)
  
    # Формируем список с результатами
    message = []
    message.append(f"Число ребер в графе G1: {num_edges_G1}")
    message.append(f"Число ребер в графе G2: {num_edges_G2}")
    message.append(f"Число изолированных подграфов в графе G1: {num_isolated_subgraphs}")
    message.append(f"Диаметр графа G2: {diameter_G2}")
    if nx.is_connected(G2):
        # Определяем диаметр второго графа
        diameter_G2 = nx.diameter(G2)
        print("Диаметр графа G2: ", diameter_G2)
    else:
        print("Второй граф не является связным.")
    return message
    # Проверяем, является ли второй граф связным
