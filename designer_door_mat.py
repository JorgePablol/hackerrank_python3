# DESIGNER DOOR MAT

# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

#LINK = https://www.hackerrank.com/challenges/designer-door-mat/problem







def modeladora(n,m):
    symbol = '.|.'
    word = 'WELCOME'
    division = n//2
    for i in range(division):
        print((symbol*i).rjust(((m//2)-1), '-')+symbol+(symbol*i).ljust(((m//2)-1), '-'))
    
    print(word.center(m, '-'))

    for i in range(division-1, -1, -1):
        print((symbol*i).rjust(((m//2)-1), '-')+symbol+(symbol*i).ljust(((m//2)-1), '-'))

if __name__ == '__main__':
    n,m = map(int,(input().split()))
    
    result = modeladora(n,m)
    
