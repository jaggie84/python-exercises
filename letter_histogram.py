import collections
c = collections.Counter('banana')
sorted(c.items(), key=lambda c: c[0])
print(c)