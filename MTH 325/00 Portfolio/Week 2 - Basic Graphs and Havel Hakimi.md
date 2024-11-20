## Havel-Hakimi Algorithm
- Below is the python implementation I created of the Havel-Hakimi algorithm. There were a few interesting conditions to work through, but I believe I've captured the most important pieces of it. Fulfills measure of success [[Measures of Success#^57af06 | number 1]].
```
def havel_hakimi(sequence):  
  """  
  This is the Havel-Hakimi algorithm to check if a degree sequence can represent a more simple graph.  
  Params:    sequence: A list of non-negative integers representing the degrees of vertices.  
  Returns:    True if the sequence is a graph (represents a simple graph), False otherwise.  """  
  
  while True:  
    
    sequence = [d for d in sequence if d > 0]  

    if not sequence:  
      return True  
      
    #sorted in reverse by decreasing vertices.  
    
    sequence.sort(reverse=True)  
    
    if sequence[0] >= len(sequence):  
      return False   
    
    for i in range(1, sequence[0] + 1):  
      sequence[i] -= 1  
  
  # This point should not be reached but just in case...  
  return False
```
![[havel_hakimi.py]]

