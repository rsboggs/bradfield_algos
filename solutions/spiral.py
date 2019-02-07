# Input n (n is size of each array)
# Output 2D array (matrix)
# Fill out array with spiral pattern
# incrementing from 1 in top left > top right -> bottom right -> top left -> etc
import pdb

def create_spiral_matrix(n):
  current_direction = "right"
  counter = 1
  row_index = 0
  col_index = 0

  matrix = [[0 for x in range(n)] for y in range(n)]

  matrix[row_index][col_index] = counter
  counter += 1

  while counter < n * n + 1:
    if current_direction == "right":
      if empty_valid_spot(matrix, row_index, col_index + 1):
        col_index += 1
      else:
        current_direction = "down"
        continue
    elif current_direction == "down":
      if empty_valid_spot(matrix, row_index + 1, col_index):
        row_index += 1
      else:
        current_direction = "left"
        continue
    elif current_direction == "left":
      if empty_valid_spot(matrix, row_index, col_index - 1):
        col_index -= 1
      else:
        current_direction = "up"
        continue
    elif current_direction == "up":
      if empty_valid_spot(matrix, row_index - 1, col_index):
        row_index -= 1
      else:
        current_direction = "right"
        continue

    matrix[row_index][col_index] = counter
    counter += 1

  return matrix

def empty_valid_spot(matrix, row_index, col_index):
  if row_index == len(matrix) or col_index == len(matrix):
    return False
  if row_index < 0 or col_index < 0:
    return False
  if matrix[row_index][col_index] != 0:
    return False
  return True