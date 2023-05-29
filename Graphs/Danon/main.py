import networkx as nx
import matplotlib.pyplot as plt

# Определяем графы
G1 = nx.Graph()
G2 = nx.Graph()

# Задаем матрицы смежности вершин для каждого графа
matrix1 = [[0, 1, 1, 0],
           [1, 0, 1, 1],
           [1, 1, 0, 1],
           [0, 1, 1, 0]]

matrix2 = [[0, 1, 0, 1],
           [1, 0, 1, 0],
           [0, 1, 0, 1],
           [1, 0, 1, 0]]

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
nx.draw(G1, with_labels=True)
plt.show()

nx.draw(G2, with_labels=True)
plt.show()

# Определяем число ребер в каждом графе
num_edges_G1 = G1.number_of_edges()
num_edges_G2 = G2.number_of_edges()

print("Число ребер в графе G1: ", num_edges_G1)
print("Число ребер в графе G2: ", num_edges_G2)

# Определяем число изолированных подграфов в первом графе
num_isolated_subgraphs = nx.number_connected_components(G1)
print("Число изолированных подграфов в графе G1: ", num_isolated_subgraphs)

# Определяем диаметр второго графа
diameter_G2 = nx.diameter(G2)
print("Диаметр графа G2: ", diameter_G2)