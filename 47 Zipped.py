n, x = map(int, input().split())
subjects = []
for i in range(x):
    m = list(map(float, input().split()))
    subjects.append(m)
print(list(zip(*subjects)))
for subject in zip(*subjects):
    print(sum(subject)/len(subject))
