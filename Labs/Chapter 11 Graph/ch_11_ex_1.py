print(" *** Directed Graph Adjacency Matrix ***")
inp = input("Enter : ")

edges = [edge.split() for edge in inp.split(",")]
vertices = sorted({vertex for edge in edges for vertex in edge})
connections = {(start, end) for start, end in edges}

print("    " + "  ".join(vertices))

for start in vertices:
    row = ["1" if (start, end) in connections else "0"
           for end in vertices]
    print(start + " : " + ", ".join(row))

print("===== End of program ======")