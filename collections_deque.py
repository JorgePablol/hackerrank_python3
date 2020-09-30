# COLLECTIONS.DEQUE()
# LINK = https://www.hackerrank.com/challenges/py-collections-deque/problem



from collections import deque
d = deque()
actions = {
    "append":d.append, 
    "appendleft": d.appendleft,
    "pop": d.pop,
    "popleft": d.popleft
}
for i in range(int(input())):
    action = input().split()
    if len(action)>1:
        x,y = action
        actions[x](int(y))
    else:
        actions[action[0]]()
print(*d)
