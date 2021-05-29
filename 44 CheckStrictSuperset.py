def issuppersubset(a, b):
    return b.issubset(a) and not (a.issubset(b))
a = set(input().split())
n = int(input())
res = True
for _ in range(n):
    b = set(input().split())
    res &= issuppersubset(a, b)
print(res)
