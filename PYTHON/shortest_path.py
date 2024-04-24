#!/usr/bin/env python3
"""Find the shortest path in a graph"""


def shortest_path(graph, start):
    """Finds the shortest path in a graph from a starting node
    """
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)

    while unvisited:
        # current = min(unvisited, key=distances.get)
        current = min(unvisited, key=lambda node: distances[node])
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current]

                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)

    print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')


if __name__ == '__main__':
    my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
    }
    shortest_path(my_graph, 'A')
