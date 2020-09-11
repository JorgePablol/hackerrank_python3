"""
SYMMETRIC DIFFERENCE
  LINK = https://www.hackerrank.com/challenges/symmetric-difference/problem
"""


n = int(input())
n_set = set(map(int,input().split()))
m = int(input())
m_set = set(map(int,input().split()))
result = m_set.symmetric_difference(n_set)
result = list(sorted(list(result)))
for i in result:
    print(i)



