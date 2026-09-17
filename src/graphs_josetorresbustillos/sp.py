"""Dijkstra's shortest path algorithm supplied with the assignment."""

import sys

from .heapq import heappop, heappush


def dijkstra(graph, source):
    """Return distances and predecessor paths for a nonnegative graph.

    Include every vertex as a key, including sinks with empty dictionaries.
    The source must exist in the graph. Paths exclude their destination;
    unreachable vertices have distance sys.maxsize and no path entry.
    """
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
