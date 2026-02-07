import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	mat=np.array(matrix)
	if mode=="column":
		return np.mean(mat,axis=0).tolist()
	if mode=="row":
		return np.mean(mat,axis=1).tolist()
		