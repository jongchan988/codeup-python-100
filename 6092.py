n = int(input())
result = []
for i in range(23):
    result.append(0)


li = list(map(int, input().split()))

for i in range(n):
    result[li[i]-1] = result[li[i]-1] + 1
for i in range(23):
    print(result[i], end = " ")


