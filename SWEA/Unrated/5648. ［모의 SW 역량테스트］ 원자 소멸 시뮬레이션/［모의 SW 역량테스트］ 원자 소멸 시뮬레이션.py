# 상(0), 하(1), 좌(2), 우(3)
# 0.5 충돌 가능
delta = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # x, y, direction, k
    atom = [list(map(int,input().split())) for _ in range(n)]

    res = 0

    # 원자 2개 이상만 충돌
    while len(atom) >= 2:
        # 원자 이동
        for i in range(len(atom)):
            atom[i][0] = atom[i][0] + delta[atom[i][2]][0]
            atom[i][1] = atom[i][1] + delta[atom[i][2]][1]

        # 부딪힌 애들 찾아주기 위해 딕셔너리 사용
        loc = {}
        for a in atom:
            if (a[0], a[1]) in loc:
                loc[(a[0],a[1])].append(a)
            else:
                loc[(a[0],a[1])] = [a]
        atom = []
        for i in loc:
            if len(loc[i]) >= 2:
                for a in loc[i]:
                    res += a[3]
            else:
                if -1000 <= loc[i][0][0] <= 1000 and -1000 <= loc[i][0][1] <= 1000:
                    atom.append(loc[i][0])
    print(f'#{tc}',res)