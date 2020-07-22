#STRING SPLIT AND JOIN                  
    #In Python, a string can be split on a delimiter.
    #Task: You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
    #Link = https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
