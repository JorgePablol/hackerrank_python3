# ITERTOOLS PERMUTATIONS
# LINK = https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

s,n = input().split()
n = int(n)
s = sorted(s)

action = permutations(s,n)

for element in action:
    a = []
    for letters in element:
        a += letters
    print("".join(a))
