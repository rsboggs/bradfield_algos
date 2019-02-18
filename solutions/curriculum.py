def is_possible_curriculum(remaining_classes, enrolled_classes = {}):
  if len(remaining_classes) == 0:
    return True

  for klass in remaining_classes:
    for prereq in klass["prereqs"]:
      if prereq not in enrolled_classes:
        return False

    class_title = klass["title"]
    enrolled_classes[class_title] = True

    new_remaining_classes = list(remaining_classes)
    new_remaining_classes.remove(klass)

    is_possible = is_possible_curriculum(new_remaining_classes, enrolled_classes)
    if is_possible == True:
      return True

    # Undo work on this path so don't pollute other recursive paths
    del enrolled_classes[class_title]
