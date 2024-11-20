def havel_hakimi(sequence):
  """
  Represents the Havel-Hakimi algorithm to check if a degree sequence can represent a more simple graph.

  Params:
    sequence: A list of non-negative integers representing the degrees of vertices.

  Returns:
    True if the sequence is a graph (represents a simple graph), False otherwise.
  """

  while True:
    # Step 1: Remove any zeros from the sequence
    sequence = [d for d in sequence if d > 0]

    # Step 2: If the sequence is empty, technically it's still a graph.
    if not sequence:
      return True

    # Step 3: Sequence sorted in reverse by decreasing vertices.
    sequence.sort(reverse=True)

    # Step 4: Check if the first element is larger than the length (not possible to use algorithm).
    if sequence[0] >= len(sequence):
      return False

    # Step 5: Subtract 1 from the next element in the sequence.
    for i in range(1, sequence[0] + 1):
      sequence[i] -= 1

  # This point should never be reached but just in case...
  return False