* Snack attack was an exercise introduced in class to learn about Matrices and matrix multiplication. 

## **Matrix Multiplication

Matrix multiplication is an operation that takes two matrices and produces another matrix. In order for matrix multiplication to be defined, **the number of columns in the first matrix must be equal to the number of rows in the second matrix.** The resulting matrix will have the same number of rows as the first matrix and the same number of columns as the second matrix.

The entry in the i row and j column of the product matrix is found by taking the product of the i row of the first matrix and the j column of the second matrix:

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

## What’s an Adjacency Matrix?

An adjacency matrix is just a way to represent a graph using a grid of numbers. If you’ve got a graph, each row and column of the matrix represents one of its vertices. The entries in the matrix tell you whether there’s an edge (a connection) between two vertices:

- **1** = There’s an edge.
- **0** = No edge.

### My Take:

It’s like a friendship chart for vertices. If two vertices are "friends" (connected by an edge), the matrix marks it with a 1. Otherwise, it’s a 0.