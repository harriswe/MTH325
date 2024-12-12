This is my interpretation of Kruskal's. There's an issue that is causing things to not look right, maybe something to do with sorting but I'm out of time for this now.

```
def find(parent, i):
  if parent[i] == i:
    return i
  return find(parent, parent[i])

def union(parent, rank, x, y):
  xroot = find(parent, x)
  yroot = find(parent, y)
  if rank[xroot] < rank[yroot]:
    parent[xroot] = yroot
  elif rank[xroot] > rank[yroot]:
    parent[yroot] = xroot 
  else:
    parent[yroot] = xroot 
    rank[xroot] += 1 

def kruskal(graph):
  n = len(graph)
  result = []
  i = 0
  e = 0
  graph = sorted(graph, key=lambda item: item[2], reverse=True) 
  parent = []
  rank = []
  for node in range(n):
    parent.append(node)
    rank.append(0)
  while e < n - 1:
    u, v, w = graph[i]
    i = i + 1 
    x = find(parent, u)
    y = find(parent, v)
    if x != y:
      e = e + 1
      result.append([u, v, w])
      union(parent, rank, x, y)
  return result
  ```
