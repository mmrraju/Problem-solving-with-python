from collections import Counter

numberOfShoes = int(input())
shoes = Counter(map(int, input().split()))
numberOfCustomer = int(input())
income = 0
for i in range(numberOfCustomer):
    size, price = map(int , input().split())
    if shoes[size]:
        income = income+price
        shoes[size] -= 1
print(income)
