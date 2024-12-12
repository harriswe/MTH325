
This algorithm uses a table (a matrix) to store and update the shortest distances between vertices. Each entry `(i, j)` in the table represents the shortest distance found so far between vertex `i` and vertex `j`.

**Initialization:** The array is initialized with the direct distances between vertices. If there's no direct edge, the distance is set to infinity (∞).

**Iteration:** The algorithm iterates through all vertices, considering each as a potential intermediate vertex (`k`). For each pair of vertices `(i, j)`, it checks if going through `k` results in a shorter path:

    - If `distance(i, k) + distance(k, j) < distance(i, j)`, then update `distance(i, j)` with the shorter distance.


This video really helped explain how to grasp the programming part of this. https://www.youtube.com/watch?v=4OQeCuLYj-4

I was able to easily convert between swift (example) and python here.

Here's my algorithm:

```
def floyd_warshall(graph):
  n = len(graph) # Number of Vertices
  
# Distance between vertices
  dist = [[float('inf') for _ in range(n)] for _ in range(n)]  
  
  for i in range(n):
    for j in range(n):
      if i == j: 
        dist[i][j] = 0
      elif graph[i][j] != float('inf'): 
        dist[i][j] = graph[i][j]
        
# checks if going from vertex `i` to `j` through vertex `k` results in a shorter path than the current shortest path between `i` and `j`. If it does, the distance in `dist` is updated. #

  for k in range(n):
    for i in range(n):
      for j in range(n):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
  return dist
```




