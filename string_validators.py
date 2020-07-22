# STRING VALIDATORS
    #Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
    #str.isalnum()
    #This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
    #Link = https://www.hackerrank.com/challenges/string-validators/problem
    
if __name__ == '__main__':
    S = input()
    print (any([char.isalnum() for char in S]))
    print (any([char.isalpha() for char in S]))
    print (any([char.isdigit() for char in S]))
    print (any([char.islower() for char in S]))
    print (any([char.isupper() for char in S]))
