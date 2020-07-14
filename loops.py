#LOOPS:
    #Task
    #The provided code stub reads and integer,n , from STDIN. For all non-negative integers i<n , print i^2.
#Link = https://www.hackerrank.com/challenges/python-loops/problem

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)
