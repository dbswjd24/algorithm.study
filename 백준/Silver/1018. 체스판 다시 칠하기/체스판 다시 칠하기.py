N, M = map(int, input().split())
board = [input() for _ in range(N)]

min_paint = 64  # 최대 8*8=64

for i in range(N - 7):
    for j in range(M - 7):
        count_w = 0  # (i,j)를 W로 시작
        count_b = 0  # (i,j)를 B로 시작
        for x in range(8):
            for y in range(8):
                current = board[i + x][j + y]
                # 체스판 패턴에 따른 기대 색
                if (x + y) % 2 == 0:
                    if current != 'W':
                        count_w += 1
                    if current != 'B':
                        count_b += 1
                else:
                    if current != 'B':
                        count_w += 1
                    if current != 'W':
                        count_b += 1
        min_paint = min(min_paint, count_w, count_b)

print(min_paint)