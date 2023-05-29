import networkx as nx
import matplotlib.pyplot as plt

# Определяем граф
G1 = nx.Graph()

# Задаем матрицу смежности вершин для первого графа
matrix1 = [[0, 1, 1, 0],
           [1, 0, 1, 1],
           [1, 1, 0, 1],
           [0, 1, 1, 0]]

# Определяем индексы отсутствующего ребра
missing_edge = None
for i in range(len(matrix1)):
    for j in range(i+1, len(matrix1)):
        if matrix1[i][j] == 0:
            missing_edge = (i+1, j+1)
            break
    if missing_edge is not None:
        break

# Добавляем отсутствующее ребро в граф
if missing_edge is not None:
    G1.add_edge(*missing_edge)

# Отображаем диаграмму данных графа
nx.draw(G1, with_labels=True)
plt.show()
