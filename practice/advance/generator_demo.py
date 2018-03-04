# 列表生成式
from collections import Iterable
l = [1,2,3,4,5]
for l1 in l:
    print(l1*l1)

g = (l2 * l2 for l2 in l)
for g1 in g:
    print(g1)


print([l3 * l3 for l3 in l])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [str.lower() for str in L1 if isinstance(str,Iterable)]
print(L2)