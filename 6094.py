n = int(input())
li = list(map(int, input().split()))
max = 10000
result = max
for i in range(n):
    if result > li[i]:
        result = li[i]
print(result)