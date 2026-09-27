def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix or not matrix[0]:
        return []

    m = len(matrix)       # 行数
    n = len(matrix[0])    # 列数
    means = []

    if mode == 'column':
        for col in range(n):
            col_sum = 0
            for row in range(m):
                col_sum += matrix[row][col]  # 注意：行在先，列在后
            means.append(col_sum / m)

    elif mode == 'row':
        for row in range(m):
            row_sum = 0
            for col in range(n):
                row_sum += matrix[row][col]
            means.append(row_sum / n)

    return means