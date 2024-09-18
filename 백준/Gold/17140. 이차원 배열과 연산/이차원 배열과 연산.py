import sys
input = sys.stdin.readline

# 행의 개수 ≥ 열의 개수인 경우 모든 행에 대해 정렬 - R연산
# 행의 개수 < 열의 개수인 경우 모든 열에 대해 정렬 - C연산
# 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬
# 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저

def cal_sort(board):
    new_board = []
    max_length = 0
    for row in board:
        row_dict = dict()
        for i in row:
            if i == 0:
                continue
            if i in row_dict:
                row_dict[i] += 1
            else:
                row_dict[i] = 1
        sorted_row = sorted(row_dict.items(), key=lambda x: (x[1], x[0]))
        new_row = []
        for x, y in sorted_row:
            new_row.append(x)
            new_row.append(y)
        new_board.append(new_row)
        max_length = max(max_length, len(new_row))

    for row in range(len(new_board)):
        if len(new_board[row]) != max_length:
            new_board[row] += [0] * (max_length - len(new_board[row]))
        if len(new_board[row]) > 100:
            new_board[row] = new_board[row][:100]

    return new_board


r, c, k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(3)]
cnt = 0

while True:
    # print(board)
    if len(board) > r-1 and len(board[0]) > c-1 and board[r-1][c-1] == k:
        print(cnt)
        break

    if cnt > 100:
        print(-1)
        break

    # R 연산
    if len(board) >= len(board[0]):
        new_board = cal_sort(board)
        board = [i.copy() for i in new_board]

    # C 연산
    else:
        now_board = list(zip(*board))
        new_board = cal_sort(now_board)
        new_board = list(zip(*new_board))
        board = [list(i) for i in new_board]

    cnt += 1