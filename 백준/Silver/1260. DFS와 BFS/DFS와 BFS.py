from collections import deque

def dfs(v, visited, graph, result):
    visited[v] = True
    result.append(v)
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph, result)

def bfs(start, graph):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    result = []

    while queue:
        v = queue.popleft()
        result.append(v)
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return result

# 입력 처리
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 인접 리스트 정렬
for g in graph:
    g.sort()

# DFS 실행
visited = [False] * (n + 1)
dfs_result = []
dfs(v, visited, graph, dfs_result)
print(' '.join(map(str, dfs_result)))

# BFS 실행
bfs_result = bfs(v, graph)
print(' '.join(map(str, bfs_result)))
