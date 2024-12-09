
- I will be using Exercises from Dr. Wells' textbook - [Data Structures Done Discretely.](https://faculty.gvsu.edu/wellsc/discrete/data_structures_done_discretely.html)
- Using measure of success [[Measures of Success#^74fe05 | here]].
## Disjunctive Conclusion

![[Pasted image 20241122101216.png | ]]
**Proof:**

- **b is even.** If b is even, then the statement "either b is even or ab is odd" is true. 
    
- **b is odd.** Since a is odd, and we're assuming b is odd in this case, let's show them generally:
    
    - a = 2k + 1 (where k is any integer)
    - b = 2m + 1 (where m is any integer)
    
    Now, to calculate ab: ab = (2k + 1)(2m + 1) = 4km + 2k + 2m + 1 = 2(2km + k + m) + 1
    
    This shows that ab can be written in the form 2n + 1 (where n = 2km + k + m), which means ab is odd.
    

**Conclusion:**

- If b is even, the statement is true
- If b is odd, then ab is odd, and the statement is still true.
## Contrapositive
![[Pasted image 20241129140740.png]]

**Contrapositive:** If x = 5, then x² = 25.

**Proof:**

We'll assume the contrapositive is true: x = 5.

Now, we can directly calculate x²:

x² = 5² = 25

This confirms the contrapositive: if x = 5, then x² = 25.

**The contrapositive is true, so the original statement is also true.**

## Contradiction

![[Pasted image 20241129140914.png]]

1. **Assumption:** Let's assume the opposite of our conjecture. Suppose 300 _does_ have a factor, let's call it 'k', where 100 < k < 150.
    
2. **Consequences:** If k is a factor of 300, this means there exists another integer 'm' such that:
    
    k * m = 300
    
    Since 100 < k < 150, let's consider the possible values for 'm':
    
    - **If m ≥ 3:** Then k * m would be greater than 300 (e.g., 101 * 3 = 303), which contradicts our equation k * m = 300.
        
    - **If m = 2:** Then k would have to be 150 (150 * 2 = 300), but this contradicts our assumption that k is less than 150.
        
    - **If m = 1:** Then k would have to be 300, which again contradicts our assumption that k is _less than_ 150.
    
*May not be inclusive of all possible cases*
3. **Contradiction:** We've explored all possible integer values for 'm', and in each case, we find a contradiction. This means our initial assumption that 300 has a factor between 100 and 150 must be false.

## Induction

### Weak Induction (Trees)

^12ff6c

**Conjecture:** In any tree with `n` vertices, there are `n-1` edges.

**Proof by Weak Induction:**

- **Base Case:** For n = 1 (a single vertex), there are 0 edges. This satisfies the theorem (1 - 1 = 0).
    
- **Hypothesis:** Assume the theorem holds true for a tree with `k` vertices (i.e., a tree with `k` vertices has `k-1`edges).
    
- **Inductive Step:** We need to show that the theorem also holds true for a tree with `k+1` vertices.
    
    - Consider a tree `T` with `k+1` vertices.
    - Remove a leaf vertex (a vertex with only one edge) and its associated edge from `T`. This results in a new tree `T'` with `k` vertices.
    - By the inductive hypothesis, `T'` has `k-1` edges.
    - Since we removed one edge to get `T'`, the original tree `T` must have had `k-1 + 1 = k` edges.
    - Therefore, the theorem holds for a tree with `k+1` vertices.
- **Conclusion:** By the principle of weak induction, the theorem holds for all trees with `n` vertices.
### Strong Induction (Spanning Trees)

**Conjecture:** Every connected graph with `n` vertices (where n ≥ 2) has a spanning tree.

**Strong Induction:**

- **Base Case:** For n = 2 (two vertices connected by an edge), the graph itself is a spanning tree.
    
- **Inductive Hypothesis:** Assume the theorem holds true for all connected graphs with `k` vertices, where `2 ≤ k ≤ m`.
    
- **Inductive Step:**

1. Start with a connected graph `G` with `m+1` vertices.
2. Remove any edge `e` from `G`. This might divide the graph into two connected components (or leave it as a single component).
3. Each connected component has at most `m` vertices.
4. By the inductive hypothesis, each connected component has a spanning tree.
5. Reconnect the components using the removed edge `e`. This forms a spanning tree for the original graph `G`.
- **Conclusion:** By the principle of strong induction, the theorem holds for all connected graphs with `n` vertices (where n ≥ 2).