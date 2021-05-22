num_e = int(input())
e = set(map(int, input().split()))

num_f = int(input())
f = set(map(int, input().split()))

print(len(e.intersection(f)))
