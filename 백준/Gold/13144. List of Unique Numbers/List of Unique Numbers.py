import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

res = 0
left, right = 0, 0
visited = [0] * 100001

while left <= right and right < n:
    if not visited[nums[right]]:
        visited[nums[right]] = 1
        right += 1
        res += right-left

    else:
        while visited[nums[right]]:
            visited[nums[left]] = 0
            left += 1
print(res)