import sys
input = sys.stdin.readline

#이분탐색
def binary_search(s,e,note1,num):
       while s<=e:
              mid = (s+e)//2
              if note1[mid] == num:
                     return 1
              elif note1[mid] > num:
                     e = mid - 1
              else:
                     s = mid + 1
       return 0

t = int(input())
for _ in range(t):
       n = int(input())
       note1 = list(map(int,input().split()))
       note1.sort()
       m = int(input())
       note2 = list(map(int,input().split()))

       for i in note2:
              print(binary_search(0,n-1,note1,i))