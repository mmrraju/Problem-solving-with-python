from collections import deque

d = deque()
for _ in range(int(input())):
    s = input().split()
    getattr(d, s[0])(*[s[1]] if len(s) >1 else [])
print(*[item for item in d])
