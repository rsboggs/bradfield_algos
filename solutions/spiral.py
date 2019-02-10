# Input n (n is size of each array)
# Output 2D array (matrix)
# Fill out array with spiral pattern
# incrementing from 1 in top left > top right -> bottom right -> top left -> etc
import pdb

def create_spiral_matrix(n):
  # 0 is right, 1 is down, etc
  current_direction = 0
  counter = 1
  row_index = 0
  col_index = 0
  row_indexes = [0, 1, 0, -1]
  col_indexes = [1, 0, -1, 0]

  matrix = [[0 for x in range(n)] for y in range(n)]

  matrix[row_index][col_index] = counter
  counter += 1

  while counter < n * n + 1:
    proposed_col_index = col_index + col_indexes[current_direction]
    proposed_row_index = row_index + row_indexes[current_direction]

    if empty_valid_spot(matrix, proposed_row_index, proposed_col_index):
      col_index = proposed_col_index
      row_index = proposed_row_index
    else:
      current_direction = (current_direction + 1) % 4
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