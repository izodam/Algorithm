import sys
input = sys.stdin.readline
def find_res():
    while True:
        check_number = u.pop()

        for i in range(len(u)):
            left = 0
            right = len(u) - 1

            while left <= right:
                now = u[i] + u[left] + u[right]
                if now == check_number:
                    print(check_number)
                    return
                elif now < check_number:
                    left += 1 
                else:
                    right -= 1


n = int(input())
u = [int(input()) for _ in range(n)]
u.sort()

find_res()