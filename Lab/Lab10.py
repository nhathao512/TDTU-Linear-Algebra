# -*- coding: utf-8 -*-
"""Lab10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XNVETi9nSLwBTGxaaITPJFQDc-2fvdzg
"""

#Exercise 1:
import numpy as np
#a
print('a)')
A = np.array([[-1, 3.5, 14],
              [0, 5, -26],
              [0, 0, 2]])

eval_A = np.linalg.eigvals(A)
print("1. eigenvalues = ", eval_A)

w, v = np.linalg.eig(A)
print("2. eigenvalues = ", w)
print("3. eigenvectors = ", v)
print()

#b
print('b)')
B = np.array([[-2, 0, 0],
              [99, 0, 0],
              [10, -4.5, 10]])

eval_B = np.linalg.eigvals(B)
print("1. eigenvalues = ", eval_B)

w, v = np.linalg.eig(B)
print("2. eigenvalues = ", w)
print("3. eigenvectors = ", v)
print()

#c
print('c)')
C = np.array([[5, 5, 0, 2],
              [0, 2, -3, 6],
              [0, 0, 3, -2],
              [0, 0, 0, 5]])

eval_C = np.linalg.eigvals(C)
print("1. eigenvalues = ", eval_C)

w, v = np.linalg.eig(C)
print("2. eigenvalues = ", w)
print("3. eigenvectors = ", v)
print()

#d
print('d)')
D = np.array([[3, 0, 0, 0],
              [6, 2, 0, 0],
              [0, 3, 6, 0],
              [2, 3, 3, -5]])

eval_D = np.linalg.eigvals(D)
print("1. eigenvalues = ", eval_D)

w, v = np.linalg.eig(D)
print("2. eigenvalues = ", w)
print("3. eigenvectors = ", v)
print()

#e
print('e)')
E = np.array([[3, 0, 0, 0, 0],
              [-5, 1, 0, 0, 0],
              [3, 8, 0, 0, 0],
              [0, -7, 2, 1, 0],
              [-4, 1, 9, -2, 3]])

eval_E = np.linalg.eigvals(E)
print("1. eigenvalues = ", eval_E)

w, v = np.linalg.eig(E)
print("2. eigenvalues = ", w)
print("3. eigenvectors = ", v)
print()

#Exercise 2:
import numpy as np
a12 = [32, 31.9, 31.8, 32.1, 32.2]
for a in a12:
  E2a = np.array([[-6, 28, 21],
                  [4, -15, -12],
                  [8,a,25]])

  #w, v np.linalg.eig(E2a)
  w = np.linalg.eigvals (E2a)
  print("Eigenvalues with a = ",a, "is: ", w)
  E2a = np.array([[-6, 28, 21], [4, -15, -12], [8,a,25]])
  print("Eigenvalues of A with a = ",a, "is: ", w) # trị riêng

#Plot đồ thị
from matplotlib import pyplot as plt
from sympy import *
A = np.array([[-6, 28, 21],[4, -15, -12],[8, 0, 15]])
#alpha = np.array([32, 31.9, 31.8, 32.1, 32.2])
alpha = [32, 31.9, 31.8, 32.1, 32.2]
color = ['b', 'r', 'g', 'k', 'c', 'm']
t = symbols('t')
x = np.arange(0, 3, 0.05)
fig = plt.figure()
#for i, alp in enumerate(alpha):  #alpha = [32, 31.9, 31.8, 32.1, 32.2]
i = 0
for alp in alpha:  #alpha = [32, 31.9, 31.8, 32.1, 32.2]
    B = A  #Sao chép ma trận A sang ma trận B
    B[2,1] = alp # Gán tham số a vào ma trận B
    lambd = np.linalg.eigvals(B)
    p = 1

    for j in range(len(lambd)):
      p = p*(lambd[j] - t)
    y = lambdify(t, p, "numpy")(x)
    plt.plot(x, y, color[i])
    i = i + 1
plt.show()

#Exercise 4:
import numpy as np

A = np.array([[-2, 2, -3],
              [2, 1, -6],
              [-1, -2, 0]])

eigenvalues, eigenvectors = np.linalg.eig(A)

