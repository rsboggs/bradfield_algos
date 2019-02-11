def is_present(alist, item, start_index = 0, end_index = None):
  if not alist:
    return False

  if end_index == None:
    end_index = len(alist) - 1

  midpoint = (end_index + start_index) // 2
  if alist[midpoint] == item:
    return True

  if item < alist[midpoint]:
    if start_index == midpoint:
      return False
    return is_present(alist, item, start_index, midpoint - 1)

  if end_index == midpoint:
    return False
  return is_present(alist, item, midpoint + 1, end_index)
