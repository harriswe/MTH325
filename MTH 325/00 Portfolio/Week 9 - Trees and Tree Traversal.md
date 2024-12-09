See proof of [[Week 6 & 7 - Proofs and Relations#^12ff6c | Weak Induction]] about trees in addition to the below:

## In-Order Traversal 

The below is a python function that encapsulates traversal.
```
 class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# In-order traversal function
def inorder_traversal(root):
    if root:
        # Traverse the left subtree
        inorder_traversal(root.left)
        # Visit the root node
        print(root.val, end=' ')
        # Traverse the right subtree
        inorder_traversal(root.right)

# Example usage
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("In-order traversal of the binary tree:")
    inorder_traversal(root)

```
### What Happens Here?

1. The tree is walked through in a very organized fashion: **left subtree -> root -> right subtree**.

## Prüfer Sequences: The IKEA of Trees

At first, Prüfer sequences seemed like a random, abstract concept... but they’re actually genius. They condense a tree into a string of numbers that uniquely describes it. If traversal is like walking through a tree, Prüfer sequences are the **blueprint** for how it’s made.

### My Take:

Think of it like disassembling a tree:

1. Peel off the smallest leaf and write down its buddy (the connected node).
2. Keep going until there’s nothing left but the core.

It’s amazing how this little sequence can hold all the info you need to rebuild the tree. It makes me think about how much data we trash when we simplify problems using code as well.
