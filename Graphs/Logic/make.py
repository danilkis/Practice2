import networkx as nx
import numpy as np
import datetime
from matplotlib import pyplot as plt




def draw_graphs(matrix_str1, matrix_str2):
    G1 = nx.Graph() #Создает два графа G1 и G2 с использованием библиотеки NetworkX.
    G2 = nx.Graph()
    matrix1 = np.array(eval(matrix_str1)) #Преобразует строковые представления матриц смежности matrix_str1 и matrix_str2 в массивы NumPy с помощью eval.
    matrix2 = np.array(eval(matrix_str2))

    G1.clear() #Очищает графы G1 и G2.
    G2.clear()

    # Добавляет узлы и ребра в каждый граф на основе матрицы смежности.
    for i in range(len(matrix1)):
        G1.add_node(i + 1)
        for j in range(i + 1, len(matrix1)):
            if matrix1[i][j] == 1:
                G1.add_edge(i + 1, j + 1)

    for i in range(len(matrix2)):
        G2.add_node(i + 1)
        for j in range(i + 1, len(matrix2)):
            if matrix2[i][j] == 1:
                G2.add_edge(i + 1, j + 1)

    # num_edges_G1 и num_edges_G2 - количество ребер в графах G1 и G2 соответственно.
    num_edges_G1 = G1.number_of_edges()
    num_edges_G2 = G2.number_of_edges()
    num_isolated_subgraphs = nx.number_connected_components(G1) #num_isolated_subgraphs - количество изолированных подграфов в графе G1.

    message = [
        f"Число ребер в графе G1: {num_edges_G1}",
        f"Число ребер в графе G2: {num_edges_G2}",
        f"Число изолированных подграфов в графе G1: {num_isolated_subgraphs}"
]




    if nx.is_connected(G1):
        diameter_G1 = nx.diameter(G1)
        message.append(f"Диаметр графа G1: {diameter_G1}")
    else:
        message.append("Первый граф не является связным.")

    if nx.is_connected(G2):
        diameter_G2 = nx.diameter(G2)
        message.append(f"Диаметр графа G2: {diameter_G2}")
    else:
        message.append("Второй граф не является связным.")

    pos = nx.spring_layout(G1)
    nx.draw_networkx(G1, pos,node_color='#D0DB97')
    plt.title('Граф 1')
    plt.savefig('graphs_images/graph_source_1.png')
    plt.clf()

    pos = nx.spring_layout(G2)
    nx.draw_networkx(G2, pos,node_color='#D0DB97') #Рисует графы G1 и G2 с помощью nx.draw_networkx и сохраняет их в соответствующие файлы в папке "graphs_images".
    plt.title('Граф 2')
    plt.savefig('graphs_images/graph_source_2.png')
    plt.clf()

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('message_log.txt', 'r+') as file:
        # Чтение всех строк из файла
        lines = file.readlines()

        # Если файл содержит 100 строк, сбросить его содержимое
        if len(lines) >= 100:
            file.seek(0)
            file.truncate()

        # Формирование строки для записи в файл (с добавлением времени)
        log_line = f"{current_time} - {message}"

        # Запись содержимого переменной 'log_line' в файл
        file.write(log_line)
        file.write('\n' + '-' * 60 + '\n')

    return message