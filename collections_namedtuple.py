# COLLECTIONS.NAMEDTUPLE()
# LINK = https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

n = int(input())
cols = ','.join(input().split())
task = namedtuple('task', cols)
suma = 0
for i in range(n):
    row = input().split()
    tank = task(*row)
    suma += int(tank.MARKS)

print(suma/n)
