from collections import deque
MAX_NUMBER = 2001
s = int(input())
# 연산 3가지
# 복사 / 붙여넣기 / 1개 삭제하기

q = deque()
q.append((1, 0, 0))
visited = [[0]*MAX_NUMBER for _ in range(MAX_NUMBER)]

while q:
    number, clipboard, time = q.popleft()
    if number >= MAX_NUMBER or clipboard >= MAX_NUMBER:
        continue
    if number == s:
        print(time)
        break
    if visited[number][clipboard]:
        continue

    visited[number][clipboard] = 1

    #  현재 화면에 1개 이상이여야 복사와 삭제 실행
    if number > 0:
        q.append((number - 1, clipboard, time + 1))
        q.append((number, number, time+1))

    # 붙여넣기 -> 1개 이상만!
    if clipboard > 0:
        q.append((number+clipboard, clipboard, time+1))