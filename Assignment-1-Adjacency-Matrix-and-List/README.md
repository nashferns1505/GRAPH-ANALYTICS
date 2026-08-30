# Adjacency Matrix and Adjacency List Representation of a Graph

---

## A. Title of the Problem

Adjacency Matrix and Adjacency List Representation of a Graph

---

## B. Problem Statement

Write a Python program to represent the same graph using both an adjacency matrix and an adjacency list.

Accept vertices and edges from the user, construct both representations, display them, calculate the storage requirement for each, and identify which representation is more suitable for a sparse graph.

---

## C. HackerRank / LeetCode Link

N/A

---

## D. GitHub Repository

[nashferns1505/GRAPH-ANALYTICS](https://github.com/nashferns1505/GRAPH-ANALYTICS)

---

## E. Solution Steps / Algorithm

1. Read the number of vertices and edges.
2. Create an adjacency matrix initialized with zeros.
3. Create an empty adjacency list.
4. Read each edge and update both graph representations.
5. Display the adjacency matrix.
6. Display the adjacency list.
7. Calculate matrix storage = `V²` and list storage = `V + 2E`.
8. Compare both values and print the better representation for a sparse graph.

---

## F. Code Developed

```python
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
```

---

## G. HackerRank Test Case Passed Screenshot / Output Screenshot

Find it in the following file:

`screenshot.png`

---

## H. Observation

The adjacency list is more suitable for sparse graphs because it uses less memory than an adjacency matrix.

The program successfully constructs both representations, displays them correctly, and compares their storage requirements.
