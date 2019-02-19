from queue import PriorityQueue
from collections import defaultdict

def network_delay_time(times, N, K):
  graph = defaultdict(dict)
  uniq_values = set()

  for start, target, time in times:
    graph[start][target] = time
    uniq_values.add(start)
    uniq_values.add(target)

  distances = {}
  for value in uniq_values:
    distances[value] = float("inf")
  distances[K] = 0

  priority_queue = PriorityQueue()
  for node_source, neighbors in graph.items():
    bucket = (node_source, neighbors)
    priority_queue.put(bucket, distances[node_source])

  while not priority_queue.empty():
    node_source, neighbors = priority_queue.get()

    for neighbor_value, distance in neighbors.items():
      if node_source == K:
        distances[neighbor_value] = distance
      elif distances[node_source] != float("inf") and distances[neighbor_value] > distances[node_source] + distance:
        distances[neighbor_value] = distances[node_source] + distance

  maximum = max(distances.values())
  return maximum if maximum < float("inf") else -1

