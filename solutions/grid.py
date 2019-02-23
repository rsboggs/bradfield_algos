# h, w place trying to reach on grid
# top left of grid is 1,1
# move only down & to right
def number_paths(h, w, grid):
  memo = [[1] * w for _ in range(0, h)]
  for i, row, in enumerate(memo):
    for j, _ in enumerate(row):
      if i == 0 or j == 0:
        continue
      first_prior = 0 if blocked_spot(grid, i - 1, j) else memo[i - 1][j]
      second_prior = 0 if blocked_spot(grid, i, j - 1) else memo[i][j - 1]
      memo[i][j] = first_prior + second_prior
  return memo[-1][-1]

def blocked_spot(grid, i, j):
  return grid[i][j] == 1