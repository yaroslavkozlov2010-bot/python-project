import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [7, 2, 8],
    [5, 7, 1],
    [3, 2, 1]
])

C = A @ B

print(f'Матрица A:\n{A}')
print(f'\nМатрица B:\n{B}')
print(f'\nМатрица C:\n{C}')

det_A = np.linalg.det(A)
det_B = np.linalg.det(B)
det_C = np.linalg.det(C)


print(f'\nОпределитель матрицы A: {det_A}')
print(f'\nОпределитель матрицы B: {det_B}')
print(f'\nОпределитель матрицы C: {det_C}')
