n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [False for _ in range(n+1)]
ans = 0

def dfs(node):
    visited[node] = True
    # ans += 1
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)

dfs(1)
print(len([x for x in visited if x != False])-1)