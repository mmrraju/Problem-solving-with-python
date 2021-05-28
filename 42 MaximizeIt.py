from itertools import product
k, m = map(int, input().split())

nums = []
for _ in range(k):
    row = map(int, input().split()[1:])
    nums.append(map((lambda x:x**2%m), row))

print(max(map((lambda x: sum(x)%m), product(*nums))))
