def shortest_path(graph, start, target):
    if start not in graph or target not in graph:
        return None

    distances = {node: float("inf") for node in graph}
    previous = {}
    visited = set()
    distances[start] = 0

    while True:
        current = None
        smallest = float("inf")

        for node in sorted(graph):
            if node not in visited and distances[node] < smallest:
                smallest = distances[node]
                current = node

        if current is None:
            return None

        if current == target:
            path = []

            while current is not None:
                path.append(current)
                current = previous.get(current)

            return path[::-1]

        visited.add(current)

        for neighbor, weight in graph[current]:
            new_distance = distances[current] + weight

            if neighbor not in visited and new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current


print(" *** Shortest Path (Dijkstra's Algorithm) ***")
edges, queries = input("Enter : ").split("/")

graph = {}

for edge in edges.split(","):
    source, weight, destination = edge.split()
    graph.setdefault(source, []).append((destination, int(weight)))
    graph.setdefault(destination, [])

for query in queries.split(","):
    start, target = query.split()
    path = shortest_path(graph, start, target)

    if path is None:
        print(f"Not have path : {start} to {target}")
    else:
        print(f"{start} to {target} : " + "->".join(path))