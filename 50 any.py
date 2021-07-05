n = int(input())
lst = list(input().split())
print(all([int(i)> 0 for i in lst]) and any([j == j[::-1] for j in lst]))
