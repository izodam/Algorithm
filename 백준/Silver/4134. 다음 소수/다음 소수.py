import math
t = int(input())
for _ in range(t):
       n = int(input())
       if n == 0 or n == 1:
              n = 2
       while True:
              for i in range(2, int(math.sqrt(n)) + 1):
                     if n % i == 0:
                            n += 1
                            break
              else:
                     print(n)
                     break