# CHECK SUBSET
# LINK = https://www.hackerrank.com/challenges/py-check-subset/problem


cases = int(input())


for i in range(cases):
    elements = int(input())
    set_a = set(map(int, input().split()))
    elements_b = int(input())
    set_b = set(map(int, input().split()))

    print(set_a.issubset(set_b))
