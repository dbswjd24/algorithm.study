from collections import deque

def bfs(N, K):
    visited = [0] * 100001
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()
        if x == K:
            return visited[x]
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= 100000 and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                queue.append(nx)

# 입력 처리
N, K = map(int, input().split())
print(bfs(N, K))
