# Dynamic Programming version
def minimum_total(triangle):
  for i in range(len(triangle) - 2, -1, -1):
    for j in range(0, len(triangle[i])):
      triangle[i][j] = min(
        triangle[i][j] + triangle[i + 1][j],
        triangle[i][j] + triangle[i + 1][j + 1]
      )

  return triangle[0][0]

# Recursive version
def minimum_total2(triangle, row_index = 0, col_index = 0):
  if len(triangle) - 1 == row_index:
    return triangle[row_index][col_index]

  return min(
    triangle[row_index][col_index] + minimum_total2(triangle, row_index + 1, col_index),
    triangle[row_index][col_index] + minimum_total2(triangle, row_index + 1, col_index + 1),
  )

# Memoized recursive version
def minimum_total3(triangle):
  return recurse_triangle(triangle, 0, 0, saved = {})

def recurse_triangle(triangle, row_index, col_index, saved):
  lookup = (row_index, col_index)
  if lookup not in saved:
    if len(triangle) - 1 == row_index:
      saved[lookup] =  triangle[row_index][col_index]
    else:
      saved[lookup] = min(
        triangle[row_index][col_index] + recurse_triangle(triangle, row_index + 1, col_index, saved),
        triangle[row_index][col_index] + recurse_triangle(triangle, row_index + 1, col_index + 1, saved),
      )
  return saved[lookup]
