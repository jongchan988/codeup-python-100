h, d, c, s = map(int, input().split())

r = h * d * c * s /8/1024/1024
print(format(r, '.1f'), "MB")
# 44100*16*2*1/8/1024/1024