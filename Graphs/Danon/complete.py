import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def draw_graph(matrix_str):
    # Определяем граф
    matrix = np.array(eval(matrix_str))
    G1 = nx.Graph()

    # Определяем индексы отсутствующего ребра
    missing_edge = None
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i][j] == 0:
                missing_edge = (i + 1, j + 1)
                break
        if missing_edge is not None:
            break

    # Добавляем отсутствующее ребро в граф
    if missing_edge is not None:
        G1.add_edge(*missing_edge)

    # Отображаем диаграмму данных графа
    nx.draw(G1, with_labels=True)

    # Сохраняем диаграмму в файл формата PNG
    plt.savefig('graph.png')
    plt.clf()  # Чистим фигуру

# Пример использования функции

