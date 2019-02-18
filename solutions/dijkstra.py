from queue import PriorityQueue

def network_delay_time(times, N, K):
  graph = {}
  for start, target, time in times:
    graph[start] = {} if start not in graph else graph[start]
    graph[target] = {} if target not in graph else graph[target]
    graph[start][target] = time
    graph[target][start] = time

  distances = {}
  for value in graph:
    distances[value] = float("inf")
  distances[K] = 0

  queue_lookup = {}
  priority_queue = PriorityQueue()
  for value, neighbors in graph.items():
    bucket = (value, neighbors)
    priority_queue.put(bucket, distances[value])
    queue_lookup[value] = bucket

  while not priority_queue.empty():
    value, neighbors = priority_queue.get()

    for neighbor_value, distance in neighbors.items():
      new_distance = distances[neighbor_value] + distance
      if new_distance < distances[value]:
        distances[value] = new_distance

  maximum = max(distances.values())
  return maximum if maximum < float("inf") else -1
