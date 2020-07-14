#PRINT FUNCTION:
#
#The included code stub will read an integer, , from STDIN.
#Without using any string methods, try to print the following:
    #123...n
#Note that "" represents the consecutive values in between.

if __name__ == '__main__':
    n = int(input())
    numeritos = []
    for i in range(1,n+1):
        numeritos.append(i)

    numeritos = map(str, numeritos)
    print("".join(numeritos))
    
    
