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
    elif ord(char) < start_index or ord(char) > end_index:
      pass
    else:
      return False

  return current_index == end_index

# Time Complexity: O(n)
# Space Complexity: O(n)
def is_pangram_2(text):
  if len(text) < 26:
    return False

  chars = [0] * 26
  for char in text:
    char_int = ord(char) - 97
    if char_int < 0 or char_int > 25:
      pass
    else:
      chars[char_int] += 1

  return all(chars)
