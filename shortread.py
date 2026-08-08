import pandas as pd
import numpy as np

df = pd.read_csv("typechart.txt", sep='\t', index_col='Type')
matrix = df.to_numpy()
eigenvalues = np.linalg.eig(matrix).eigenvalues
print(eigenvalues)
