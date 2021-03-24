a = int(input())
m = list(map(int, input().split()))

b = int(input())
n = list(map(int, input().split()))

lis = sorted(set(m).symmetric_difference(set(n)))

print(*lis, sep='\n')
