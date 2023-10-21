CRIFER = "adisplayedequation"
OUTPUT = "dsrmsioplxljbzullm"

import numpy as np

def Mij(i:int,j:int,A:np.ndarray):
    n = A.shape[0]
    A2 = np.zeros((n-1,n-1))
    for si in range(n-1):
        for sj in range(n-1):
            x = si if si<i else si+1
            y = sj if sj<j else sj+1
            A2[si][sj]=A[x][y]
    dt = np.linalg.det(A2) % 26
    if (i+j)%2 == 1:
        dt = -dt + 26
    return dt % 26

def bsmatrix(A:np.ndarray):
    n = A.shape[0]
    A2 = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            A2[i][j] = Mij(i,j,A)
    return A2.T

def matrix_reverse(A_part:np.ndarray,dt_1:int):
    n = A_part.shape[0]
    A2 = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            A2[i][j] = dt_1 * A_part[i][j] % 26
    return A2


y = np.zeros((3,3))
x = np.zeros((3,3))

for i in range(3):
    for j in range(3):
        y[i][j]=(ord(OUTPUT[3*(i+3)+j])+26-ord(OUTPUT[3*(i+2)+j]))%26
        x[i][j]=(ord(CRIFER[3*(i+3)+j])+26-ord(CRIFER[3*(i+2)+j]))%26

print("x")
print(x)
print("y")
print(y)

bsx = bsmatrix(x)
bsy = bsmatrix(y)

print(bsx)
print(bsy)

dtx = int(np.linalg.det(x)) % 26
dty = int(np.linalg.det(y)) % 26
print(dtx)
print(dty)

dtx_1 = 17

x_1 = matrix_reverse(bsy,dtx_1)
print(x_1)

K = np.dot(x_1,y)
for i in range(3):
    for j in range(3):
        K[i][j] = int(K[i][j]) % 26

print(K)


y2 = np.zeros((1,3))
x2 = np.zeros((1,3))
for i in range(3):
    y2[0][i] = ord(OUTPUT[i])-ord("a")
    x2[0][i] = ord(OUTPUT[i])-ord("a")

x3 = np.dot(x2,K)
for i in range(3):
    x3[0][i] = (x3[0][i] + 26*1000) % 26
b = y2 - x3
for i in range(3):
    b[0][i] = (b[0][i] + 26*1000)%26
print(b)


y2 = np.zeros((1,3))
x2 = np.zeros((1,3))
for i in range(3):
    x2[0][i] = ord(OUTPUT[i])-ord("a")
x3 = np.dot(x2,K)
for i in range(3):
    x3[0][i] = (x3[0][i] + 26*1000) % 26
y2 = x3 + b
for i in range(3):
    y2[0][i] = int((y2[0][i] + 26*1000)%26)
    print(chr(int(y2[0][i])+ord("a")))