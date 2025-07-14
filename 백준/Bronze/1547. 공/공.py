M = int(input())
ball = 1  # 공은 처음에 1번 컵 아래

for _ in range(M):
    X, Y = map(int, input().split())
    if ball == X:
        ball = Y
    elif ball == Y:
        ball = X
    # else: 공은 다른 데 있으므로 그대로

print(ball)