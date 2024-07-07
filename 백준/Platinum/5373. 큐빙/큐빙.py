import sys
input = sys.stdin.readline

# 5373. 큐빙

# 큐브 회전시 기준면 회전됨
def turn(i):
    # 각 변의 꼭짓점 이동
    temp = cube[i][0][0]
    cube[i][0][0] = cube[i][2][0]
    cube[i][2][0] = cube[i][2][2]
    cube[i][2][2] = cube[i][0][2]
    cube[i][0][2] = temp

    # 각 변의 가운데 점 이동
    temp = cube[i][0][1]
    cube[i][0][1] = cube[i][1][0]
    cube[i][1][0] = cube[i][2][1]
    cube[i][2][1] = cube[i][1][2]
    cube[i][1][2] = temp


def move(side, direction):
    if direction == '+':
        if side == 'U':
             turn(0)
             temp = cube[2][0]
             cube[2][0] = cube[5][0]
             cube[5][0] = cube[3][0]
             cube[3][0] = cube[4][0]
             cube[4][0] = temp
    
        elif side == 'D':
            turn(1)
            temp = cube[2][2]
            cube[2][2] = cube[4][2]
            cube[4][2] = cube[3][2]
            cube[3][2] = cube[5][2]
            cube[5][2] = temp
    
        elif side == 'F':
            turn(2)
            temp = cube[0][2]
            cube[0][2] = [cube[4][2][2], cube[4][1][2], cube[4][0][2]]
            cube[4][2][2], cube[4][1][2], cube[4][0][2] = cube[1][0][2], cube[1][0][1], cube[1][0][0]
            cube[1][0][2], cube[1][0][1], cube[1][0][0] = cube[5][0][0], cube[5][1][0], cube[5][2][0]
            cube[5][0][0], cube[5][1][0], cube[5][2][0] = temp[0], temp[1], temp[2]
    
        elif side == 'B':
            turn(3)
            temp = cube[0][0]
            cube[0][0] = [cube[5][0][2], cube[5][1][2], cube[5][2][2]]
            cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[1][2][2], cube[1][2][1], cube[1][2][0]
            cube[1][2][2], cube[1][2][1], cube[1][2][0] = cube[4][2][0], cube[4][1][0], cube[4][0][0]
            cube[4][2][0], cube[4][1][0], cube[4][0][0] = temp[0], temp[1], temp[2]
    
        elif side == 'L':
            turn(4)
            temp = [cube[2][0][0], cube[2][1][0], cube[2][2][0]]
            cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[0][0][0], cube[0][1][0], cube[0][2][0]
            cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[3][2][2], cube[3][1][2], cube[3][0][2]
            cube[3][2][2], cube[3][1][2], cube[3][0][2] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
            cube[1][0][0], cube[1][1][0], cube[1][2][0] = temp[0], temp[1], temp[2]

    
        elif side == 'R':
            turn(5)
            temp = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
            cube[0][0][2], cube[0][1][2], cube[0][2][2] = [cube[2][0][2], cube[2][1][2], cube[2][2][2]]
            cube[2][0][2], cube[2][1][2], cube[2][2][2] = [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
            cube[1][0][2], cube[1][1][2], cube[1][2][2] = [cube[3][2][0], cube[3][1][0], cube[3][0][0]]
            cube[3][2][0], cube[3][1][0], cube[3][0][0] = [temp[0], temp[1], temp[2]]

    else:
        # 반시계는 시계 3번 돌린것!
        move(side, '+')
        move(side, '+')
        move(side, '+')


# 윗 면은 흰색, 아랫 면은 노란색, 앞 면은 빨간색, 뒷 면은 오렌지색, 왼쪽 면은 초록색, 오른쪽 면은 파란색
tc = int(input())
for t in range(tc):
    n = int(input())

    cube = []
    for c in ['w', 'y', 'r', 'o', 'g', 'b']:
        cube.append([[c] * 3 for _ in range(3)])

    # 돌린면, 돌린 방향
    # U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면
    # +인 경우에는 시계 방향 (그 면을 바라봤을 때가 기준), -인 경우에는 반시계 방향
    command_move = list(input().strip().split())

    for command in command_move:
        side, direction = command[0], command[1]
        move(side, direction)

    for line in cube[0]:
        print(''.join(line))
