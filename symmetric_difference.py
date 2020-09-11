"""
SYMMETRIC DIFFERENCE
  LINK = https://www.hackerrank.com/challenges/symmetric-difference/problem
"""




if __name__ == '__main__':
    M = int(input())
    m = input().split()
    N = int(input())
    n = input().split()

    m = map(int,m)
    n = map(int,n)

    n = set(n)
    m = set(m)

    diff = n.difference(m) | m.difference(n)

    listeddiff = list(diff)
    
    for i in range(len(listeddiff)):
        valor_actual = listeddiff[i]
        posicion_actual = i
        while posicion_actual > 0 and listeddiff[posicion_actual -1] > valor_actual:
            listeddiff[posicion_actual] = listeddiff[posicion_actual-1]
            posicion_actual -=1
        listeddiff[posicion_actual] = valor_actual
            

    for i in range(len(listeddiff)):
            print(listeddiff[i])



