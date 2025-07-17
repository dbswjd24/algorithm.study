N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 2)

for i in range(1, N + 1):
    # 이전 날까지 최대 수익 carry
    dp[i] = max(dp[i], dp[i - 1])
    # 상담이 가능한 경우
    if i + T[i - 1] <= N + 1:
        dp[i + T[i - 1]] = max(dp[i + T[i - 1]], dp[i] + P[i - 1])

# 마지막 날까지의 최대 수익 출력
print(max(dp))