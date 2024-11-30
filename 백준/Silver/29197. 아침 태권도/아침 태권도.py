import sys
input = sys.stdin.readline

# 입력
N = int(input())

quad1 = set()
quad2 = set()
quad3 = set()
quad4 = set()
axis = set()

for _ in range(N):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        quad1.add(y/x)
    elif x < 0 and y > 0:
        quad2.add(y/x)
    elif x < 0 and y < 0:
        quad3.add(y/x)
    elif x > 0 and y < 0:
        quad4.add(y/x)
        
    elif x == 0 and y > 0:
        axis.add('y')
    elif x == 0 and y < 0:
        axis.add('-y')
    elif y == 0 and x > 0:
        axis.add('x')
    elif y == 0 and x < 0:
        axis.add('-x')

res = len(quad1) + len(quad2) + len(quad3) + len(quad4) + len(axis)
print(res)