import sys
input = sys.stdin.readline

def solve(picked):
    global answer
    if len(picked) == N:
        for n in include_numbers:
            if n not in picked:
                break
        else:
            answer += 1
        return

    for n in range(10):
        picked.append(n)
        solve(picked)
        picked.pop()

N, M = map(int, input().split())
include_numbers = list(map(int, input().split()))
numbers = [n for n in range(10)]

answer = 0
for n in range(10):
    picked = []
    picked.append(n)
    solve(picked)
    picked.pop()
print(answer)