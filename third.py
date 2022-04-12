import pip
import numpy as np
x = np.array([22, 6, 7, 2])
y = np.array([25, 10, 24, 28])
z = np.column_stack ([x, y])
print(z.shape)
