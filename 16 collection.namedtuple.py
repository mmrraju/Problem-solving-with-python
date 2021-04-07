from collections import namedtuple

n = int(input())
column = input().split()
total = 0
for i in range(n):
    students = namedtuple('student', column)
    column1, column2, column3, column4 = input().split()
    student = students (column1, column2, column3, column4)
    total +=int(student.MARKS)
print('{:.2f}'.format(total/n))
