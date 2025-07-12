N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

max_len = 1  # 최소 정사각형 넓이는 1

for i in range(N):
    for j in range(M):
        for size in range(1, min(N - i, M - j)):
            # 네 꼭짓점
            if board[i][j] == board[i][j + size] == board[i + size][j] == board[i + size][j + size]:
                max_len = max(max_len, size + 1)

print(max_len * max_len)