for i in range(int(input())):
    n , k = map(int, input().split())
    lst = list(map(int, input().split()))
    l = len(lst)
    y = 0
    for i in range(l):
        if lst[i]<=0:
            y+=1 
    if y >= k:
        print('NO')
    else:
        print('YES')
