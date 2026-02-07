import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
              mat1=np.array(a)
              mat2=np.array(b)

              if mat1.ndim != mat2.ndim:
                return -1
            
              if mat1.shape[1]!= mat2.shape[0]:
                return -1
            
              return np.matmul(mat1,mat2)