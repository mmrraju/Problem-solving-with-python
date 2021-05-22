k, arr = int(input()), list(map(int, input().split()))

s1 = set()
s2 = set()

for i in arr:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)
ans = s1.difference(s2)
print(*list(ans))
