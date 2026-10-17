print(" *** Graph Traversal ***")
inp = input("Enter : ")

graph = {}

for edge in inp.split(","):
    a, b = edge.split()
    graph.setdefault(a, set()).add(b)
    graph.setdefault(b, set()).add(a)

vertices = sorted(graph)

visited = set()
depth = []

for start in vertices:
    stack = [start]

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        depth.append(node)
        stack.extend(sorted(graph[node], reverse=True))

visited = set()
breadth = []

for start in vertices:
    if start in visited:
        continue

    queue = [start]
    visited.add(start)
    front = 0

    while front < len(queue):
        node = queue[front]
        front += 1
        breadth.append(node)

        for neighbor in sorted(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("Depth First Traversals : " + " ".join(depth))
print("Bredth First Traversals : " + " ".join(breadth))
print("===== End of program =====")