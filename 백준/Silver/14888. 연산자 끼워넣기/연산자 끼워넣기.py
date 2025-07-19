N = int(input())
A = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_val = -int(1e9)
min_val = int(1e9)

def dfs(idx, total, add, sub, mul, div):
    global max_val, min_val
    if idx == N:
        max_val = max(max_val, total)
        min_val = min(min_val, total)
        return
    if add:
        dfs(idx + 1, total + A[idx], add - 1, sub, mul, div)
    if sub:
        dfs(idx + 1, total - A[idx], add, sub - 1, mul, div)
    if mul:
        dfs(idx + 1, total * A[idx], add, sub, mul - 1, div)
    if div:
        if total < 0:
            dfs(idx + 1, -(-total // A[idx]), add, sub, mul, div - 1)
        else:
            dfs(idx + 1, total // A[idx], add, sub, mul, div - 1)

dfs(1, A[0], *ops)
print(max_val)
print(min_val)