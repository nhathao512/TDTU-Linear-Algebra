# -*- coding: utf-8 -*-
"""Lab9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ybBrysqwVqrrB7AgvswTdz36EfVOPii1
"""

#Exercise 9:
import numpy as np
import matplotlib.pyplot as plt
pts = np.array( [[0, 1, 3, 3, 4, 4, 5, 6, 5, 5, 3, 3, 2, 2, 1, 1, 0],
                [2, 3, 3, 4, 4, 3, 3, 2, 2, 0, 0, 1, 1, 0, 0, 2, 2]])
#a
tx = 2
ty = 4
transV = [[tx], [ty]]
trans_pts = np.add(transV, pts)
print("trans_pts= ",trans_pts)
plt.plot(pts[0], pts[1], 'r-')
plt.plot(trans_pts[0],trans_pts[1], 'go-')
plt.title("Translation")
plt.show()

#b
pi = math.pi
transV1 = np.array([[math.cos(pi/3), -math.sin(pi/3)],
                   [math.sin(pi/3), math.cos(pi/3)]])
trans_pts1 = np.matmul(transV1,pts)
print("trans_pts= ",trans_pts1)
plt.plot(pts[0], pts[1], 'r-')
plt.plot(trans_pts1[0], trans_pts1[1], 'go-')
plt.title("Rotation")
plt.show()

#c

trans_pts1 = np.vstack((pts[0]*2, pts[1]*3))
print("trans_pts= ",trans_pts1)
plt.plot(pts[0], pts[1], 'r-')
plt.plot(trans_pts1[0], trans_pts1[1], 'go-')
plt.title("Rotation")
plt.show()

#d
Sx = 0.5
Sy = -1.5

Shearx = np.array([[1, 0], [Sx, 1]])
Sheary = np.array([[1, Sy], [0, 1]])
trans_pts= np. matmul (Sheary, pts)
print("trans_pts= ",trans_pts)
plt.plot(pts[0], pts[1], 'r-') #'b-'
plt.plot(trans_pts[0], trans_pts[1], 'go-')
plt.title("Translation")
plt.show()

#Exercise 10:
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 3, 1, 1],
              [1, 1, 3, 1]])
transform_pts = np.matmul(-np.eye (2), A)
plt.plot(A[0], A[1], 'b-');
plt.plot(transform_pts[0], transform_pts[1], 'ro-');
plt.show()

#Exercise 11:
import numpy as np
import matplotlib.pyplot as plt

# 1st row is x-values, and 2nd row is y-values
pts = np.array([[2, 2, -3, -3, -2,   -2,    0, 0.0, -2.0, -2, 2],
		            [4, 5,  5, -5, -5, -0.5, -0.5, 0.5,  0.5,  4, 4]])
pts = np.vstack( (pts, np.ones(pts.shape[1]) ) )

print(pts)

T1 = [[-1,  0, 0],
      [ 0, -1, 0],
      [ 0,  0, 1]]

transform_pts = np.matmul( T1, pts )

f = plt.figure()
f.set_figwidth(5)
f.set_figheight(5)

plt.fill(pts[0], pts[1],'b')
plt.fill(transform_pts[0], transform_pts[1],'r')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(linestyle = '--')

plt.show()

#Exercise 12:
import numpy as np

x = np.array([2015, 2016, 2017, 2018, 2019])
y = np.array([12, 19, 29, 37, 45])

A = np.vstack([x, np.ones(len(x))]).T

m, b = np.linalg.lstsq(A, y, rcond=None)[0]

x_2020 = 2020
y_2020 = m * x_2020 + b
print("Estimated sales in 2020: ", y_2020)

#Exercise 13:
import numpy as np

A = np.array([[1, 2], [0, -3], [2, 6]])
b = np.array([1, 1, 0])
x, _, _, _ = np.linalg.lstsq(A, b, rcond=None)

vector = np.dot(A, x)

print("Coefficients:", x)
print("Vector in column space of A closest to b:", vector)