#DETECTING FLOATING POINT NUMBER:
#    You are given a string N .
#Your task is to verify that N is a floating point number.
#
#In this task, a valid float number must satisfy all of the following requirements
#Link = https://www.hackerrank.com/challenges/introduction-to-regex/problem

#REAL SOLUTION:

import re
    for i in range(int(input())):
        print(bool(re.search(r"^[+-]?\d*\.\d+$",input().strip())))
        
#MY SOLUTION:

import re
test_cases = int(input())


for element in range(test_cases):
    n = input()
    check = re.search(r".", n)
    trust = None
    if check:
        try:
            conversion = float(n)
            if conversion:
                trust = True
            print(trust)
        except:
            trust = False
            print(trust)
    elif check == False:
        trust = False
        print(trust)
