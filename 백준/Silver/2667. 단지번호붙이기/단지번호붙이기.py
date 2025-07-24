import sys
sys.setrecursionlimit(10000)

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    count = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                count += dfs(nx, ny)
    return count

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(dfs(i, j))

result.sort()
print(len(result))
for r in result:
    print(r)
