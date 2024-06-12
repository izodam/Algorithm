# 14499. 주사위 굴리기


# def turn_dice(command):
#     # 동
#     if command == 1:
#         dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
#     # 서
#     elif command == 2:
#         dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
#     # 북
#     elif command == 3:
#         dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
#     # 남
#     elif command == 4:
#         dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]


def turn_dice(move):
    if move == 1:  # 동쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[
            2]  # 주사위 변화 4 2 1 6 5 3
    elif move == 2:  # 서쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[
            3]  # 주사위 변화 3 2 6 1 5 4
    elif move == 3:  # 북쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[
            1]  # 주사위 변화 5 1 3 4 6 2
    elif move == 4:  # 남쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]


n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
commands = list(map(int, input().split()))

dice = [0] * 6
delta = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]

for command in commands:
    if 0 <= x + delta[command][0] < n and 0 <= y + delta[command][1] < m:
        x += delta[command][0]
        y += delta[command][1]
        turn_dice(command)
        if board[x][y] == 0:
            board[x][y] = dice[5]
        else:
            dice[5] = board[x][y]
            board[x][y] = 0

        print(dice[0])
