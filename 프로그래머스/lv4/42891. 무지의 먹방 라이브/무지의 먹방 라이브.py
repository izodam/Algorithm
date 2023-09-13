import heapq

def solution(food_times, k):
    n = len(food_times)
    answer = -1
    if sum(food_times)<k:
        answer = -1
    
    q = []
    for i in range(n):
        #(음식 시간, 음식 번호)형태로 heapq에 삽입
        heapq.heappush(q,(food_times[i],i+1))
    food_num = n    #남은 음식 개수
    pre = 0         #이전에 제거한 음식의 시간
    
    while q:
        # 먹는데 걸리는 시간 = 남은 양 * 남은 음식 개수
        t = (q[0][0] - pre) * food_num
        # 시간이 남을 경우 현재 음식 빼기
        if k >= t:
            k -= t
            pre, _ = heapq.heappop(q)
            food_num -= 1
        # 시간이 부족할 경우 남은 음식 중에 먹어야 할 음식 찾기  
        else:
            idx = k%food_num
            q.sort(key=lambda x:x[1]) # 음식 번호를 기준으로 정렬
            answer = q[idx][1]
            break
    return answer
        
        

        
    
    
    
    