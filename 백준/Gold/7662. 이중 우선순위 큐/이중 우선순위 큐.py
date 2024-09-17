import sys
input = sys.stdin.readline
import heapq

t = int(input())

for tc in range(t):
    k = int(input())
    # ‘I n’은 정수 n을 Q에 삽입하는 연산
    # ‘D -1’는 Q 에서 최솟값을 삭제하는 연산
    # ‘D 1’는 Q에서 최댓값을 삭제하는 연산
    # Q가 비어있는데 적용할 연산이 ‘D’라면 이 연산은 무시

    min_heap = []
    max_heap = []
    visited = [0] * 1000001
    for i in range(k):
        operator, n = input().split()
        if operator == 'I':
            heapq.heappush(min_heap, (int(n), i))
            heapq.heappush(max_heap, (-int(n), i))
            visited[i] = 1

        else:
            # 최소 힙
            if n == '-1':
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)

                if min_heap:
                    visited[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)

            if n == '1':
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)


    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if len(min_heap) == 0 or len(max_heap) == 0:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
