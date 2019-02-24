# Recursion
def minimum_count(coins, amount, count = 0):
  if amount < 0:
    return -1
  elif amount == 0:
    return count

  next = []
  for coin in coins:
    if amount - coin >= 0:
      next.append(minimum_count(coins, amount - coin, count + 1))

  minimum = min(next)
  maximum = max(next)
  if minimum == -1 and maximum == -1:
    return -1
  else:
    return minimum
