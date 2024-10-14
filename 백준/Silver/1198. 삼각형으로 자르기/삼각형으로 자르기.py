from itertools import combinations
import sys
input = sys.stdin.readline


def triangle_area(x, y, z):
    return abs((x[0]*y[1]+y[0]*z[1]+z[0]*x[1]-x[1]*y[0]-y[1]*z[0]-z[1]*x[0]))/2


max_area = []
a = []

n = int(input())
jum = [list(map(int,input().split())) for _ in range(n)]

jum_list = list(combinations(jum, 3))
for k in range(len(jum_list)):
    max_area.append(triangle_area(jum_list[k][0], jum_list[k][1], jum_list[k][2]))
print(max(max_area))