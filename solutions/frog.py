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

# Recursive approach
# def jc(i, n):
#   pass

# def frog(i, n):
#   if i == n:
#     return 0
#   if i == n - 1:
#     return jc(i, i + 1)
#   else:
#     return min(
#       jc(i, i + 1) + f(i + 1, n),
#       jc(i, i + 2) + f(i + 2, n))
#     )

# Memoize
# def jc(i, n):
#   pass

# def frog(i, n, saved):
#     if i == n:
#       return 0
#     if i == n - 1:
#       return jc(i, i + 1)
#     if saved[i] is not None:
#       return saved[i]
#     else:
#       saved[i] = min(
#         jc(i, i + 1) + frog(i + 1, n, saved),
#         jc(i, i + 2) + frog(i + 2, n, saved)
#       )
#     return saved[i]

# Bottoms up right to left
# def solve():
#   frog[n] = 0
#   frog[n - 1] = jc(n - 1, )
#   for i in [n - 2..1]:
#     frog[i] = min(
#       jc(i, i + 1) + frog(i + 1, n, saved),
#       jc(i, i + 2) + frog(i + 2, n, saved)
#     )
#   return frog[1]

# Bottoms up left to right
# def jc(i, n):
#   return 0

# def solve(n):
#   min_cost = []
#   min_cost[1] = 0
#   min_cost[2] = jc(1, 2)
#   for i in range(3, n):
#     min_cost[i] = min(
#       min_cost[i - 2] + jc(i - 2, i),
#       min_cost[i - 1] + jc(i - 1, i),
#     )

#   return min_cost[n]
