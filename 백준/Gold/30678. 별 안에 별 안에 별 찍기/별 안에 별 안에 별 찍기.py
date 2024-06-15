# 30678

def create_star(n):
    if n == 0:
        return ["*"]

    prev_pattern = create_star(n - 1)
    size = len(prev_pattern)
    empty_line = " " * size

    new_pattern = []

    # 상단 부분
    for line in prev_pattern:
        new_pattern.append(empty_line*2 + line + empty_line*2)

    # 중간 상단 부분
    for line in prev_pattern:
        new_pattern.append(empty_line*2 + line + empty_line*2)

    # 가운데 부분
    for line in prev_pattern:
        new_pattern.append(line * 5)

    # 중간 하단 부분
    for line in prev_pattern:
        new_pattern.append(empty_line + line*3 + empty_line)

    # 하단 부분
    for line in prev_pattern:
        new_pattern.append(empty_line + line + empty_line + line + empty_line)

    return new_pattern


def print_star(n):
    pattern = create_star(n)
    for line in pattern:
        print(line)



n = int(input())
print_star(n)