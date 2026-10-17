def find(parent, node):
    while parent[node] != node:
        parent[node] = parent[parent[node]]
        node = parent[node]
    return node


def has_cycle(edges):
    parent = {}

    for source, destination in edges:
        parent.setdefault(source, source)
        parent.setdefault(destination, destination)

        root_source = find(parent, source)
        root_destination = find(parent, destination)

        if root_source == root_destination:
            return True

        parent[root_source] = root_destination

    return False


inp = input("Enter : ")
edges = [edge.split() for edge in inp.split(",")]

if has_cycle(edges):
    print("Graph has a cycle")
else:
    print("Graph has no cycle")