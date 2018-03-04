from collections import Iterable
l = ['1', '2', '3']
s = set(['4', '5', '6'])
d = {'1': 'a', '2': 'b', '3': 'c'}
t = ('x', 'y', 'z')

if isinstance(l, Iterable):
    for l1 in l:
        print(l1)
    print("\n")

if isinstance(s, Iterable):
    for s1 in s:
        print(s1)
    print("\n")

if isinstance(d, Iterable):
    for d1 in d:
        print(d1)
    print("\n")

if isinstance(t, Iterable):
    for t1 in t:
        print(t1)
    print("\n")
