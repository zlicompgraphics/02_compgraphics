"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)): # rows
        for j in range(len(matrix[i])): # columns
            if i == j:
                matrix[i][j] = 1.0
            else:
                matrix[i][j] = 0.0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    c = len(m2[0])
    temp = new_matrix(c, 4)
    for i in range(4): # number of rows in m1
        for j in range(c): # number of columns in m2
            for k in range(4):
                temp[i][j] += m1[i][k] * m2[k][j]
    for i in range(4):
        for j in range(c):
            m2[i][j] = temp[i][j]

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m