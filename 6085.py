w, h, b = map(int, input().split())
r = w*h*b/8/1024/1024
print(format(r, '.2f'), "MB")
# 1024*768*24/8/1024/1024