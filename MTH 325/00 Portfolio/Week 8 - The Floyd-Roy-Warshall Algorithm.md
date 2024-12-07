
This algorithm uses a table (a matrix) to store and update the shortest distances between vertices. Each entry `(i, j)` in the table represents the shortest distance found so far between vertex `i` and vertex `j`.

1. **Initialization:** The table is initialized with the direct distances between vertices. If there's no direct edge, the distance is set to infinity (∞).

3. **Iteration:** The algorithm iterates through all vertices, considering each as a potential intermediate vertex (`k`). For each pair of vertices `(i, j)`, it checks if going through `k` results in a shorter path:

    - If `distance(i, k) + distance(k, j) < distance(i, j)`, then update `distance(i, j)` with the shorter distance.
3. **Completion:** After iterating through all the possibilities, we're left with the correct matrix.
    

I had great difficulty figuring out how to digitalize matrices, especially sequentially. I'd have included a more comprehensive example if not due to this. 