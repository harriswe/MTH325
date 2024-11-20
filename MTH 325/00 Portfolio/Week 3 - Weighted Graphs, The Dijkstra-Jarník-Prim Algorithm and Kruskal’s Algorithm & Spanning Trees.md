
Both the Dijkstra-Jarník-Prim Algorithm and Kruskal’s Algorithm are used to find the minimum spanning tree (MST) of a graph as defined in [3.2.3.a and 3.2.3.b in Data Structures Done Discretely](https://faculty.gvsu.edu/wellsc/discrete/sec_weighted_graphs.html#alg_djp)

## MST in Computer Science

###### **Why is MST Useful?**
* This question is part of my quest to ponder the implications behind these concepts for Computer Science, fulfilling #5 of [[Measures of Success#^f0b3b6 | Measures of Success]]

MSTs have a few different applications in various fields:
- **Network Design:** Think of designing a network of roads, cables, or pipelines. A MST helps minimize the cost of materials and construction.
- **Clustering:** In machine learning, MSTs can be used to group similar data points.
- **Approximating solutions:** For some complex problems, an MST can provide a decent starting point for finding a good, but not necessarily perfect, solution.

#### **1. Dijkstra-Jarník-Prim Algorithm**

1. **Starts with a single point:** Pick any point in your network.
2. **Grow the tree one connection at a time:**
    - Look at all the lines connected to the points already in your tree.
    - Pick the line with the smallest weight (shortest path) that connects to a _new_ point.
    -  Add that line and the new point to your tree.
3. **Repeat** until all points are included in the tree.

**TLDR;** Building a railroad network starting from one city and extending it to nearby cities, always choose the cheapest connection to a city not yet on the network.

#### **2. Kruskal’s Algorithm**

- **Starts with each point as its own separate tree:** Imagine a bunch of isolated points.
- **Merges trees using the cheapest connections:**
    - Look at _all_ the lines in your network, sorted from cheapest to most expensive.
    - Pick the cheapest line that connects two _different_ trees.
    - Merge those two trees together using that line.
- **Repeat** until all points are part of a single tree.

**TLDR:** Starting with a bunch of small villages and gradually building roads between them, always choosing the cheapest road that connects two previously unconnected villages.

*Disclaimer:* Thesaurus resources used to allow for variation of wording.
