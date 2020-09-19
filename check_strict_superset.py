# CHECK STRICT SUPERSET
# LINK = https://www.hackerrank.com/challenges/py-check-strict-superset/problem



# Enter your code here. Read input from STDIN. Print output to STDOUT
set_a = set(map(int, input().split()))
n = int(input())
empty_set = set()
comparizon = list()
for i in range(n):
    empty_set = set(map(int, input().split()))
    if set_a.issuperset(empty_set):
        comparizon.append(True)
    else:
        comparizon.append(False)

print(all(comparizon))  
