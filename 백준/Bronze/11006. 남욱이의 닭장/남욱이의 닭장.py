t = int(input())

for _ in range(t) :
  n, m = map(int, input().split())
  u = (m*2) - n
  x = n - m
  print(u, x)