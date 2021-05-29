for _ in range(int(input())):
    a = int(input())
    a_set = set(map(int, input().split()))
    b = int(input())
    b_set = set(map(int, input().split()))
    if a_set.issubset(b_set):
        print('True')
    else:
        print('False')
