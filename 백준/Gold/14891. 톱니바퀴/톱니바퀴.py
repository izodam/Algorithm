import sys
input = sys.stdin.readline

# 14891. 톱니바퀴

# 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전
# 점수
# 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
# 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
# 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
# 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
from collections import deque

# 회전해야하는 톱니바퀴 찾기
def find_numbers(n, direction):
    # 오른쪽 톱니바퀴 체크 -> n의 index 2와 n+1의 index 6이 맞닿음
    if 0 <= n + 1 < 4 and n + 1 not in rotate_number:
        if wheel[n][2] != wheel[n+1][6]:
            check.append((n+1, direction*(-1)))
            rotate_number.append(n+1)
            find_numbers(n+1, direction*(-1))

    # 왼쪽 톱니바퀴 체크 -> n의 index 6와 n-1의 index 2이 맞닿음
    if 0 <= n-1 < 4 and n - 1 not in rotate_number:
        if wheel[n][6] != wheel[n-1][2]:
            check.append((n-1, direction*(-1)))
            rotate_number.append(n-1)
            find_numbers(n-1, direction*(-1))

def turn():
    for n, direction in check:
        wheel[n].rotate(direction)



# N극은 0, S극은 1
# 12시방향부터 시계방향 순서대로
wheel = [deque(list(input().strip())) for _ in range(4)]

# 회전 횟수
k = int(input())

score = 0

# 회전 방법
# 톱니바퀴 번호, 방향 (1 : 시계, -1 : 반시계)
for _ in range(k):
    n, direction = map(int, input().split())
    n -= 1

    check = [(n, direction)]
    # 회전시킬 톱니바퀴의 번호
    rotate_number = [n]

    find_numbers(n, direction)
    turn()

for i in range(4):
    score += int(wheel[i][0]) * (2 ** i)

print(score)

