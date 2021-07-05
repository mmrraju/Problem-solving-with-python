
n, m = map(int, input().split())
rows = [list(map(int, input().split())) for i in range(n)]
k = int(input())
rows.sort(key=lambda x: x[k])
for line in rows:
    print(*line, sep=" ")
