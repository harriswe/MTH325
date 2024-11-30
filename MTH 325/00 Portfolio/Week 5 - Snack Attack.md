* Snack attack was an exercise introduced in class to learn about Matrices and matrix multiplication. 

## **Matrix Multiplication

Matrix multiplication is an operation that takes two matrices and produces another matrix. In order for matrix multiplication to be defined, **the number of columns in the first matrix must be equal to the number of rows in the second matrix.** The resulting matrix will have the same number of rows as the first matrix and the same number of columns as the second matrix.

The entry in the i row and j column of the product matrix is found by taking the product of the i row of the first matrix and the j column of the second matrix. For example, consider the following matrices:

```
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]
```

The product of A and B, denoted AB, is

```
AB = [[1*5+2*7, 1*6+2*8],
     [3*5+4*7, 3*6+4*8]]

  = [[19, 22],
     [43, 50]]
```

## **Adjacency Matrices**

An adjacency matrix is a square matrix that represents a finite graph. The rows and columns of the adjacency matrix are indexed by the vertices of the graph. The entry in the ith row and jth column is 1 if there is an edge from vertex i to vertex j, and 0 otherwise.

For example, consider the following graph:

[asy] unitsize(1 cm);

pair A, B, C;

A = (0,1); B = (1,1); C = (1,0);

draw(A--B--C--cycle);

label("A", A, N); label("B", B, NE); label("C", C, SE); [/asy]

The adjacency matrix for this graph is

```
[[0, 1, 1],
 [1, 0, 1],
 [1, 1, 0]]
```

**Applications of Matrix Multiplication and Adjacency Matrices**

Matrix multiplication and adjacency matrices have a number of applications in graph theory and other areas of mathematics. For example, the powers of an adjacency matrix can be used to count the number of paths of a given length between two vertices in a graph.

**Conclusion**

In this portfolio entry, I have demonstrated my understanding of matrix multiplication and adjacency matrices. I have also discussed some of the applications of these concepts.