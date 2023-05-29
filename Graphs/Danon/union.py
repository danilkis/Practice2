import matplotlib.pyplot as plt
import networkx as nx

def create_union_graph(matrix1, matrix2):
    # Create empty union graph
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

    return union_graph

# Example matrices
matrix1 = [[0, 1, 1, 0],
           [1, 0, 1, 1],
           [1, 1, 0, 1],
           [0, 1, 1, 0]]
matrix2 = [[0, 1, 0, 1],
           [1, 0, 1, 0],
           [0, 1, 0, 1],
           [1, 0, 1, 0]]

# Create the union graph
union_graph = create_union_graph(matrix1, matrix2)

# Plot the graph
pos = nx.spring_layout(union_graph)
nx.draw_networkx(union_graph, pos)
plt.title('Объединение')
plt.show()
