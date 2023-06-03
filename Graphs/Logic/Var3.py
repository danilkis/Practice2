import numpy as np
#import make
# Расчет степеней вершин
def calculate_vertex_degrees(adj_matrix):
    degrees = []
    for row in adj_matrix:
        degree = sum(row) # Суммируем значения в строке матрицы
        degrees.append(degree)
    return degrees

# Поиск всех правильных графов из N вершин
def find_all_regular_graphs(N):
    # Инициализация графа с N вершинами
    adj_matrix = [[0] * N for _ in range(N)]

    # Инициализация степеней вершин
    degrees = [N-1] * N

    # Общее количество ребер в полном графе
    total_edges = N * (N-1) // 2

    # Перебор возможных ребер
    for i in range(N-1):
        for j in range(i+1, N):
            if degrees[i] > 0 and degrees[j] > 0:
                adj_matrix[i][j] = 1
                adj_matrix[j][i] = 1
                degrees[i] -= 1
                degrees[j] -= 1
                total_edges -= 1

    # Проверка на правильность графа
    if total_edges == 0 and all(degrees[i] == 0 for i in range(N)):
        return adj_matrix
    else:
        return None

def Fill(matrix_str1,matrix_str2,N):
    adj_matrix1 = np.array(eval(matrix_str1))
    adj_matrix2 = np.array(eval(matrix_str2))

    #make.draw_graphs(adj_matrix1, adj_matrix2)

    degrees1 = calculate_vertex_degrees(adj_matrix1)
    degrees2 = calculate_vertex_degrees(adj_matrix2)

    message = [
        f"Степень вершин в графе G1: {degrees1}",
        f"Степень вершин в графе G2: {degrees2}",
    ]



    # 2) Поиск всех правильных графов из N вершин
    regular_graphs = find_all_regular_graphs(N)

    if regular_graphs:
        message.append("Regular graph with", N, "vertices found:")
    else:
        message.append("No regular graph with", N, "vertices found.")

    return message
