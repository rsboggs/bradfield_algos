def stone_jump(n, stones):
  jumps = {}
  lowest_cost = None

  stack = []
  if n == 2:
    stack.append((0, 1, 0))
  elif n > 2:
    stack.append((0, 2, 0))
    stack.append((0, 1, 0))

  while stack:
    current_index, next_index, cost = stack.pop()
    next_path = (current_index, next_index)
    if next_path not in jumps:
      jumps[next_path] = abs(stones[current_index] - stones[next_index])

    new_cost = cost + jumps[next_path]
    if next_index + 1 == n:
      if lowest_cost is None or new_cost < lowest_cost:
        lowest_cost = new_cost
    elif next_index + 2 == n:
      stack.append((next_index, next_index + 1, new_cost))
    else:
      stack.append((next_index, next_index + 2, new_cost))
      stack.append((next_index, next_index + 1, new_cost))

  return lowest_cost
