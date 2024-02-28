from collections import deque
T = int(input())
for tc in range(1, T + 1):
    # 빈 창구가 여러 곳인 경우 창구번호가 작은 곳으로 간다
    # 정비 창구
    # 먼저 기다리는 고객이 우선
    # 두명 동시 접수창고 끝나면 창구 번호 작은 고객이 우선

    # 접수 창구의 개수 N, 정비 창구의 개수 M,
    # 차량 정비소를 방문한 고객의 수 K,
    # 지갑을 두고 간 고객이 이용한 접수 창구번호 A와 정비 창구번호 B
    n, m, k, a, b = map(int, input().split())
    reception = list(map(int, input().split()))
    repair = list(map(int, input().split()))
    customer = list(map(int, input().split()))

    # 접수 대기 -> 인덱스 넣어줌
    c = deque()
    # 수리 대기
    p = deque()

    counter_reception = [-1] * n
    counter_repair = [-1] * m

    idx_coustomer = 0
    l_coustomer = len(customer)

    # 방문기록 저장
    visit = [[-1,-1] for _ in range(k)]

    time = 0
    while True:
        # 정비 창구에서 일 다 본 사람 빼기
        for i in range(m):
            if counter_repair[i] != -1 and counter_repair[i][1] == 0:
                counter_repair[i] = -1
        # 접수 창구 끝난 사람 정비 창구 대기열에 넣기
        for i in range(n):
            if counter_reception[i] != -1 and counter_reception[i][1] == 0:
                p.append(counter_reception[i][0])
                counter_reception[i] = -1

        # 들어 온 사람 접수 창구 대기열에 넣기
        for i in range(idx_coustomer, l_coustomer):
            if customer[i] == time:
                c.append(i)
            else:
                idx_coustomer = i
                break

        # 정비 창구 비어있으면 사람 옮기기
        for i in range(m):
            if counter_repair[i] == -1 and p:
                idx = p.popleft()
                counter_repair[i] = [idx, repair[i]-1]
                visit[idx][1] = i
            # 정비 창구 차있으면 시간 지났으니까 -1
            elif counter_repair[i] != -1:
                counter_repair[i][1] -= 1

        # 접수 창구 비어있으면 사람 옮기기
        for i in range(n):
            if counter_reception[i] == -1 and c:
                idx = c.popleft()
                counter_reception[i] = [idx, reception[i]-1]
                visit[idx][0] = i
            # 접수 창구 차있으면 시간 지났으니까 -1
            elif counter_reception[i] != -1:
                counter_reception[i][1] -= 1

        time += 1

        # 모든 사람 일 끝났는지 확인  -> while 끝내기 위함
        for i in range(k):
            if visit[i][1] == -1:
                break
        else:
            break
    res = 0
    for i in range(k):
        if visit[i][0] == a-1 and visit[i][1] == b-1:
            res += (i+1)

    if not res:
        res = -1

    print(f'#{tc}',res)