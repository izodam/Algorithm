T = int(input())
for _ in range(T):
    yeon = 0
    korea = 0
    for _ in range(9):
        y, k = map(int,input().split())
        yeon += y
        korea += k
    if yeon > korea:
        print('Yonsei')
    elif yeon < korea:
        print('Korea')
    else:
        print('Draw')