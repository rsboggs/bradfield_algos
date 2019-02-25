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

  if not next:
    return -1
  minimum = min(next)
  maximum = max(next)
  if minimum == -1 and maximum == -1:
    return -1
  else:
    return minimum

# Memoize Recursion
def minimum_count2(coins, amount, saved = {}):
  if amount < 0:
    return -1
  elif amount == 0:
    return 0

  memoize_key = (tuple(coins), amount)
  if memoize_key in saved:
    return saved[memoize_key]

  count = None
  for coin in sorted(coins, reverse=True):
    if amount - coin >= 0:
      added_count = minimum_count2(coins, amount - coin, saved)
      if added_count != -1 and (count == None or added_count < count):
        count = added_count + 1

  saved[memoize_key] = -1 if count == None else count
  return saved[memoize_key]