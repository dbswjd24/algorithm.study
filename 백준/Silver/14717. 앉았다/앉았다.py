def get_score(x, y):
    if x == y:
        return 190 + x
    else:
        return 100 + (x + y) % 10

cards = [i for i in range(1, 11)] * 2
A, B = map(int, input().split())

if A == B:
    cards.remove(A)
    cards.remove(A)  # 같은 카드이므로 두 번 제거
else:
    cards.remove(A)
    cards.remove(B)

my_score = get_score(A, B)
win = 0
total = 0

n = len(cards)
for i in range(n):
    for j in range(i+1, n):
        c1, c2 = cards[i], cards[j]
        opp_score = get_score(c1, c2)
        if my_score > opp_score:
            win += 1
        total += 1

prob = win / total
prob = int(prob * 1000 + 0.5) / 1000  # 반올림

print(f"{prob:.3f}")
