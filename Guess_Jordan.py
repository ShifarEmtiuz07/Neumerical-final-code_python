import sys

import numpy as np

n = int(input("enter the num:"))

a = [[3, -0.1, -0.2, 7.85], [0.1, 7, -0.3, -19.3], [0.3, -0.2, 10, 71.4]]

x = np.zeros(n)

for i in range(n):
    if a[i][i] == 0.0:
        sys.exit

    for j in range(n):
        if i != j:
            ratio = a[j][i] / a[i][i]

            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]
print(a)

for i in range(n):
    x[i] = a[i][n] / a[i][i]

print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')
