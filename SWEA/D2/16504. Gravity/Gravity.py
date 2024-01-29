T = int(input())

for t in range(T):
    N = int(input())        # 상자가 쌓여있는 가로 길이
    arr = list(map(int,input().split()))

    # 해당 상자보다 높이가 낮은 상자들의 개수가 답

    max_v = 0       # 가장 큰 낙차

    for i in range(N-1):
        cnt = 0     # 오른쪽에 있는 더 낮은 높이의 개수
        for j in range(i+1, N):
            if arr[j] < arr[i]:
                cnt += 1
        if max_v < cnt:
            max_v = cnt

    print(f'#{t+1} {max_v}')