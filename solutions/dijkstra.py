import heapq
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

  priority_queue = []
  entries = {}
  for node_source, neighbors in graph.items():
    bucket = [distances[node_source], node_source]
    heapq.heappush(priority_queue, bucket)
    entries[node_source] = bucket

  while len(priority_queue) > 0:
    _queue_distance, node_source = heapq.heappop(priority_queue)
    neighbors = graph[node_source]

    for neighbor_value, distance in neighbors.items():
      if node_source == K and distances[neighbor_value] > distance:
        distances[neighbor_value] = distance
        if neighbor_value in entries:
          entries[neighbor_value][0] = distance
      elif distances[node_source] != float("inf") and distances[neighbor_value] > distances[node_source] + distance:
        distances[neighbor_value] = distances[node_source] + distance
        if neighbor_value in entries:
          entries[neighbor_value][0] = distances[node_source] + distance

  values = distances.values()
  if len(values) != N:
    return -1
  maximum = max(values)
  return maximum if maximum < float("inf") else -1

