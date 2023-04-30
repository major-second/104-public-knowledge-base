from time import time
from collections import deque
a = list(range(100000))
b = deque(a.copy())

t = time()
for i in range(10000):
  a.append(a[0])
  a.pop(0)
print(time() - t)

t = time()
for i in range(10000):
  b.append(b[0])
  b.popleft()
print(time() - t)

print(deque(a) == b)