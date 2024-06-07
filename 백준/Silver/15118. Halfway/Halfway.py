def find_halfway_point(n):
    total_comparisons = n * (n - 1) // 2
    half_comparisons = (total_comparisons + 1) // 2  # (total + 1) // 2 to handle both odd and even cases

    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        # Calculate comparisons made by mid
        comparisons = mid * (2 * n - mid - 1) // 2
        if comparisons < half_comparisons:
            left = mid + 1
        else:
            right = mid

    return left

n = int(input())
print(find_halfway_point(n))
