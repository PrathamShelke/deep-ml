import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	A=np.array(matrix)
	eigenvalues, eigenvectors = np.linalg.eig(A)
	return eigenvalues.tolist()