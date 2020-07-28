#MAP AND LAMBDA FUNCTION

    #Let's learn some new Python concepts! You have to generate a list of the first N fibonacci numbers,  being 0 the first number.
    #Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

    #Link = https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
    
cube = lambda x: x**3

def fibonacci(n):
    x = 0
    y = 1
    z = None
    i = 0
    numbers = list()
    if n >= 1:
        numbers.append(x)
        
    if n >= 2:
        numbers.append(y)
    if n > 2:
        while i < n-2:
            
            z = x + y
            numbers.append(z)
            x = y
            y = z     
            i += 1
        return numbers
    return numbers
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
   
