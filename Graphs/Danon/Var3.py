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
