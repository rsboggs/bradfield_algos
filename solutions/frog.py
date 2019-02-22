def jump_cost(value1, value2):
  return abs(value1 - value2)

def stone_jump(n, stones):
  cost = [float("inf")] * n
  cost[0] = 0

  for index in range(len(stones) - 1):
    cost[index + 1] = min(cost[index + 1], cost[index] + jump_cost(stones[index], stones[index + 1]))
    if index + 2 < n:
      cost[index + 2] = min(cost[index + 2], cost[index] + jump_cost(stones[index], stones[index + 2]))

  return cost[-1]
