from collections import deque

n = int(input())
moves = [0] + list(int(input()) for _ in range(n))
visited = [0] * (n+1)
safe_count = 0

def dfs(node):
    if visited[node] == 1:
        return False
    if visited[node] == 2:
        return True
    visited[node] = 1
    next_node = moves[node]

    if next_node != 0 and not dfs(next_node):
        return False
    
    visited[node] = 2
    return True


for i in range(1, n+1):
    if visited[i] != True:
        if dfs(i):
            safe_count += 1

print(safe_count)