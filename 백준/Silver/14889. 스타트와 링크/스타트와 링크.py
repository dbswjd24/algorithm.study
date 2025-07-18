from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
people = list(range(N))
min_diff = float('inf')

for start in combinations(people, N // 2):
    link = [p for p in people if p not in start]

    start_score = 0
    link_score = 0

    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            start_score += S[start[i]][start[j]] + S[start[j]][start[i]]
            link_score += S[link[i]][link[j]] + S[link[j]][link[i]]

    diff = abs(start_score - link_score)
    min_diff = min(min_diff, diff)

    if min_diff == 0:
        break

print(min_diff)