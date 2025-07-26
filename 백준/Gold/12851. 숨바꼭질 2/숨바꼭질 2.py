from collections import deque

def hide_and_seek(n, k):
    MAX = 100001
    visited = [-1] * MAX
    count = [0] * MAX

    queue = deque()
    queue.append(n)
    visited[n] = 0
    count[n] = 1

    while queue:
        current = queue.popleft()

        for next_pos in [current - 1, current + 1, current * 2]:
            if 0 <= next_pos < MAX:
                if visited[next_pos] == -1:  # 처음 방문
                    visited[next_pos] = visited[current] + 1
                    count[next_pos] = count[current]
                    queue.append(next_pos)
                elif visited[next_pos] == visited[current] + 1:  # 같은 시간에 다시 방문
                    count[next_pos] += count[current]

    print(visited[k])
    print(count[k])

# 예제 입력
n, k = map(int, input().split())
hide_and_seek(n, k)