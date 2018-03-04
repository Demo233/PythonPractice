# 定义一个函数熟悉 1.必选参数2.默认参数3.可变参数4.命名关键字参数5.关键字参数
# def sayHello(name,telephone='',**address):
#     print("hello ", name, telephone,address)
#
# t = ('luoyang','shanghai')
# sayHello('Zhao Yihao','17621860036',city="luoyang")


# 利用递归函数计算阶乘

def fect(number):
    if(number == 1):
        return 1
    else:
        return number * fect(number - 1)

while True:
    str = input("需要求几的阶乘?")
    number = int(str)
    print("%s的阶乘为:%s" % (str,fect(number)))


