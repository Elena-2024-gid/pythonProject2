def get_matrix (n, m, value):
    matrix = []
    for N in range (0,n):
        matrix.append([])
        for M in range (0,m):
            matrix[N].append(value)
    return matrix
result1 = get_matrix(2,3,5)
print(result1)