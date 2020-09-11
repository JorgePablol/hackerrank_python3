"""
INTRODUCTION TO SETS
  LINK = https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
"""

def average(arr):
    numbers = set(arr)
    return sum(numbers)/len(numbers)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
