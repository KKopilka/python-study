import random
m = 4
n = 4
mat = [ [ random.randint(-100, 100) for j in range(n)] for i in range(m) ]
print('Matrix:')
for i in range(m):
    print(mat[i])
