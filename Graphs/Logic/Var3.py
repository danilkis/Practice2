import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Расчет степеней вершин
def calculate_vertex_degrees(adj_matrix):
    degrees = []
    for row in adj_matrix:
        degree = sum(row)  # Суммируем значения в строке матрицы
        degrees.append(degree)
    return degrees

# Поиск всех правильных графов из N вершин
def generate_graphs(n):
    graphs = []

    # Создаем список вершин
    vertices = list(range(n))

    # Генерируем все возможные графы
    for i in range(n):
        graph = [[0] * n for _ in range(n)]

        # Добавляем ребра между вершинами
        for j in range(n // 2):
            neighbor = (i + j + 1) % n
            graph[i][neighbor] = 1
            graph[neighbor][i] = 1



        graphs.append(graph)

    return graphs

def draw_graph(graph, filename):
    G = nx.Graph()

    # Добавляем вершины в граф
    G.add_nodes_from(range(len(graph)))

    # Добавляем ребра в граф
    for i in range(len(graph)):
        for neighbor in graph[i]:
            G.add_edge(i, neighbor)

    # Рисуем граф
    pos = nx.spring_layout(G)  # Определяем позиции вершин
    nx.draw_networkx(G, pos, node_color='#D0DB97')

    # Добавляем метки степеней вершин
    degrees = [len(graph[i]) for i in range(len(graph))]
    for i in range(len(graph)):
        x, y = pos[i][0], pos[i][1] + 0.05
        plt.text(x, y, f'deg: {degrees[i]}', ha='center', va='center')

    plt.title('Граф')
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.1)
    plt.clf()


def Fill(matrix_str1, matrix_str2):
    adj_matrix1 = np.array(eval(matrix_str1))
    adj_matrix2 = np.array(eval(matrix_str2))

    degrees1 = calculate_vertex_degrees(adj_matrix1)
    degrees2 = calculate_vertex_degrees(adj_matrix2)

    message = [
        f"Степень вершин в графе G1: {degrees1}",
        f"Степень вершин в графе G2: {degrees2}",
    ]

    n = adj_matrix1.shape[1]
    # Пример использования
    graphs = generate_graphs(n)
    filenames = [
        'graphs_images/graph_result_1.png',
        'graphs_images/graph_result_2.png',
        'graphs_images/graph_result_3.png'
    ]

    last_graphs = graphs[-3:]

    # Записываем графы в указанные файлы
    for i in range(len(graphs)):
        filename = filenames[i % len(filenames)]  # Используем оператор модуля для выбора индекса файла
        draw_graph(graphs[i], filename)
    # Выводим все матрицы смежности
    for i, graph in enumerate(graphs):
        message.append(f"Правильный граф из {i + 1} вершин")
        matrix_str = np.array2string(np.array(graph), separator="\n")
        message.append(matrix_str)

    return message
