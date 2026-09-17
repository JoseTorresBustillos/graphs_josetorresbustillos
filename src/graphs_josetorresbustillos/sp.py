"""Shortest paths and breadth-first graph traversal."""

import sys
from collections import deque

from .heapq import heappop, heappush


def dijkstra(graph, source):
    dist = {node: sys.maxsize for node in graph}
    dist[source] = 0
    heap = []
    heappush(heap, (0, source))
    path = {source: []}

    while heap:
        w, u = heappop(heap)
        for v in graph[u]:
            if w + graph[u][v] < dist[v]:
                dist[v] = w + graph[u][v]
                heappush(heap, (dist[v], v))
                path[v] = path[u] + [u]

    return dist, path


def bfs(graph, source):
    """Return reachable vertices in breadth-first order from source.

    Accept an adjacency dictionary in the same format as dijkstra.
    Edge weights are ignored, and neighbors are visited in dictionary
    insertion order. Destinations missing as keys are treated as sinks.
    Raise ValueError if source is not a key in graph.

    Each vertex is visited once, including in graphs with cycles. Time
    complexity is O(V + E), with O(V) extra space for reachable vertices.
    """
    if source not in graph:
        raise ValueError("source must be a vertex in graph")

    visited = {source}
    queue = deque([source])
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph.get(vertex, {}):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order
