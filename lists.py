# LISTS:

#Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above(see link). 
#Iterate through each command in order and perform the corresponding operation on your list.
#Link = https://www.hackerrank.com/challenges/python-lists/problem


if __name__ == '__main__':
    N = int(input())
    the_list = list()

    for _ in range(N):
        query = input().split()
        if query[0] == "print":
            print(the_list)
        elif query[0] == "insert":
            the_list.insert(int(query[1]), int(query[2]))
        elif query[0] == "remove":
            the_list.remove(int(query[1]))
        elif query[0] == "append":
            the_list.append(int(query[1]))
        elif query[0] == "sort":
            the_list = sorted(the_list)
        elif query[0] == "pop":
            the_list.pop()
        elif query[0] == "reverse":
            the_list.reverse()

    
    
