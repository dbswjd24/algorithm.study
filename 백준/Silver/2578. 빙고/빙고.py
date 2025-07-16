board = [list(map(int, input().split())) for _ in range(5)]
calls = [num for _ in range(5) for num in map(int, input().split())]

def count_bingo(board):
    bingo = 0

    # 가로
    for row in board:
        if all(x == 0 for x in row):
            bingo += 1

    # 세로
    for col in range(5):
        if all(board[row][col] == 0 for row in range(5)):
            bingo += 1

    # 대각선
    if all(board[i][i] == 0 for i in range(5)):
        bingo += 1
    if all(board[i][4 - i] == 0 for i in range(5)):
        bingo += 1

    return bingo

# 사회자가 숫자를 부르기 시작
for idx, number in enumerate(calls):
    # 철수의 보드에서 number를 찾아 0으로 바꾸기
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                board[i][j] = 0

    # 빙고 줄 개수 세기
    if count_bingo(board) >= 3:
        print(idx + 1)
        break