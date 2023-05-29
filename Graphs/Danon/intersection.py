import matplotlib.pyplot as plt
import networkx as nx

def create_intersection_graph(matrix1, matrix2): #todo: Посмотреть что тут
    # Create empty intersection graph
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

    return intersection_graph

# Example matrices
matrix1 = [[0, 1, 1, 0],
           [1, 0, 1, 1],
           [1, 1, 0, 1],
           [0, 1, 1, 0]]
matrix2 = [[0, 1, 0, 1],
           [1, 0, 1, 0],
           [0, 1, 0, 1],
           [1, 0, 1, 0]]

# Create the intersection graph
intersection_graph = create_intersection_graph(matrix1, matrix2)

# Plot the graph
pos = nx.spring_layout(intersection_graph)
nx.draw_networkx(intersection_graph, pos)
plt.title('Пересечение')
plt.show()
