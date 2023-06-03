import networkx as nx
import numpy as np
from matplotlib import pyplot as plt


def draw_graphs(matrix_str1, matrix_str2):
    G1 = nx.Graph()
    G2 = nx.Graph()
    matrix1 = np.array(eval(matrix_str1))
    matrix2 = np.array(eval(matrix_str2))

    G1.clear()
    G2.clear()

    # Add nodes and edges to each graph based on the adjacency matrix
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

    # Display the graphs
    num_edges_G1 = G1.number_of_edges()
    num_edges_G2 = G2.number_of_edges()
    num_isolated_subgraphs = nx.number_connected_components(G1)

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
    nx.draw_networkx(G2, pos,node_color='#D0DB97')
    plt.title('Граф 2')
    plt.savefig('graphs_images/graph_source_2.png')
    plt.clf()

    with open('message_log.txt', 'r+') as file:
    # Read all lines from the file
        lines = file.readlines()

    # If the file has reached 100 lines, reset it
        if len(lines) >= 100:
            file.seek(0)
            file.truncate()

    # Write the contents of the 'message' variable to the file
        file.write('\n'.join(message))
        file.write('\n' + '-' * 60 + '\n')

    return message