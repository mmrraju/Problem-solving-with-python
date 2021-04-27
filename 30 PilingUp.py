from collections import deque

for _ in range(int(input())):
    n = int(input())
    lst = deque(map(int, input().split()))
    for cube in reversed(sorted(lst)):
        if lst[-1] == cube:
            lst.pop()
        elif lst[0] == cube:
            lst.popleft()
        else:
            print('No')
            break
    else:
        print('Yes')
        
