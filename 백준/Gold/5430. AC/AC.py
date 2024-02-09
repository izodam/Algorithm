from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())

    arr = input().rstrip()[1:-1].split(',')

    arr = deque(arr)
    flag = 0

    for i in p:
        if i == 'R':
            flag += 1
        else:
            if n == 0:
                print('error')
                break
            elif arr:
                if flag % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print('error')
                break
    else:
        if flag % 2 != 0:
            arr.reverse()
        print('[{0}]'.format(','.join(map(str,arr))))