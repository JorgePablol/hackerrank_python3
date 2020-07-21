# TUPLES:

#Task
#Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers.
#Then compute and print the result of hash(t).
#Link = https://www.hackerrank.com/challenges/python-tuples/problem


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    my_tuple = tuple(integer_list)

    print(hash(my_tuple))
