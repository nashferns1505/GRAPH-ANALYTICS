# Even Forest - Maximum Number of Removable Edges

---

## A. Title of the Problem

Even Forest - Maximum Number of Removable Edges

---

## B. Problem Statement

Given a tree, remove the maximum number of edges such that every resulting connected component contains an even number of nodes.

The tree is rooted at node `1`.

The number of nodes `n` is even and satisfies:

`2 ≤ n ≤ 100`

The objective is to determine the maximum number of edges that can be removed while ensuring that every resulting subtree has an even number of nodes.

---

## C. HackerRank / LeetCode Link

[HackerRank – Even Tree](https://www.hackerrank.com/challenges/even-tree/problem?utm_source=chatgpt.com)

---

## D. GitHub Repository

[nashferns1505/GRAPH-ANALYTICS](https://github.com/nashferns1505/GRAPH-ANALYTICS)

---

## E. Solution Steps / Algorithm

1. Read the number of nodes and edges.
2. Create an undirected adjacency list for the tree.
3. Start DFS traversal from node `1`.
4. Calculate the size of each subtree.
5. If a child subtree contains an even number of nodes, remove the edge connecting it to its parent.
6. Increment the count of removable edges.
7. If the subtree size is odd, add its size to the parent subtree.
8. Continue until all nodes are visited.
9. Return the total number of removable edges.

---

## F. Code Developed

```python
def evenForest(t_nodes, t_edges, t_from, t_to):
    graph = [[] for _ in range(t_nodes + 1)]

    for i in range(t_edges):
        u = t_from[i]
        v = t_to[i]
        graph[u].append(v)
        graph[v].append(u)

    answer = 0

    def dfs(node, parent):
        nonlocal answer
        size = 1

        for child in graph[node]:
            if child != parent:
                child_size = dfs(child, node)

                if child_size % 2 == 0:
                    answer += 1
                else:
                    size += child_size

        return size

    dfs(1, 0)
    return answer


n, e = map(int, input().split())

t_from = []
t_to = []

for _ in range(e):
    u, v = map(int, input().split())
    t_from.append(u)
    t_to.append(v)

print(evenForest(n, e, t_from, t_to))
```

---

## G. HackerRank Test Case Passed Screenshot / Output Screenshot

Find it in the following file:

`screenshot2.png`

---

## H. Observation

The program successfully finds the maximum number of edges that can be removed while ensuring that every resulting component contains an even number of nodes.

For the given test case, the output is:

`2`

The algorithm uses Depth First Search to calculate subtree sizes efficiently.

Time Complexity: `O(V + E)`

Space Complexity: `O(V + E)`
