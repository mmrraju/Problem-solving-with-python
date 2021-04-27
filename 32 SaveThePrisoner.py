for _ in range(int(input())):
    n, m, s = list(map(int, input().split()))
    print(((s+m-2)%n) + 1)
