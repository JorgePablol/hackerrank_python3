# ITERTOOLS.PRODUCT()
# LINK = https://www.hackerrank.com/challenges/itertools-product/problem



from itertools import product

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = product(a,b)

for _ in c:
    print(_, end=" ")
