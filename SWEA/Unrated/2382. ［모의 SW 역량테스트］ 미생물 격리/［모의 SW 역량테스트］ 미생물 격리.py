# (상: 1, 하: 2, 좌: 3, 우: 4)
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

T = int(input())
for tc in range(1, T+1):
    # 테두리 약품 칠해져 있음
    # 약품 칠해진 셀 도착시 절반 죽고 이동방향 반대
    # 홀수이면 소수점 버림 (1마리면 0마리 되므로 사라짐)
    # 한 셀에 모이면 합쳐짐 -> 이동방향은 미생물 수가 많은 군집의 이동방향
    # m시간 후 남아있는 미생물 합 구하기
    n, m, k = map(int,input().split())

    # 세로 위치, 가로 위치, 미생물 수, 이동 방향
    micro = [list(map(int,input().split())) for _ in range(k)]

    while m > 0:
        # 이동
        for i in range(len(micro)):
            micro[i][0] += delta[micro[i][3]-1][0]
            micro[i][1] += delta[micro[i][3]-1][1]
            # 약물이면 방향 뒤집고 미생물 반으로 줄이기
            if micro[i][0] == 0 or micro[i][0] == n-1 or micro[i][1] == 0 or micro[i][1] == n-1:
                micro[i][2] //= 2
                if micro[i][3] % 2 == 0:
                    micro[i][3] -= 1
                else:
                    micro[i][3] += 1

        location = {}
        # 겹치는 애들 찾기
        for i in micro:
            if (i[0], i[1]) in location:
                location[(i[0], i[1])].append(i)
            else:
                location[(i[0], i[1])] = [i]
        # print(location)
        micro = []
        for l in location:
            # 해당 위치에 2개 이상 있으면 합치기
            if len(location[l]) >= 2:
                number = 0
                direction = 0
                max_number = 0
                for each in location[l]:
                    if each[2] > max_number:
                        max_number = each[2]
                        direction = each[3]
                    number += each[2]
                micro.append([l[0], l[1], number, direction])
            else:
                if location[l][0][2] != 0:
                    micro.append(location[l][0])
        # print(micro)
        m -= 1
    res = 0
    for each in micro:
        res += each[2]
    print(f'#{tc}', res)