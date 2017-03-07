#!/usr/bin/python3

#Example code for problem 3 in python

import sys

#returns the minor corresponding to the given rows and columns
#where rows cols are lists of integers (zero indexed
def minor(matrix,rows,cols):
    if len(rows)!=len(cols):
        print("Can't take the minor of a non-square submatrix");
        return None;
    if len(rows)==1:
        return matrix[rows[0]][cols[0]];
    else:
        ret = 0
        newCols = cols[1:]
        for i in range(0,len(rows)):
            newRows = rows[:i] + rows[i+1:]
            ret += matrix[rows[i]][cols[0]]*(1 if i%2==0 else -1)*minor(matrix,newRows,newCols);
        return ret;

#returns the determinant of a matrix
#The matrix is represented by a list of lists
#The value is computed using Laplace Expansion.
def det(matrix):
    return minor(matrix,list(range(0,len(matrix))),list(range(0,len(matrix))));

line = sys.stdin.readline();
n = int(line);
matrix = []
for i in range(0,n):
    line = sys.stdin.readline();
    matrix.append(list(map(int,line.split())));
print(det(matrix))
