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
