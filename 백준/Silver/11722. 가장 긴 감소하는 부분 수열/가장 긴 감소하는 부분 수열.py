def binary_search(target, lis):
    start = 0
    end = len(lis) - 1
    while start < end:
        mid = (start + end) // 2
        if lis[mid] == target:
            return mid
        elif lis[mid-1] > target > lis[mid]:
            return mid
        elif target > lis[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return start


n = int(input())
lst = list(map(int,input().split()))

lis = [lst[0]]

for target in lst[1:]:
    if lis[-1] > target:
        lis.append(target)
    else:
        idx = binary_search(target, lis)
        lis[idx] = target

print(len(lis))