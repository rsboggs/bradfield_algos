# Dynamic Programming version
def minimum_total(triangle):
  for i in range(len(triangle) - 2, -1, -1):
    for j in range(0, len(triangle[i])):
      triangle[i][j] = min(
        triangle[i][j] + triangle[i + 1][j],
        triangle[i][j] + triangle[i + 1][j + 1]
      )

  return triangle[0][0]
