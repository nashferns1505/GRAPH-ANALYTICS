n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

matrix = [[0] * n for _ in range(n)]
adj_list = [[] for _ in range(n)]

print("Enter edges (source destination):")

for _ in range(e):
    u, v = map(int, input().split())

    matrix[u][v] = 1
    matrix[v][u] = 1

    adj_list[u].append(v)
    adj_list[v].append(u)

print("\nAdjacency Matrix:")
for row in matrix:
    print(*row)

print("\nAdjacency List:")
for i in range(n):
    print(i, "->", adj_list[i])

matrix_storage = n * n
list_storage = n + 2 * e

print("\nStorage Requirement:")
print("Adjacency Matrix:", matrix_storage, "entries")
print("Adjacency List:", list_storage, "entries")

if list_storage < matrix_storage:
    print("Adjacency List is more suitable for a sparse graph.")
else:
    print("Adjacency Matrix uses fewer entries for this graph.")
