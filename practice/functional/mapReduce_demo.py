from functools import reduce

# 1.利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# map(f,[1,2,3]) -> f(1)/f(2)/f(3) 的 generator
# def change(str):
#     return str.capitalize()
#
# l = ['adam', 'LISA', 'barT']
# l1 = list(map(change,l))
# print(l1)

# 注:upper 全部转大写、lower全部转小写,capitalize 首字母大写其余小写,title把每个单词首字母改为大写,其余全部小写

# 2.Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# reduce(f,[1,2,3]) -> f(f(1,2),3)

# def prod(x,y):
#     return  x * y
#
#
# l = [1,2,3,4]
# l1 = reduce(prod,l)
# print(l1)


# 3.利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

# 自己尝试的方法

# def str2float(str):
#     arr = str.split(".");
#     pre = arr[0]
#     suf = arr[1]
#     def nn(ch):
#         d = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#         return d[ch]
#     def xx(x,y):
#         return x * 10 + y
#     def zz(a,b):
#         print(a,b)
#         return a * 0.1 + b * 0.01
#     return reduce(xx,list(map(nn,pre))) + reduce(zz,list(map(nn,suf)))
#
# str = '123.456'
# f = str2float(str)
# print(f)
# print(isinstance(f,float))

# def nn(ch):
#     d = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#     return d[ch]
#
# def zz(a,b):
#     return a * 0.1 + b
#
# print(reduce(zz,list(map(nn,'654')))*0.1)

# 参考的方法

s = '546512.21312'
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

a, b = s.split(".", 1)   #分离整数与小数

def str2listnum(ab):     #通过字典把字符串改成数字类型
    return DIGITS[ab]

def intnum(a):           #计算整数部分
    def fn(x, y):
        return x * 10 + y
    return reduce(fn, map(str2listnum, a))

def floatnum(b):         #计算小数部分
    def fn(x, y):
        return x * 10 + y
    fb = reduce(fn, map(str2listnum, b)) #和整数计算一样  456
    dot = len(list(map(str2listnum, b))) #小数列表包含位数  3
    return fb / (10**dot)  #除以10的次数即小数列表的位数

print(intnum(a) + floatnum(b))   #返回整数＋小数的值,自动为float
print(isinstance(intnum(a) + floatnum(b),float))


# print(str.split(".")[0])
# print(1*100+2*10+3+4*(1/10)+5*(1/100)+6*(1/1000))