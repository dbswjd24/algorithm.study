//https://www.acmicpc.net/problem/2309

heights = [int(input()) for _ in range(9)]
total = sum(heights)
found = False

for i in range(9):
    for j in range(i + 1, 9):
        if total - (heights[i] + heights[j]) == 100:
            exclude1, exclude2 = heights[i], heights[j]
            found = True
            break
    if found:
        break

heights.remove(exclude1)
heights.remove(exclude2)
heights.sort()

for h in heights:
    print(h)
