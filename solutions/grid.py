MOD = 10 ** 9 + 7

# h, w place trying to reach on grid
# top left of grid is 1,1
# move only down & to right
def number_paths(h, w, grid):
  memo = [[1] * w for _ in range(0, h)]

  for i, row, in enumerate(memo):
    for j, _ in enumerate(row):
      if blocked_spot(grid, i, j) or (i == 0 and memo[i][j - 1] == 0) or (j == 0 and memo[i - 1][j] == 0):
        memo[i][j] = 0
        continue
      if i == 0 or j == 0:
        continue
      memo[i][j] = (memo[i - 1][j] + memo[i][j - 1]) % MOD

  return memo[-1][-1]

def blocked_spot(grid, i, j):
  return grid[i][j] == 1