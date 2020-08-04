# RE.START() AND RE.END()
    # These expressions return the indices of the start and end of the substring matched by the group.
    # Link = https://www.hackerrank.com/challenges/re-start-re-end/problem
    
import re
S = input()
k = input()
anymatch = 'No'
for m in re.finditer(r'(?=('+k+'))',S):
    anymatch = 'Yes'
    print((m.start(1),m.end(1)-1))
if anymatch == 'No':
    print((-1, -1))