for i in range(len(eigenvalues)):
    print("Eigenvalue: ",eigenvalues[i])
    print("Eigenvector: ",eigenvectors[:,i])
    print()

AT = A.T
eigenvalues_AT, eigenvectors_AT = np.linalg.eig(AT)

for i in range(len(eigenvalues_AT)):
    print("Eigenvalue: ",eigenvalues_AT[i])
    print("Eigenvector: ",eigenvectors_AT[:,i])
    print()

A_inv = np.linalg.inv(A)
eigenvalues_A_inv, eigenvectors_A_inv = np.linalg.eig(A_inv)

for i in range(len(eigenvalues_A_inv)):
    print("Eigenvalue: ",eigenvalues_A_inv[i])
    print("Eigenvector: ", eigenvectors_A_inv[:,i])
    print()

#Exercise 5:
import numpy as np
#An n×n-matrix A is said to be diagonalizable if it can be written on the form
#  A = P * D * P^-1
#where D is a diagonal n×n matrix with the eigenvalues of A,
#and P is a nonsingular n×n matrix consisting of the eigenvectors
import numpy as np

def checkDiagonalizable(A):
  w, P = np.linalg.eig(A) # w is eigenvalues of A; P is vectorvalues of A
  print("w = ",w)
  D = np.diag(w) #Chuyển thành ma trận đường chéo của w
  print("D = \n",D)
  print("--------")
  P_1 = np.linalg.inv(P)

  res = np.matmul(np.matmul(P,D),P_1)
  print("res = \n",res)
  return np.allclose(A, res) #if A = res return True

A1 = np.array([[4, -5],
               [2, -3]])
print(checkDiagonalizable(A1))

A2 = np.array([[0, 2],
               [0, 1]])
print(checkDiagonalizable(A2))

A3 = np.array([[2, 3],
               [1, 4]])
print(checkDiagonalizable(A3))

A4 = np.array([[1, 2, -2],
               [-2, 5, -2],
               [-6, 6, -3]])
print(checkDiagonalizable(A4))

A5 = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]])
print(checkDiagonalizable(A5))

#Exercise 6:
import numpy as np

A = np.array([[1, 2, -2],
              [0, 3, -2],
              [0, 0, 1]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)
print()

print("Eigenvectors:")
print(eigenvectors)
print()
P = eigenvectors
P_inv = np.linalg.inv(P)
D = np.diag(eigenvalues)
P_inv_A_P = P_inv @ A @ P
print("P:")
print(P)
print()

print("P^-1:")
print(P_inv)
print()

print("D:")
print(D)
print()

print("P^-1AP:")
print(P_inv_A_P)

#Exercise 7:

import numpy as np

A1 = np.array([[1, 0],
               [0, -3]])

A2 = np.array([[-5, 0],
               [0, 0]])

A3 = np.array([[np.sqrt(6), 1],
               [0, np.sqrt(6)]])

A4 = np.array([[np.sqrt(3), 2],
               [0, np.sqrt(3)]])

u, s, vh = np.linalg.svd(A1)
print("A1 - the singular values of the matrices is:", s)
u, s, vh = np.linalg.svd(A2)
print("A2 - the singular values of the matrices is:", s)
u, s, vh = np.linalg.svd(A3)
print("A3 - the singular values of the matrices is:", s)
u, s, vh = np.linalg.svd(A4)
print("A4 - the singular values of the matrices is:", s)

#Exercise 8:
import numpy as np

B1 = np.array([[-18, 13, -4, 4],
               [2, 19, -4, 12],
               [-14, 11, -12, 8],
               [-2, 21, 4, 8]])

B2 = np.array([[6, -8, -4, 5, -4],
               [2, 7, -5, -6, 4],
               [0, -1, -8, 2, 2],
               [-1, -2, 4, 4,-8]])

U1,S1,V1 = np.linalg.svd(B1)
U2,S2,V2 = np.linalg.svd(B2)

print("SVD of B1:")
print("U = ")
print(U1)
print("S = ")
print(S1)
print("V^T = ")
print(V1.T)
print()

print("SVD of B2:")
print("U = ")
print(U2)
print("S = ")
print(S2)
print("V^T = ")
print(V2.T)