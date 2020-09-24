# ITER TOOLS COMBINATIONS WITH REPLACEMENT
#   LINK = https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

s,n = input().split()
n = int(n)
s = sorted(s)

#action = combinations(s,n)
#for _ in s:
#    print(_)
#for i in range(1,n+1):
action = combinations_with_replacement(s,n)
for element in action:
    a = []
    for letters in element:
        a += letters
    print("".join(a))
