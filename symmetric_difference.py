e = int(input())
e_space = set(input().split())

f = int(input())
f_space = set(input().split())

print(len(e_space.symmetric_difference(f_space)))
