# Time Complexity: O(n log n)
# Space Complexity: O(1)
def is_pangram_1(text):
  if len(text) < 26:
    return False

  chars = list(text)
  chars.sort()
  start_index = 97
  end_index = start_index + 25
  final_char = "z"

  current_index = start_index
  next_index = start_index + 1

  for char in chars:
    if char == chr(current_index):
      continue
    elif char == final_char:
      return True
    elif char == chr(next_index):
      current_index += 1
      next_index += 1
    else:
      return False

  return current_index == end_index
