# 使用yield函数将字符串的每个字符的ascii码打印出来
def each_str(str):
    for ch in str:
        yield ord(ch)
    return '%s chars' % len(str)

# 方法1:
for x in each_str('abc'):
    print(x)

# 方法2:
g = each_str("xyz")
try:
    while True:
        print(next(g))
except Exception as e:
    print(e.value)
