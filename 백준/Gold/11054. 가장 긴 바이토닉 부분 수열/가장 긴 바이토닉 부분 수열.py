import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
reverse = arr[::-1]

increase = [1] * n
decrease = [1] * n


for i in range(n):
  for j in range(i):
    if arr[i] > arr[j]:
      increase[i] = max(increase[i], increase[j]+1)
    if reverse[i] > reverse[j]:
      decrease[i] = max(decrease[i], decrease[j]+1)

res = []
for i in range(n):
  res.append(increase[i]+decrease[n-i-1]-1)
print(max(res))