#RE.FINDALL() AND RE.FINDITER():
    #The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings.
    #Link = https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
    
import re
consonants = 'qwrtypsdfghjklzxcvbnm'
vowels = 'aeiou'
match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',input(),flags = re.I)

if match:
    for i in match:
        print(i)
else:
    print ('-1')
