# COLLECTIONS COUNTER
# LINK = https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

n_shoes = int(input())

shoe_sizes = Counter(input().split())

n_customers = int(input())
earnings = 0
for i in range(n_customers):
    task,payment = None, None
    task, payment = input().split()

    if shoe_sizes[task]:
        earnings = earnings + int(payment)
        shoe_sizes[task] = shoe_sizes[task]-1

print(earnings)
