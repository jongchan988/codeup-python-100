# 판짜기
pan = []
h = 10
w = 10
point_x = 1
point_y = 1
for i in range(h):
    pan.append([])
    for j in range(w):
        pan[i].append(0)

# 입력받기
for i in range(h):
    pan[i] = list(map(int, input().split()))

# 이동하기


while(True):
    if pan[point_x][point_y] == 2:
        pan[point_x][point_y] = 9
        break
    elif pan[point_x][point_y] == 0:
        pan[point_x][point_y] = 9
        if pan[point_x][point_y + 1] == 0 or pan[point_x][point_y + 1] == 2:
            point_y += 1
        elif pan[point_x  + 1][point_y] == 0 or pan[point_x + 1][point_y] == 2:
            point_x += 1
        else:
            break

# 출력하기
for i in range(h):
    for j in range(w):
        print(pan[i][j], end = " ")
    print()