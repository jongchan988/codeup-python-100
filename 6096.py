w = 19
h = 19
d = []

# 판짜기
for i in range(h):
    d.append([])

# 판 입력 받기
for i in range(h):
    d[i] = list(map(int, input().split()))

# 횟수 입력 받기
n = int(input())
for i in range(n):
    # 뒤집기
    x, y = map(int, input().split())
    x = x - 1
    y = y - 1
    for j in range(h):
        if d[x][j] == 1:
            d[x][j] = 0
        else :
            d[x][j] = 1

        if d[j][y] == 1:
            d[j][y] = 0
        else :
            d[j][y] = 1

# 출력
for i in range(h):
    for j in range(w):
        print(d[i][j], end = " ")
    print()